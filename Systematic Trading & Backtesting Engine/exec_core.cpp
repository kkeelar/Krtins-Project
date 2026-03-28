#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <atomic>
#include <chrono>
#include <condition_variable>
#include <cstdint>
#include <mutex>
#include <queue>
#include <thread>
#include <vector>
#include <limits>
#include <random>

namespace py = pybind11;
using namespace pybind11::literals;

struct Order {
    int idx;               // asset index
    int qty;               // absolute quantity
    int side;              // +1 buy, -1 sell
    double price;          // top-of-book price
    double volume;         // available volume snapshot
    int order_type;        // 0=market, 1=limit
    double limit_price;    // relevant if order_type==1
    std::int64_t signal_ts_ns;  // from python
    std::chrono::steady_clock::time_point submit_ts;
};

struct StepContext {
    std::atomic<int> remaining{0};
    std::vector<double> latencies_ns;  // per order
    std::atomic<int> rejected{0};
};

class ExecutionEngine {
   public:
    ExecutionEngine(double transaction_cost,
                    double slippage,
                    double starting_cash,
                    double gross_leverage_cap,
                    double liquidity_factor = 0.05,
                    double impact_k = 0.1,
                    double max_pos_frac = 0.2,
                    double base_latency_ns = 1e4,
                    double queue_latency_ns = 5e3,
                    double noise_latency_ns = 5e3)
        : txn_cost_(transaction_cost),
          slippage_(slippage),
          cash_(starting_cash),
          gross_cap_(gross_leverage_cap),
          liquidity_factor_(liquidity_factor),
          impact_k_(impact_k),
          max_pos_frac_(max_pos_frac),
          base_latency_ns_(base_latency_ns),
          queue_latency_ns_(queue_latency_ns),
          noise_latency_ns_(noise_latency_ns),
          stop_(false) {
        worker_ = std::thread([this]() { this->run(); });
    }

    ~ExecutionEngine() {
        stop_ = true;
        queue_cv_.notify_all();
        if (worker_.joinable()) worker_.join();
    }

    // One timestep; orders aligned to prices indices
    py::dict step(const std::vector<double>& prices,
                  const std::vector<int>& qty,
                  const std::vector<int>& side,
                  double signal_ts_ns,
                  const std::vector<double>& volumes = {},
                  const std::vector<int>& order_type = {},
                  const std::vector<double>& limit_price = {}) {
        const auto submit_time = std::chrono::steady_clock::now();

        if (prices.size() != qty.size() || prices.size() != side.size()) {
            throw std::runtime_error("prices, qty, side must align");
        }

        // capture price snapshot for risk calculations
        {
            std::lock_guard<std::mutex> lock(price_mtx_);
            prices_snapshot_ = prices;
            if (positions_.size() < prices.size()) {
                positions_.resize(prices.size(), 0.0);
            }
            volumes_snapshot_ = volumes;
            if (volumes_snapshot_.empty()) {
                volumes_snapshot_.assign(prices.size(), std::numeric_limits<double>::infinity());
            }
        }

        auto ctx = std::make_shared<StepContext>();
        ctx->latencies_ns.reserve(qty.size());

        int order_count = 0;
        for (size_t i = 0; i < prices.size(); ++i) {
            if (qty[i] == 0 || side[i] == 0) continue;
            double vol = i < volumes_snapshot_.size() ? volumes_snapshot_[i] : std::numeric_limits<double>::infinity();
            int otype = (i < order_type.size()) ? order_type[i] : 0;
            double lmt = (i < limit_price.size()) ? limit_price[i] : 0.0;
            Order o{static_cast<int>(i), std::abs(qty[i]), side[i], prices[i],
                    vol, otype, lmt, static_cast<std::int64_t>(signal_ts_ns), submit_time};
            {
                std::lock_guard<std::mutex> lock(queue_mtx_);
                ctx->remaining.fetch_add(1, std::memory_order_relaxed);
                queue_.emplace(o, ctx);
            }
            order_count++;
        }

        if (order_count == 0) {
            return build_result(signal_ts_ns, submit_time, submit_time, *ctx);
        }

        queue_cv_.notify_one();

        // wait until all orders processed
        std::unique_lock<std::mutex> lock(step_mtx_);
        step_cv_.wait(lock, [&ctx]() { return ctx->remaining.load() == 0; });

        const auto done_time = std::chrono::steady_clock::now();
        return build_result(signal_ts_ns, submit_time, done_time, *ctx);
    }

    std::vector<double> get_positions() const { return positions_; }
    double get_cash() const { return cash_; }

   private:
    void run() {
        while (!stop_) {
            std::pair<Order, std::shared_ptr<StepContext>> item;
            {
                std::unique_lock<std::mutex> lock(queue_mtx_);
                queue_cv_.wait(lock, [this]() { return stop_ || !queue_.empty(); });
                if (stop_ && queue_.empty()) break;
                item = std::move(queue_.front());
                queue_.pop();
            }
            process_order(item.first, *item.second);
        }
    }

    void process_order(const Order& o, StepContext& ctx) {
        auto exec_time = std::chrono::steady_clock::now();

        // ensure positions vector sized
        if (positions_.size() <= static_cast<size_t>(o.idx)) {
            positions_.resize(o.idx + 1, 0.0);
        }

        double price = o.price;
        if (price <= 0 || std::isnan(price)) {
            ctx.rejected.fetch_add(1, std::memory_order_relaxed);
            finish_order(ctx, o, exec_time);
            return;
        }

        // Limit order check
        if (o.order_type == 1) {
            if ((o.side > 0 && price > o.limit_price) || (o.side < 0 && price < o.limit_price)) {
                ctx.rejected.fetch_add(1, std::memory_order_relaxed);
                finish_order(ctx, o, exec_time);
                return;
            }
        }

        double avail_vol = (o.volume > 0 && !std::isinf(o.volume)) ? o.volume : std::numeric_limits<double>::infinity();
        double max_fill = std::isinf(avail_vol) ? static_cast<double>(o.qty) : avail_vol * liquidity_factor_;
        double filled_qty = std::min(static_cast<double>(o.qty), max_fill);
        if (filled_qty <= 0) {
            ctx.rejected.fetch_add(1, std::memory_order_relaxed);
            finish_order(ctx, o, exec_time);
            return;
        }

        double impact = 0.0;
        if (!std::isinf(avail_vol) && avail_vol > 0) {
            impact = impact_k_ * (filled_qty / avail_vol);
        }

        double dir = (o.side > 0 ? 1.0 : -1.0);
        double exec_price = price * (1.0 + dir * slippage_ + dir * impact);
        double notional = exec_price * filled_qty * dir;
        double fee = std::abs(notional) * txn_cost_;

        // risk: projected cash and gross exposure
        double projected_cash = cash_ - notional - fee;
        double projected_pos = positions_[o.idx] + filled_qty * o.side;

        std::vector<double> snapshot;
        {
            std::lock_guard<std::mutex> lock(price_mtx_);
            snapshot = prices_snapshot_;
        }

        double gross_with = current_gross_with(snapshot, o.idx, projected_pos);
        double projected_equity = projected_cash + gross_with;
        double gross_after = projected_equity != 0.0 ? gross_with / std::abs(projected_equity) : 0.0;

        double pos_limit_notional = max_pos_frac_ * std::abs(projected_equity);
        double projected_notional = std::abs(projected_pos * price);
        if (pos_limit_notional > 0 && projected_notional > pos_limit_notional) {
            ctx.rejected.fetch_add(1, std::memory_order_relaxed);
            finish_order(ctx, o, exec_time);
            return;
        }

        if (projected_cash < 0 || (gross_cap_ > 0 && gross_after > gross_cap_)) {
            ctx.rejected.fetch_add(1, std::memory_order_relaxed);
            finish_order(ctx, o, exec_time);
            return;
        }

        // apply
        positions_[o.idx] = projected_pos;
        cash_ = projected_cash;

        finish_order(ctx, o, exec_time);
    }

    void finish_order(StepContext& ctx, const Order& o, const std::chrono::steady_clock::time_point& exec_time) {
        size_t qsize = queue_.size();
        double noise = noise_dist_(rng_) * noise_latency_ns_;
        double queue_delay = static_cast<double>(qsize) * queue_latency_ns_;
        double latency_ns = base_latency_ns_ + queue_delay + noise;
        if (latency_ns < 0) latency_ns = 0;
        ctx.latencies_ns.push_back(latency_ns);
        ctx.remaining.fetch_sub(1, std::memory_order_relaxed);
        if (ctx.remaining.load() == 0) {
            std::lock_guard<std::mutex> lock(step_mtx_);
            step_cv_.notify_all();
        }
    }

    // helper to compute gross with current positions and provided snapshot
    double current_gross(const std::vector<double>& prices) const {
        double gross = 0.0;
        size_t n = std::min(prices.size(), positions_.size());
        for (size_t i = 0; i < n; ++i) {
            gross += std::abs(positions_[i] * prices[i]);
        }
        return gross;
    }

    double current_gross_with(const std::vector<double>& prices, size_t idx, double new_pos) const {
        double gross = 0.0;
        size_t n = std::min(prices.size(), positions_.size());
        for (size_t i = 0; i < n; ++i) {
            if (i == idx) {
                gross += std::abs(new_pos * prices[i]);
            } else {
                gross += std::abs(positions_[i] * prices[i]);
            }
        }
        return gross;
    }

    py::dict build_result(double signal_ts_ns,
                          const std::chrono::steady_clock::time_point& submit,
                          const std::chrono::steady_clock::time_point& done,
                          StepContext& ctx) {
        double avg = 0.0;
        double p95 = 0.0;
        if (!ctx.latencies_ns.empty()) {
            for (double v : ctx.latencies_ns) avg += v;
            avg /= static_cast<double>(ctx.latencies_ns.size());
            auto copy = ctx.latencies_ns;
            std::sort(copy.begin(), copy.end());
            size_t idx = static_cast<size_t>(std::ceil(copy.size() * 0.95)) - 1;
            p95 = copy[idx];
        }

        double e2e = std::chrono::duration_cast<std::chrono::nanoseconds>(done - submit).count();

        return py::dict(
            "positions"_a = positions_,
            "cash"_a = cash_,
            "avg_latency_ns"_a = avg,
            "p95_latency_ns"_a = p95,
            "rejected"_a = ctx.rejected.load(),
            "orders_processed"_a = static_cast<int>(ctx.latencies_ns.size()),
            "e2e_latency_ns"_a = e2e);
    }

    // members
    double txn_cost_;
    double slippage_;
    double cash_;
    double gross_cap_;
    double liquidity_factor_;
    double impact_k_;
    double max_pos_frac_;
    double base_latency_ns_;
    double queue_latency_ns_;
    double noise_latency_ns_;
    std::vector<double> positions_;
    std::vector<double> prices_snapshot_{};
    std::vector<double> volumes_snapshot_{};
    std::mutex price_mtx_;

    std::atomic<bool> stop_;
    std::thread worker_;

    std::queue<std::pair<Order, std::shared_ptr<StepContext>>> queue_;
    std::mutex queue_mtx_;
    std::condition_variable queue_cv_;

    std::mutex step_mtx_;
    std::condition_variable step_cv_;

    std::mt19937 rng_{std::random_device{}()};
    std::normal_distribution<double> noise_dist_{0.0, 1.0};
};

PYBIND11_MODULE(exec_core, m) {
    py::class_<ExecutionEngine>(m, "ExecutionEngine")
        .def(py::init<double, double, double, double, double, double, double, double, double, double>(),
             py::arg("transaction_cost"),
             py::arg("slippage"),
             py::arg("starting_cash"),
             py::arg("gross_leverage_cap"),
             py::arg("liquidity_factor") = 0.05,
             py::arg("impact_k") = 0.1,
             py::arg("max_pos_frac") = 0.2,
             py::arg("base_latency_ns") = 1e4,
             py::arg("queue_latency_ns") = 5e3,
             py::arg("noise_latency_ns") = 5e3)
        .def("step", &ExecutionEngine::step,
             py::arg("prices"),
             py::arg("qty"),
             py::arg("side"),
             py::arg("signal_ts_ns"),
             py::arg("volumes") = std::vector<double>(),
             py::arg("order_type") = std::vector<int>(),
             py::arg("limit_price") = std::vector<double>())
        .def("get_positions", &ExecutionEngine::get_positions)
        .def("get_cash", &ExecutionEngine::get_cash);
}

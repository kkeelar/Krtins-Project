# Convert trading signals into simulated portfolio performance #
from __future__ import annotations

from typing import Dict, List, Tuple

from pathlib import Path
import csv

import numpy as np
import pandas as pd
try:
    from tabulate import tabulate
except ImportError:
    tabulate = None
try:
    import exec_core  # type: ignore
except ImportError:
    exec_core = None

TRANSACTION_COST = 0.001  # 0.1% per trade #
SLIPPAGE = 0.0005  # 0.05% price penalty #
STARTING_CASH = 100_000.0
DEFAULT_GROSS_LEVERAGE_CAP = 1.5  # cap gross notional / equity #

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

from metrics import max_drawdown, sharpe_ratio, cagr, hit_rate


# Run a simple backtest with equal-weight position sizing #
def backtest(
    signals: pd.DataFrame,
    data: Dict[str, pd.DataFrame],
    use_vol_targeting: bool = False,
    vol_window: int = 20,
    gross_leverage_cap: float = DEFAULT_GROSS_LEVERAGE_CAP,
    risk_free_rate: float = 0.0,
    use_cpp_engine: bool = True,
) -> pd.DataFrame:
    if signals.empty:
        raise ValueError("signals cannot be empty")
    missing = [t for t in signals.columns if t not in data]
    if missing:
        raise ValueError(f"price data missing for: {missing}")

    # Align prices to signal dates #
    closes = {t: df["Close"].reindex(signals.index).ffill() for t, df in data.items()}
    prices = pd.DataFrame(closes)

    returns = prices.pct_change()
    vol = returns.rolling(vol_window).std().shift(1) * np.sqrt(252)
    vol = vol.reindex(signals.index)

    eps = 1e-8

    # optional C++ engine
    use_cpp = use_cpp_engine and exec_core is not None

    tickers = list(signals.columns)
    index_lookup = {t: i for i, t in enumerate(tickers)}

    if use_cpp:
        engine = exec_core.ExecutionEngine(TRANSACTION_COST, SLIPPAGE, STARTING_CASH, gross_leverage_cap)
        cpp_positions = np.zeros(len(tickers))
        cash = STARTING_CASH
        latencies = []
        rejections = 0
    else:
        cash = STARTING_CASH
        positions = {t: 0.0 for t in signals.columns}  # shares #
        turnover_records: List[Tuple[pd.Timestamp, float]] = []
        skipped_prices: List[Tuple[pd.Timestamp, str]] = []

    portfolio_values = []

    for dt, row in signals.iterrows():
        # Identify active scores #
        active = row.copy()
        if active.abs().sum() == 0 or active.isna().all():
            target_shares = {t: 0.0 for t in signals.columns}
        else:
            # pull current positions snapshot
            if use_cpp:
                current_positions = {t: cpp_positions[index_lookup[t]] for t in tickers}
            else:
                current_positions = positions

            total_value = cash + sum(current_positions[t] * prices.at[dt, t] for t in current_positions)

            # score-based weights
            if use_vol_targeting:
                day_vol = vol.loc[dt]
                inv_vol = 1 / day_vol.replace(0, np.nan).clip(lower=eps)
                raw_scores = active * inv_vol
            else:
                raw_scores = active

            denom = raw_scores.abs().sum()
            if denom == 0 or np.isnan(denom):
                weights = pd.Series(0, index=active.index, dtype=float)
            else:
                weights = raw_scores / denom

            alloc_per_dollar = weights * total_value
            raw_target_shares = {
                t: alloc_per_dollar.get(t, 0.0) / prices.at[dt, t] if prices.at[dt, t] != 0 else 0.0
                for t in signals.columns
            }

            # Enforce gross leverage cap by scaling targets if needed #
            gross_notional = sum(abs(raw_target_shares[t]) * prices.at[dt, t] for t in signals.columns)
            portfolio_equity = cash + sum(current_positions[t] * prices.at[dt, t] for t in current_positions)
            gross_limit = gross_leverage_cap * portfolio_equity
            scale = 1.0 if gross_notional == 0 else min(1.0, gross_limit / gross_notional)
            target_shares = {t: raw_target_shares[t] * scale for t in signals.columns}

        if use_cpp:
            trades = {t: target_shares[t] - cpp_positions[index_lookup[t]] for t in tickers}
            qty_vec = []
            side_vec = []
            price_vec = []
            for t in tickers:
                idx = index_lookup[t]
                delta = trades[t]
                price = prices.at[dt, t]
                if np.isnan(delta) or np.isnan(price):
                    qty_vec.append(0)
                    side_vec.append(0)
                    price_vec.append(price if not np.isnan(price) else 0.0)
                    continue
                qty_vec.append(int(round(abs(delta))))
                if delta > 0:
                    side_vec.append(1)
                elif delta < 0:
                    side_vec.append(-1)
                else:
                    side_vec.append(0)
                price_vec.append(price)
            res = engine.step(price_vec, qty_vec, side_vec, float(pd.Timestamp(dt).value))
            cpp_positions = np.array(res["positions"], dtype=float)
            cash = float(res["cash"])
            latencies.append(res["avg_latency_ns"])
            rejections += int(res["rejected"])
            port_value = cash + sum(cpp_positions[index_lookup[t]] * prices.at[dt, t] for t in tickers)
            portfolio_values.append((dt, port_value))
        else:
            trades = {t: target_shares[t] - positions[t] for t in signals.columns}
            day_turnover_notional = 0.0
            for t, qty in trades.items():
                if qty == 0 or np.isnan(qty):
                    continue
                price = prices.at[dt, t]
                if np.isnan(price):
                    skipped_prices.append((dt, t))
                    continue
                if qty > 0:
                    exec_price = price * (1 + SLIPPAGE)
                    notional = qty * exec_price
                    fee = abs(notional) * TRANSACTION_COST
                    cash -= notional + fee
                else:
                    exec_price = price * (1 - SLIPPAGE)
                    notional = qty * exec_price
                    fee = abs(notional) * TRANSACTION_COST
                    cash -= notional + fee  # notional negative, so subtract adds cash minus fee #
                day_turnover_notional += abs(notional)
                positions[t] += qty

            # Prevent negative cash: if cash < 0, scale back positions proportionally and recompute cash #
            if cash < 0:
                # Scale down all positions to fit available equity, leave cash at zero #
                portfolio_equity = cash + sum(positions[t] * prices.at[dt, t] for t in positions)
                if portfolio_equity <= 0:
                    raise RuntimeError(f"Portfolio insolvent on {dt.date()}")
                scale = portfolio_equity / (portfolio_equity - cash)
                for t in positions:
                    positions[t] *= scale
                cash = 0.0

            # Portfolio valuation #
            port_value = cash + sum(positions[t] * prices.at[dt, t] for t in positions)
            portfolio_values.append((dt, port_value))
            turnover = 0.0 if port_value == 0 else day_turnover_notional / port_value
            turnover_records.append((dt, turnover))

    equity = pd.Series(
        {dt: val for dt, val in portfolio_values},
        name="portfolio_value",
    )
    returns = equity.pct_change().fillna(0.0)

    if use_cpp:
        turnover = pd.Series(np.nan, index=equity.index, name="daily_turnover")
        results = pd.DataFrame({"portfolio_value": equity, "daily_return": returns, "daily_turnover": turnover})
        if latencies:
            results.attrs["latency_ns_avg"] = float(np.mean(latencies))
            results.attrs["latency_ns_p95"] = float(np.percentile(latencies, 95))
            results.attrs["rejections"] = rejections
    else:
        turnover = pd.Series({dt: t for dt, t in turnover_records}, name="daily_turnover")
        results = pd.DataFrame({"portfolio_value": equity, "daily_return": returns, "daily_turnover": turnover})
        if skipped_prices:
            unique = {(dt.date(), t) for dt, t in skipped_prices}
            print(f"[WARN] Skipped {len(unique)} trades due to missing prices (date, ticker) samples: {list(unique)[:5]}")

    return results


# Pretty print a summary table to console #
def print_backtest_summary(results: pd.DataFrame, risk_free_rate: float = 0.0) -> None:
    final_value = results["portfolio_value"].iloc[-1]
    daily_returns = results["daily_return"]
    sharpe = sharpe_ratio(daily_returns, risk_free_rate=risk_free_rate)
    mdd = max_drawdown(results["portfolio_value"])
    annual_cagr = cagr(results["portfolio_value"])
    hit = hit_rate(daily_returns)
    avg_turnover = results.get("daily_turnover", pd.Series(dtype=float)).mean()

    summary = pd.DataFrame(
        {
            "final_value": [final_value],
            "sharpe": [sharpe],
            "max_drawdown": [mdd],
            "avg_return": [daily_returns.mean()],
            "volatility": [daily_returns.std()],
            "cagr": [annual_cagr],
            "hit_rate": [hit],
            "turnover": [avg_turnover],
        }
    ).round(6)
    print("=== BACKTEST SUMMARY ===")
    if tabulate:
        print(tabulate(summary, headers="keys", tablefmt="github", showindex=False))
    else:
        print(summary.to_string(index=False))


def write_summary_row(path: Path, row: dict) -> None:
    path.parent.mkdir(exist_ok=True)
    header = list(row.keys())
    exists = path.exists()
    with path.open("a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        if not exists:
            writer.writeheader()
        writer.writerow(row)


if __name__ == "__main__":
    from data import load_data
    from strategies import momentum_strategy

    tickers = ["AAPL", "MSFT", "AMZN", "GOOG", "META", "NVDA", "TSLA", "JPM", "XOM", "JNJ"]
    prices = load_data(tickers, "2020-01-01", "2023-01-01")
    signals = momentum_strategy(prices, window=20)
    results = backtest(signals, prices, risk_free_rate=0.02)
    results_rounded = results.round(6)
    final_value = results["portfolio_value"].iloc[-1]
    results_path = RESULTS_DIR / "momentum_backtest.csv"
    results_rounded.to_csv(results_path, index=True)

    print_backtest_summary(results, risk_free_rate=0.02)
    if "latency_ns_avg" in results.attrs:
        print(
            f"Latency ns avg={results.attrs['latency_ns_avg']:.0f}, "
            f"p95={results.attrs['latency_ns_p95']:.0f}, "
            f"rejected={results.attrs.get('rejections', 0)}"
        )
    # persist summary to CSV
    summary_path = RESULTS_DIR / "summary_runs.csv"
    summary_row = {
        "run_name": "momentum_example_cpp" if exec_core else "momentum_example_py",
        "description": "Momentum example run",
        "final_value": final_value,
        "sharpe": sharpe_ratio(results["daily_return"], risk_free_rate=0.02),
        "max_drawdown": max_drawdown(results["portfolio_value"]),
        "avg_return": results["daily_return"].mean(),
        "volatility": results["daily_return"].std(),
        "cagr": cagr(results["portfolio_value"]),
        "hit_rate": hit_rate(results["daily_return"]),
        "turnover": results.get("daily_turnover", pd.Series(dtype=float)).mean(),
        "latency_ns_avg": results.attrs.get("latency_ns_avg"),
        "latency_ns_p95": results.attrs.get("latency_ns_p95"),
        "rejections": results.attrs.get("rejections"),
    }
    write_summary_row(summary_path, summary_row)

    print("\n=== BACKTEST TAIL ===")
    tail = results_rounded.tail()
    if tabulate:
        print(tabulate(tail, headers="keys", tablefmt="github"))
    else:
        print(tail.to_string())
    print(f"\nSaved results to {results_path}")

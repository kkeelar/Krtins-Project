# Convert trading signals into simulated portfolio performance #
from __future__ import annotations

from typing import Dict

from pathlib import Path

import numpy as np
import pandas as pd
try:
    from tabulate import tabulate
except ImportError:
    tabulate = None

TRANSACTION_COST = 0.001  # 0.1% per trade #
SLIPPAGE = 0.0005  # 0.05% price penalty #
STARTING_CASH = 100_000.0

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

from metrics import max_drawdown, sharpe_ratio


# Run a simple backtest with equal-weight position sizing #
def backtest(
    signals: pd.DataFrame,
    data: Dict[str, pd.DataFrame],
    use_vol_targeting: bool = False,
    vol_window: int = 20,
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

    cash = STARTING_CASH
    positions = {t: 0.0 for t in signals.columns}  # shares #
    portfolio_values = []

    prev_values = None

    for dt, row in signals.iterrows():
        # Identify active signals #
        active = row[row != 0]
        if active.empty:
            target_shares = {t: 0.0 for t in signals.columns}
        else:
            total_value = cash + sum(positions[t] * prices.at[dt, t] for t in positions)

            if use_vol_targeting:
                day_vol = vol.loc[dt]
                inv_vol = 1 / day_vol.replace(0, np.nan).clip(lower=eps)
                raw = active * inv_vol
                denom = raw.abs().sum()
                if denom == 0 or np.isnan(denom):
                    weights = active / active.abs().sum()
                else:
                    weights = raw / denom
            else:
                weights = active / active.abs().sum()

            alloc_per_dollar = weights * total_value
            target_shares = {
                t: alloc_per_dollar.get(t, 0.0) / prices.at[dt, t] for t in signals.columns
            }

        # Generate trades #
        trades = {t: target_shares[t] - positions[t] for t in signals.columns}

        # Execute trades with slippage and costs #
        for t, qty in trades.items():
            if qty == 0 or np.isnan(qty):
                continue
            price = prices.at[dt, t]
            if np.isnan(price):
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
            positions[t] += qty

        # Portfolio valuation #
        port_value = cash + sum(positions[t] * prices.at[dt, t] for t in positions)
        portfolio_values.append((dt, port_value))
        prev_values = port_value

    equity = pd.Series(
        {dt: val for dt, val in portfolio_values},
        name="portfolio_value",
    )
    returns = equity.pct_change().fillna(0.0)
    results = pd.DataFrame({"portfolio_value": equity, "daily_return": returns})
    return results


# Pretty print a summary table to console #
def print_backtest_summary(results: pd.DataFrame) -> None:
    final_value = results["portfolio_value"].iloc[-1]
    daily_returns = results["daily_return"]
    sharpe = sharpe_ratio(daily_returns)
    mdd = max_drawdown(results["portfolio_value"])

    summary = pd.DataFrame(
        {
            "final_value": [final_value],
            "sharpe": [sharpe],
            "max_drawdown": [mdd],
            "avg_return": [daily_returns.mean()],
            "volatility": [daily_returns.std()],
        }
    ).round(6)
    print("=== BACKTEST SUMMARY ===")
    if tabulate:
        print(tabulate(summary, headers="keys", tablefmt="github", showindex=False))
    else:
        print(summary.to_string(index=False))


if __name__ == "__main__":
    from data import load_data
    from strategies import momentum_strategy

    tickers = ["AAPL", "MSFT", "AMZN", "GOOG", "META", "NVDA", "TSLA", "JPM", "XOM", "JNJ"]
    prices = load_data(tickers, "2020-01-01", "2023-01-01")
    signals = momentum_strategy(prices, window=20)
    results = backtest(signals, prices)
    results_rounded = results.round(6)
    results_path = RESULTS_DIR / "momentum_backtest.csv"
    results_rounded.to_csv(results_path, index=True)

    print_backtest_summary(results)
    print("\n=== BACKTEST TAIL ===")
    tail = results_rounded.tail()
    if tabulate:
        print(tabulate(tail, headers="keys", tablefmt="github"))
    else:
        print(tail.to_string())
    print(f"\nSaved results to {results_path}")

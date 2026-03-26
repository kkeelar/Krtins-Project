# Parameter sweep across multiple strategies #
from __future__ import annotations

from typing import Dict, List
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd
try:
    from tabulate import tabulate
except ImportError:
    tabulate = None

from backtest import backtest, print_backtest_summary
from metrics import sharpe_ratio
from strategies import (
    long_only_momentum,
    mean_reversion_strategy,
    momentum_strategy,
    breakout_strategy,
    vol_scaled_momentum,
)

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


# Backward-compatible momentum sweep #
def run_parameter_sweep(data: Dict[str, pd.DataFrame], windows: List[int]) -> pd.DataFrame:
    return run_strategy_comparison(
        data=data,
        strategy_configs=[
            {
                "name": "momentum",
                "generator": lambda d, params: momentum_strategy(d, params["window"]),
                "params": [{"window": w} for w in windows],
            }
        ],
    )


# General strategy comparison across parameter grids #
def run_strategy_comparison(
    data: Dict[str, pd.DataFrame], strategy_configs: List[Dict]
) -> pd.DataFrame:
    rows = []
    for config in strategy_configs:
        name = config["name"]
        generator = config["generator"]
        use_vol_targeting = config.get("use_vol_targeting", False)
        vol_window = config.get("vol_window", 20)
        for params in config["params"]:
            signals = generator(data, params)
            bt = backtest(
                signals,
                data,
                use_vol_targeting=use_vol_targeting,
                vol_window=vol_window,
            )
            final_value = bt["portfolio_value"].iloc[-1]
            avg_ret = bt["daily_return"].mean()
            vol = bt["daily_return"].std()
            sharpe = sharpe_ratio(bt["daily_return"])
            rows.append(
                {
                    "strategy_name": name,
                    "parameters": params,
                    "final_value": final_value,
                    "avg_return": avg_ret,
                    "volatility": vol,
                    "sharpe": sharpe,
                }
            )

    df = pd.DataFrame(rows)
    df = df.sort_values("sharpe", ascending=False)
    return df


def format_parameters(param_dict: Dict) -> str:
    return ", ".join(f"{k}={v}" for k, v in param_dict.items())


def print_top_results(df: pd.DataFrame, top_n: int = 10) -> None:
    display_df = df.copy()
    display_df["parameters"] = display_df["parameters"].apply(format_parameters)
    display_df = display_df.round(6)
    print("=== PARAMETER SWEEP RESULTS ===")
    top = display_df.head(top_n)
    if tabulate:
        print(tabulate(top, headers="keys", tablefmt="github", showindex=False))
    else:
        print(top.to_string(index=False))
    best = display_df.iloc[0]
    print(
        f"\nBest strategy: {best['strategy_name']} ({best['parameters']}), "
        f"Sharpe={best['sharpe']:.4f}, Final Value={best['final_value']:.2f}"
    )


if __name__ == "__main__":
    from data import load_data

    tickers = ["AAPL", "MSFT", "AMZN", "GOOG", "META", "NVDA", "TSLA", "JPM", "XOM", "JNJ"]
    prices = load_data(tickers, "2020-01-01", "2023-01-01")

    momentum_windows = [5, 10, 20, 50, 100]
    mr_windows = [5, 10, 20]
    mr_thresholds = [1, 2]
    lom_windows = [10, 20, 50]
    breakout_windows = [20, 50, 100]
    vsm_windows = [10, 20, 50]
    vsm_vol_windows = [10, 20]

    configs = [
        {
            "name": "momentum",
            "generator": lambda d, params: momentum_strategy(d, params["window"]),
            "params": [{"window": w} for w in momentum_windows],
        },
        {
            "name": "momentum_vol_targeted",
            "generator": lambda d, params: momentum_strategy(d, params["window"]),
            "params": [{"window": w} for w in momentum_windows],
            "use_vol_targeting": True,
            "vol_window": 20,
        },
        {
            "name": "long_only_momentum",
            "generator": lambda d, params: long_only_momentum(d, params["window"]),
            "params": [{"window": w} for w in lom_windows],
        },
        {
            "name": "mean_reversion",
            "generator": lambda d, params: mean_reversion_strategy(
                d, params["window"], params["z_threshold"]
            ),
            "params": [{"window": w, "z_threshold": z} for w, z in product(mr_windows, mr_thresholds)],
        },
        {
            "name": "breakout",
            "generator": lambda d, params: breakout_strategy(d, params["window"]),
            "params": [{"window": w} for w in breakout_windows],
        },
        {
            "name": "vol_scaled_momentum",
            "generator": lambda d, params: vol_scaled_momentum(
                d, params["window"], params["vol_window"]
            ),
            "params": [
                {"window": w, "vol_window": vw} for w, vw in product(vsm_windows, vsm_vol_windows)
            ],
        },
    ]

    summary = run_strategy_comparison(prices, configs)
    summary["parameters"] = summary["parameters"].apply(lambda p: dict(p))
    summary_rounded = summary.round(6)

    # Save results #
    summary_path = RESULTS_DIR / "strategy_comparison.csv"
    summary_rounded.to_csv(summary_path, index=False)
    parameter_sweep_path = RESULTS_DIR / "parameter_sweep.csv"
    summary_rounded.to_csv(parameter_sweep_path, index=False)

    print_top_results(summary)
    print(f"\nSaved results to {summary_path}")

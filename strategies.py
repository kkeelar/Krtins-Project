# Momentum strategy that ranks assets by recent returns and outputs position signals #
from __future__ import annotations

from typing import Dict

import pandas as pd
import numpy as np


# Generate momentum signals based on rolling returns #
def momentum_strategy(data: Dict[str, pd.DataFrame], window: int) -> pd.DataFrame:
    if window <= 0:
        raise ValueError("window must be positive")
    if not data:
        raise ValueError("data cannot be empty")

    # Build returns DataFrame aligned by date #
    returns = {}
    for ticker, df in data.items():
        if "Close" not in df.columns:
            raise ValueError(f"Close column missing for {ticker}")
        # Simple window return: price_t / price_{t-window} - 1 #
        ret = df["Close"] / df["Close"].shift(window) - 1
        returns[ticker] = ret

    returns_df = pd.concat(returns, axis=1)
    returns_df.columns.name = None

    # Rank assets each day and assign signals #
    ranks = returns_df.rank(axis=1, method="first", pct=True)
    signals = pd.DataFrame(index=returns_df.index, columns=returns_df.columns, dtype=int)

    top_cutoff = 0.70  # top 30% #
    bottom_cutoff = 0.30  # bottom 30% #

    signals[ranks >= top_cutoff] = 1
    signals[ranks <= bottom_cutoff] = -1
    signals[(ranks < top_cutoff) & (ranks > bottom_cutoff)] = 0

    # Shift forward one day to avoid lookahead #
    signals = signals.shift(1)

    # Drop rows where signals are all NaN (pre-window) #
    signals = signals.dropna(how="all")

    return signals


# Mean reversion signals using rolling return z-scores #
def mean_reversion_strategy(
    data: Dict[str, pd.DataFrame], window: int, z_threshold: float
) -> pd.DataFrame:
    if window <= 1:
        raise ValueError("window must be greater than 1")
    if z_threshold <= 0:
        raise ValueError("z_threshold must be positive")
    if not data:
        raise ValueError("data cannot be empty")

    signals = {}
    for ticker, df in data.items():
        if "Close" not in df.columns:
            raise ValueError(f"Close column missing for {ticker}")
        rets = df["Close"].pct_change()
        mean = rets.rolling(window).mean()
        std = rets.rolling(window).std()
        z = (rets - mean) / std

        sig = pd.Series(0, index=rets.index)
        sig[z > z_threshold] = -1  # short when rich #
        sig[z < -z_threshold] = 1  # long when cheap #
        signals[ticker] = sig

    signals_df = pd.DataFrame(signals)
    signals_df = signals_df.shift(1)
    signals_df = signals_df.dropna(how="all")
    return signals_df


# Long-only momentum: long top 30% by return, flat otherwise #
def long_only_momentum(data: Dict[str, pd.DataFrame], window: int) -> pd.DataFrame:
    if window <= 0:
        raise ValueError("window must be positive")
    if not data:
        raise ValueError("data cannot be empty")

    returns = {}
    for ticker, df in data.items():
        if "Close" not in df.columns:
            raise ValueError(f"Close column missing for {ticker}")
        ret = df["Close"] / df["Close"].shift(window) - 1
        returns[ticker] = ret

    returns_df = pd.concat(returns, axis=1)
    returns_df.columns.name = None

    ranks = returns_df.rank(axis=1, method="first", pct=True)
    signals = pd.DataFrame(0, index=returns_df.index, columns=returns_df.columns, dtype=int)
    top_cutoff = 0.70  # top 30% #
    signals[ranks >= top_cutoff] = 1
    signals = signals.shift(1)
    signals = signals.dropna(how="all")
    return signals


# Breakout strategy using Donchian channels #
def breakout_strategy(data: Dict[str, pd.DataFrame], window: int) -> pd.DataFrame:
    if window <= 1:
        raise ValueError("window must be greater than 1")
    if not data:
        raise ValueError("data cannot be empty")

    signals = {}
    for ticker, df in data.items():
        if not {"High", "Low", "Close"}.issubset(df.columns):
            raise ValueError(f"High/Low/Close columns missing for {ticker}")
        rolling_max = df["High"].rolling(window).max().shift(1)
        rolling_min = df["Low"].rolling(window).min().shift(1)
        sig = pd.Series(0, index=df.index)
        sig[df["Close"] > rolling_max] = 1
        sig[df["Close"] < rolling_min] = -1
        signals[ticker] = sig

    signals_df = pd.DataFrame(signals)
    signals_df = signals_df.shift(1)
    signals_df = signals_df.dropna(how="all")
    return signals_df


# Volatility-scaled momentum to reward high return per unit risk #
def vol_scaled_momentum(
    data: Dict[str, pd.DataFrame], window: int, vol_window: int
) -> pd.DataFrame:
    if window <= 0 or vol_window <= 0:
        raise ValueError("window and vol_window must be positive")
    if not data:
        raise ValueError("data cannot be empty")

    eps = 1e-8
    scores = {}
    for ticker, df in data.items():
        if "Close" not in df.columns:
            raise ValueError(f"Close column missing for {ticker}")
        momentum_ret = df["Close"] / df["Close"].shift(window) - 1
        vol = df["Close"].pct_change().rolling(vol_window).std().clip(lower=eps)
        score = momentum_ret / vol
        scores[ticker] = score

    score_df = pd.DataFrame(scores)
    score_df.columns.name = None

    ranks = score_df.rank(axis=1, method="first", pct=True)
    signals = pd.DataFrame(index=score_df.index, columns=score_df.columns, dtype=int)

    top_cutoff = 0.70  # top 30% #
    bottom_cutoff = 0.30  # bottom 30% #

    signals[ranks >= top_cutoff] = 1
    signals[ranks <= bottom_cutoff] = -1
    signals[(ranks < top_cutoff) & (ranks > bottom_cutoff)] = 0

    signals = signals.shift(1)
    signals = signals.dropna(how="all")
    return signals


if __name__ == "__main__":
    from data import load_data

    tickers = ["AAPL", "MSFT", "AMZN", "GOOG", "META", "NVDA", "TSLA", "JPM", "XOM", "JNJ"]
    prices = load_data(tickers, "2020-01-01", "2023-01-01")
    mom_signals = momentum_strategy(prices, window=20)
    print("Momentum sample:")
    print(mom_signals.head())

    mr_signals = mean_reversion_strategy(prices, window=20, z_threshold=1.5)
    print("\nMean reversion sample:")
    print(mr_signals.head())

    bo_signals = breakout_strategy(prices, window=50)
    print("\nBreakout sample:")
    print(bo_signals.head())

    vsm_signals = vol_scaled_momentum(prices, window=20, vol_window=10)
    print("\nVol-scaled momentum sample:")
    print(vsm_signals.head())

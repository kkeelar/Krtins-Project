# Continuous score-based strategies #
from __future__ import annotations

from typing import Dict, List

import pandas as pd
import numpy as np


# Utilities #
def _row_zscore(df: pd.DataFrame, eps: float = 1e-8) -> pd.DataFrame:
    mean = df.mean(axis=1)
    std = df.std(axis=1).replace(0, np.nan)
    z = (df.sub(mean, axis=0)).div(std + eps, axis=0)
    return z


# Generate momentum scores based on rolling returns #
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
        ret = df["Close"] / df["Close"].shift(window) - 1
        returns[ticker] = ret

    returns_df = pd.concat(returns, axis=1)
    returns_df.columns.name = None
    scores = returns_df
    scores = scores.shift(1)  # avoid lookahead
    scores = scores.dropna(how="all")
    return scores


# Mean reversion scores using rolling return z-scores #
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
        signals[ticker] = z

    signals_df = pd.DataFrame(signals)
    signals_df = signals_df.shift(1)  # avoid lookahead
    signals_df = signals_df.dropna(how="all")
    return signals_df


# Long-only momentum: keep positive momentum scores, zero negatives #
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

    scores = returns_df.clip(lower=0)  # only positive momentum contributes
    scores = scores.shift(1)
    scores = scores.dropna(how="all")
    return scores


# Breakout strategy using Donchian channels -> score = distance from channel mid, normalized by range #
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
        mid = (rolling_max + rolling_min) / 2
        rng = (rolling_max - rolling_min).replace(0, np.nan)
        score = (df["Close"] - mid) / rng
        signals[ticker] = score

    signals_df = pd.DataFrame(signals)
    signals_df = signals_df.shift(1)  # avoid lookahead
    signals_df = signals_df.dropna(how="all")
    return signals_df


# Volatility-scaled momentum score: momentum / volatility #
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

    score_df = score_df.shift(1)
    score_df = score_df.dropna(how="all")
    return score_df


# Normalization helper: cross-sectional zscore #
def normalize_scores(scores: pd.DataFrame) -> pd.DataFrame:
    return _row_zscore(scores)


# Combined multi-factor strategy (momentum short/long horizons, mean reversion, vol-scaled) #
def combined_factor_strategy(
    data: Dict[str, pd.DataFrame],
    mom_short: int = 10,
    mom_long: int = 50,
    mr_window: int = 10,
    mr_z: float = 1.0,
    vol_mom_window: int = 20,
    vol_vol_window: int = 10,
    weights: Dict[str, float] | None = None,
) -> pd.DataFrame:
    if weights is None:
        weights = {"mom_short": 1.0, "mom_long": 1.0, "mean_rev": 1.0, "vol_scaled": 1.0}

    s_mom_s = momentum_strategy(data, mom_short)
    s_mom_l = momentum_strategy(data, mom_long)
    s_mr = mean_reversion_strategy(data, mr_window, mr_z)
    s_vol = vol_scaled_momentum(data, vol_mom_window, vol_vol_window)

    comps = {
        "mom_short": normalize_scores(s_mom_s),
        "mom_long": normalize_scores(s_mom_l),
        "mean_rev": normalize_scores(s_mr),
        "vol_scaled": normalize_scores(s_vol),
    }

    # align indices/columns
    idx = comps["mom_short"].index.intersection(comps["mom_long"].index)
    for v in comps.values():
        idx = idx.intersection(v.index)
    cols = comps["mom_short"].columns
    for v in comps.values():
        cols = cols.intersection(v.columns)

    combined = pd.DataFrame(0.0, index=idx, columns=cols)
    total_w = sum(weights.values())
    for name, w in weights.items():
        combined += (w / total_w) * comps[name].reindex(idx, columns=cols)
    return combined


# Dynamic strategy weighting based on rolling Sharpe (no lookahead) #
def dynamic_weighted_strategy(
    score_map: Dict[str, pd.DataFrame],
    prices: Dict[str, pd.DataFrame],
    sharpe_lookback: int = 60,
    min_periods: int = 20,
    temperature: float = 1.0,
) -> pd.DataFrame:
    """score_map: name -> score DF (aligned, shifted already)
    prices: ticker -> df with Close
    Returns final combined scores per asset per day with weights driven by past Sharpe."""
    # align scores
    common_idx = None
    common_cols = None
    for df in score_map.values():
        common_idx = df.index if common_idx is None else common_idx.intersection(df.index)
        common_cols = df.columns if common_cols is None else common_cols.intersection(df.columns)
    scores_aligned = {k: v.reindex(common_idx, columns=common_cols) for k, v in score_map.items()}

    # asset returns
    close_panel = pd.concat({t: df["Close"] for t, df in prices.items()}, axis=1)
    asset_rets = close_panel.pct_change().reindex(common_idx)

    # compute per-strategy daily pnl using previous-day normalized weights
    strategy_returns = {}
    for name, s in scores_aligned.items():
        w = s.shift(1)
        denom = w.abs().sum(axis=1).replace(0, np.nan)
        w_norm = w.div(denom, axis=0).fillna(0)
        pnl = (w_norm * asset_rets).sum(axis=1)
        strategy_returns[name] = pnl
    strat_ret_df = pd.DataFrame(strategy_returns)

    # rolling Sharpe up to t-1
    roll_mean = strat_ret_df.rolling(sharpe_lookback, min_periods=min_periods).mean().shift(1)
    roll_std = strat_ret_df.rolling(sharpe_lookback, min_periods=min_periods).std().shift(1)
    sharpe = roll_mean / (roll_std.replace(0, np.nan))

    # convert Sharpe to weights (softmax over positive values)
    sharpe_pos = sharpe.clip(lower=0)
    expw = np.exp(sharpe_pos / max(temperature, 1e-6))
    weight_per_day = expw.div(expw.sum(axis=1), axis=0).fillna(0)

    # combine scores per day
    combined_scores = pd.DataFrame(0.0, index=common_idx, columns=common_cols)
    for name, s in scores_aligned.items():
        combined_scores += s.mul(weight_per_day[name], axis=0)

    combined_scores = combined_scores.dropna(how="all")
    return combined_scores


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

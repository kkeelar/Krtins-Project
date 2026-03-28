# Common performance metrics #
from __future__ import annotations

import numpy as np
import pandas as pd


# Compute daily Sharpe ratio with sqrt(252) annualization #
def sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.0) -> float:
    """
    returns: daily returns series
    risk_free_rate: annual risk-free rate (e.g., 0.02 for 2%)
    """
    excess = returns - risk_free_rate / 252
    vol = excess.std()
    if vol == 0 or np.isnan(vol):
        return np.nan
    return excess.mean() / vol * np.sqrt(252)


def cagr(equity: pd.Series) -> float:
    if equity.empty:
        return np.nan
    start, end = equity.iloc[0], equity.iloc[-1]
    if start <= 0:
        return np.nan
    days = len(equity)
    years = days / 252
    if years == 0:
        return np.nan
    return (end / start) ** (1 / years) - 1


def hit_rate(returns: pd.Series) -> float:
    if returns.empty:
        return np.nan
    positives = (returns > 0).sum()
    return positives / len(returns)


# Compute maximum drawdown from an equity curve #
def max_drawdown(equity: pd.Series) -> float:
    rolling_max = equity.cummax()
    drawdown = equity / rolling_max - 1.0
    return drawdown.min()

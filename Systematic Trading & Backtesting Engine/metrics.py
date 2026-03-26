# Common performance metrics #
from __future__ import annotations

import numpy as np
import pandas as pd


# Compute daily Sharpe ratio with sqrt(252) annualization #
def sharpe_ratio(returns: pd.Series) -> float:
    vol = returns.std()
    if vol == 0 or np.isnan(vol):
        return np.nan
    return returns.mean() / vol * np.sqrt(252)


# Compute maximum drawdown from an equity curve #
def max_drawdown(equity: pd.Series) -> float:
    rolling_max = equity.cummax()
    drawdown = equity / rolling_max - 1.0
    return drawdown.min()

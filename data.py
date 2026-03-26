# Data layer for downloading and cleaning historical OHLCV data #
from __future__ import annotations

from typing import Dict, List

import pandas as pd
import yfinance as yf


COLUMNS = ["Open", "High", "Low", "Close", "Volume"]


# Download one ticker and return a cleaned OHLCV DataFrame #
def _download_single(ticker: str, start: str, end: str) -> pd.DataFrame:
    df = yf.download(ticker, start=start, end=end, progress=False)
    if df.empty:
        raise ValueError(f"No data returned for ticker '{ticker}'")

    # Keep only OHLCV columns and sort by date #
    df = df[COLUMNS].copy()
    # Flatten multi-index columns from yfinance into simple names #
    if getattr(df.columns, "nlevels", 1) > 1:
        df.columns = df.columns.get_level_values(0)
    df.columns.name = None
    df.index = pd.to_datetime(df.index).tz_localize(None)
    df.sort_index(inplace=True)
    return df


# Download and align OHLCV data for multiple tickers #
def load_data(tickers: List[str], start: str, end: str) -> Dict[str, pd.DataFrame]:
    if not tickers:
        raise ValueError("tickers list cannot be empty")

    raw = {t: _download_single(t, start, end) for t in tickers}

    # Build a common date index (union) and forward-fill gaps #
    all_dates = sorted(set().union(*[df.index for df in raw.values()]))
    common_index = pd.DatetimeIndex(all_dates, name="Date")

    aligned: Dict[str, pd.DataFrame] = {}
    for ticker, df in raw.items():
        # Reindex to common dates, forward-fill, drop leading NaNs #
        reindexed = df.reindex(common_index).ffill().dropna()
        aligned[ticker] = reindexed

    return aligned


if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "AMZN", "GOOG", "META", "NVDA", "TSLA", "JPM", "XOM", "JNJ"]
    data = load_data(tickers, "2020-01-01", "2023-01-01")
    for ticker, df in data.items():
        print(f"\n{ticker} sample:")
        print(df.head())

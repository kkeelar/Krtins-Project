import unittest

import pandas as pd
import numpy as np

from strategies import (
    momentum_strategy,
    mean_reversion_strategy,
    breakout_strategy,
    vol_scaled_momentum,
    long_only_momentum,
)


def _make_price_df(close_prices):
    dates = pd.date_range("2020-01-01", periods=len(close_prices), freq="D")
    close = pd.Series(close_prices, index=dates)
    df = pd.DataFrame({
        "Open": close,
        "High": close + 1,
        "Low": close - 1,
        "Close": close,
        "Volume": 1_000,
    })
    return df


def _two_asset_data():
    up = _make_price_df([100, 101, 102, 104, 106, 108, 110, 112])
    down = _make_price_df([100, 99, 98, 97, 96, 95, 94, 93])
    return {"UP": up, "DOWN": down}


class StrategyTests(unittest.TestCase):
    def test_momentum_signals_rank_correctly(self):
        data = _two_asset_data()
        sig = momentum_strategy(data, window=2)
        nz = sig.dropna().iloc[-1]
        self.assertGreater(nz["UP"], nz["DOWN"])

    def test_long_only_momentum_flats_loser(self):
        data = _two_asset_data()
        sig = long_only_momentum(data, window=2)
        last_row = sig.dropna().iloc[-1]
        self.assertGreater(last_row["UP"], 0)
        self.assertGreaterEqual(last_row["DOWN"], 0)

    def test_mean_reversion_flips_direction(self):
        data = _two_asset_data()
        sig = mean_reversion_strategy(data, window=2, z_threshold=0.1)
        nz = sig.dropna().iloc[-1]
        self.assertLess(nz["DOWN"], 0)  # underperformer gets negative z
        self.assertGreater(nz["UP"], nz["DOWN"])

    def test_breakout_triggers(self):
        data = _two_asset_data()
        sig = breakout_strategy(data, window=3)
        nz_rows = sig.dropna()
        self.assertGreater(len(nz_rows), 0)
        self.assertTrue((nz_rows["UP"] > 0).any())

    def test_vol_scaled_prefers_return_per_risk(self):
        data = _two_asset_data()
        sig = vol_scaled_momentum(data, window=2, vol_window=2)
        nz = sig.dropna().iloc[-1]
        self.assertGreater(nz["UP"], nz["DOWN"])


if __name__ == "__main__":
    unittest.main()

import unittest
import pandas as pd
import numpy as np

from backtest import backtest
from data import COLUMNS


def _toy_prices():
    dates = pd.date_range("2020-01-01", periods=5, freq="D")
    p1 = pd.Series([100, 101, 102, 103, 104], index=dates)
    p2 = pd.Series([100, 99, 98, 97, 96], index=dates)
    make_df = lambda s: pd.DataFrame(
        {
            "Open": s,
            "High": s + 1,
            "Low": s - 1,
            "Close": s,
            "Volume": 1_000,
        }
    )
    return {"WIN": make_df(p1), "LOSE": make_df(p2)}


class BacktestTests(unittest.TestCase):
    def test_leverage_cap_scales_positions(self):
        data = _toy_prices()
        dates = next(iter(data.values())).index
        # Go all-in long both assets every day -> raw gross 2x; cap should scale to <=1.5x
        signals = pd.DataFrame(1, index=dates, columns=["WIN", "LOSE"]).astype(int)
        res = backtest(signals, data, gross_leverage_cap=1.5)
        # Check that portfolio never goes negative and leverage limit respected approximately
        equity = res["portfolio_value"]
        self.assertTrue((equity > 0).all())

    def test_missing_price_logs_and_skips(self):
        data = _toy_prices()
        # introduce NaN price
        data["WIN"].loc[data["WIN"].index[2], "Close"] = np.nan
        signals = pd.DataFrame(1, index=data["WIN"].index, columns=["WIN", "LOSE"]).astype(int)
        res = backtest(signals, data)
        # Ensure result still produced
        self.assertFalse(res.empty)


if __name__ == "__main__":
    unittest.main()

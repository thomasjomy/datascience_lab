import pandas as pd
import numpy as np


rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
ts = pd.Series(np.random.randn(len(rng)), rng)
ts_utc = ts.tz_localize("UTC")
ts_us_east = ts_utc.tz_convert("US/Eastern")

print(ts)
print(ts_utc)
print(ts_us_east)
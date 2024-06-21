import pandas as pd
import numpy as np


date_range1 = pd.date_range("1/1/2012", periods=100, freq="s")
ts = pd.Series(np.random.randint(0, 500, len(date_range1)), index=date_range1)
ts.resample("5Min").sum();

print(ts)
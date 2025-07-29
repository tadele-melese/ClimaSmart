
import pandas as pd

def compute_vci(ndvi_series):
    ndvi_rolling_max = ndvi_series.rolling(window=12, min_periods=1).max()
    ndvi_rolling_min = ndvi_series.rolling(window=12, min_periods=1).min()

    vci = 100 * (ndvi_series - ndvi_rolling_min) / (ndvi_rolling_max - ndvi_rolling_min)
    vci = vci.clip(0, 100)
    return vci


import pandas as pd
import numpy as np

def fetch_chirps(start='2000-01', end='2024-12', region='ethiopia'):
    dates = pd.date_range(start=start, end=end, freq='M')
    np.random.seed(42)
    rainfall = np.random.gamma(2.0, 1.5, len(dates))  # simulate rain
    return pd.Series(rainfall, index=dates, name='precip')

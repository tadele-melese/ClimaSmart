import xarray as xr
import numpy as np
from pymannkendall import original_test
import matplotlib.pyplot as plt

def mann_kendall_test_ts(ts):
    try:
        result = original_test(ts)
        return result.trend == 'increasing', result.p, result.slope
    except:
        return np.nan, np.nan, np.nan

def plot_trend_map(data: xr.DataArray, title="Mann-Kendall Trend Map"):
    """
    Compute and plot Mann-Kendall trend map for gridded time series data.
    """
    increasing = np.full(data.shape[1:], np.nan)
    slope = np.full_like(increasing, np.nan)
    
    for i in range(data.shape[1]):
        for j in range(data.shape[2]):
            ts = data[:, i, j].values
            _, _, slope_val = mann_kendall_test_ts(ts)
            slope[i, j] = slope_val

    plt.imshow(slope, cmap='coolwarm')
    plt.colorbar(label='Trend Slope')
    plt.title(title)
    plt.show()

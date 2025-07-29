# climate/climate_trend.py
import pandas as pd
import numpy as np
from scipy.stats import linregress


def compute_trend(series: pd.Series, method: str = "linear") -> dict:
    """
    Compute trend using linear regression or Mann-Kendall test.

    Parameters:
        series (pd.Series): Time series.
        method (str): 'linear' or 'mann-kendall'.

    Returns:
        dict: slope, p-value, and trend direction.
    """
    result = {}
    if method == "linear":
        x = np.arange(len(series))
        slope, intercept, r_value, p_value, std_err = linregress(x, series.values)
        result = {"slope": slope, "p_value": p_value, "trend": "increasing" if slope > 0 else "decreasing"}
    else:
        from pymannkendall import original_test
        mk_result = original_test(series.values)
        result = {"slope": mk_result.slope, "p_value": mk_result.p, "trend": mk_result.trend}

    return result
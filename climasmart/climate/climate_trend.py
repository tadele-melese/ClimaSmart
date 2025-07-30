import pandas as pd
import numpy as np
from scipy.stats import linregress
from pymannkendall import original_test


def compute_trend(series: pd.Series, method: str = "linear") -> dict:
    if method == "linear":
        x = np.arange(len(series))
        slope, intercept, r_value, p_value, std_err = linregress(x, series.values)
        return {
            "slope": slope,
            "p_value": p_value,
            "trend": "increasing" if slope > 0 else "decreasing"
        }
    elif method == "mann-kendall":
        mk_result = original_test(series.values)
        return {
            "slope": mk_result.slope,
            "p_value": mk_result.p,
            "trend": mk_result.trend
        }
    else:
        raise ValueError(f"Unsupported method: {method}")


def mann_kendall_test(series: pd.Series) -> dict:
    result = original_test(series.values)
    return {
        "slope": result.slope,
        "p_value": result.p,
        "trend": result.trend
    }

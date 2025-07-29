# climate/climate_normal.py
import pandas as pd
from typing import Tuple

def compute_climate_normal(data: pd.DataFrame, period: Tuple[int, int] = (1981, 2010)) -> pd.DataFrame:
    """
    Compute long-term climate normals for each month.

    Parameters:
        data (pd.DataFrame): DataFrame with datetime index and a single column of values.
        period (Tuple[int, int]): Start and end year for baseline normal.

    Returns:
        pd.DataFrame: Monthly means (normals).
    """
    mask = (data.index.year >= period[0]) & (data.index.year <= period[1])
    baseline = data.loc[mask]
    monthly_normals = baseline.groupby(baseline.index.month).mean()
    monthly_normals.index.name = "Month"
    return monthly_normals
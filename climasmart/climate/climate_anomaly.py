# climate/climate_anomaly.py
import pandas as pd

def compute_anomalies(data: pd.DataFrame, normal: pd.DataFrame) -> pd.DataFrame:
    """
    Compute climate anomalies from a monthly normal.

    Parameters:
        data (pd.DataFrame): DataFrame with datetime index.
        normal (pd.DataFrame): Monthly normals with index from 1 to 12.

    Returns:
        pd.DataFrame: Anomalies (value - normal).
    """
    anomalies = data.copy()
    for month in range(1, 13):
        anomalies.loc[anomalies.index.month == month] -= normal.loc[month].values[0]
    return anomalies

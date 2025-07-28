def compute_rainfall_anomaly(rain_series):
    """
    Computes rainfall anomaly from monthly climatology.

    Parameters:
        rain_series (pd.Series): Time-indexed rainfall values

    Returns:
        pd.Series: Anomaly values
    """
    monthly_climatology = rain_series.groupby(rain_series.index.month).mean()
    anomaly = rain_series - rain_series.index.month.map(monthly_climatology)
    return anomaly

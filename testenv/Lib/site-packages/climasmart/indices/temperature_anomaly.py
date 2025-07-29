def compute_temperature_anomaly(temp_series):
    """
    Computes temperature anomaly from monthly climatology.

    Parameters:
        temp_series (pd.Series): Time-indexed temperature values

    Returns:
        pd.Series: Anomaly values
    """
    monthly_climatology = temp_series.groupby(temp_series.index.month).mean()
    anomaly = temp_series - temp_series.index.month.map(monthly_climatology)
    return anomaly

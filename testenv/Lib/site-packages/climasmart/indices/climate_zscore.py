def compute_climate_zscore(series, baseline_mean, baseline_std):
    """
    Compute Z-score anomaly compared to baseline climatology.
    """
    return (series - baseline_mean) / baseline_std

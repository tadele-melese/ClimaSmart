def compute_ndvi_anomaly(ndvi, ndvi_climatology):
    """
    Compute NDVI anomaly against long-term climatology.
    """
    anomaly = ndvi - ndvi_climatology
    return anomaly

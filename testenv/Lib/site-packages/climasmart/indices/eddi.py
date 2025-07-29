import numpy as np

def compute_eddi(precip, pet, scale=1):
    """
    Compute the Evaporative Demand Drought Index (EDDI).
    EDDI = Z-score of (PET - Precipitation)
    """
    edd = pet - precip
    rolling = edd.rolling(window=scale, min_periods=1).sum()
    zscore = (rolling - rolling.mean()) / rolling.std()
    return zscore

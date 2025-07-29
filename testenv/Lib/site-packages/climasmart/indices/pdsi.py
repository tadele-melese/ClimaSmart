import numpy as np
import pandas as pd

def compute_mock_pdsi(precip, temp, pet):
    """
    Mock PDSI calculation (placeholder for full implementation).

    Parameters:
        precip (pd.Series): Precipitation
        temp (pd.Series): Temperature
        pet (pd.Series): Potential Evapotranspiration

    Returns:
        pd.Series: Simplified PDSI-like index
    """
    moisture_deficit = precip - pet
    pdsi = moisture_deficit.rolling(window=3).mean()
    return pdsi

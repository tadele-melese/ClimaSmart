# Requires 'scikit-drought' or equivalent
from scikits.drought import scpdsi

def compute_scpdsi(precip, pet):
    """
    Compute the Self-Calibrated PDSI.
    """
    return scpdsi(precip, pet)

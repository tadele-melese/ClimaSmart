# climate/climate_metrics.py
from sklearn.metrics import mean_squared_error, r2_score 
import numpy as np

def compute_rmse(y_true, y_pred) -> float:
    """
    Compute Root Mean Squared Error (RMSE).
    """
    return np.sqrt(mean_squared_error(y_true, y_pred))

def compute_nse(y_true, y_pred) -> float:
    """
    Compute Nash-Sutcliffe Efficiency.
    """
    numerator = np.sum((y_true - y_pred) ** 2)
    denominator = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (numerator / denominator)


def compute_r2(y_true, y_pred) -> float:
    """
    Compute R-squared.
    """
    return r2_score(y_true, y_pred)
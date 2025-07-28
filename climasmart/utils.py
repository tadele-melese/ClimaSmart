import os
import logging
import numpy as np
import pandas as pd

def setup_logger(name='climasmart', level=logging.INFO):
    """
    Setup and return a logger instance.

    Parameters:
        name (str): Logger name
        level (int): Logging level (e.g. logging.INFO)

    Returns:
        logging.Logger: Configured logger
    """
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger


def ensure_dir(path):
    """
    Create directory if it doesn't exist.

    Parameters:
        path (str): Directory path to create
    """
    if not os.path.exists(path):
        os.makedirs(path)


def safe_divide(numerator, denominator, fill_value=np.nan):
    """
    Safely divide two arrays or numbers, avoiding division by zero.

    Parameters:
        numerator (float or np.ndarray)
        denominator (float or np.ndarray)
        fill_value: value to use where denominator == 0

    Returns:
        np.ndarray or float: Result of division
    """
    numerator = np.array(numerator)
    denominator = np.array(denominator)
    result = np.full_like(numerator, fill_value, dtype=np.float64)
    mask = denominator != 0
    result[mask] = numerator[mask] / denominator[mask]
    return result


def date_range(start, end, freq='D'):
    """
    Generate a pandas DatetimeIndex between two dates.

    Parameters:
        start (str or pd.Timestamp): Start date
        end (str or pd.Timestamp): End date
        freq (str): Frequency string (e.g. 'D', 'M', 'H')

    Returns:
        pd.DatetimeIndex
    """
    return pd.date_range(start=start, end=end, freq=freq)


def series_to_dataframe(series, col_name='value'):
    """
    Convert pandas Series to DataFrame with named column.

    Parameters:
        series (pd.Series)
        col_name (str): Name of the column

    Returns:
        pd.DataFrame
    """
    return series.to_frame(name=col_name)


def rolling_mean(series, window=3):
    """
    Compute rolling mean for a pandas Series.

    Parameters:
        series (pd.Series)
        window (int): Rolling window size

    Returns:
        pd.Series
    """
    return series.rolling(window=window, min_periods=1).mean()

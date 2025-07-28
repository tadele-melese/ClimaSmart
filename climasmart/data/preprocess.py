import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def fill_missing_values(df, method="interpolate"):
    """
    Fill missing values in the DataFrame.

    Parameters:
        df (pd.DataFrame): Input data with missing values
        method (str): 'ffill', 'bfill', or 'interpolate' (default)

    Returns:
        pd.DataFrame: DataFrame with filled missing values
    """
    if method == "ffill":
        return df.fillna(method="ffill")
    elif method == "bfill":
        return df.fillna(method="bfill")
    elif method == "interpolate":
        return df.interpolate(method="time")
    else:
        raise ValueError("Invalid method. Choose from 'ffill', 'bfill', 'interpolate'.")

def remove_outliers_iqr(df, multiplier=1.5):
    """
    Detect and replace outliers using the IQR method.

    Parameters:
        df (pd.DataFrame): DataFrame with numerical columns
        multiplier (float): IQR multiplier (default 1.5)

    Returns:
        pd.DataFrame: DataFrame with outliers replaced by NaN
    """
    def iqr_outliers(col):
        Q1 = col.quantile(0.25)
        Q3 = col.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - multiplier * IQR
        upper_bound = Q3 + multiplier * IQR
        return col.where((col >= lower_bound) & (col <= upper_bound))
    
    return df.apply(iqr_outliers)

def normalize(df, method="minmax"):
    """
    Normalize or standardize numerical columns.

    Parameters:
        df (pd.DataFrame): Input DataFrame
        method (str): 'minmax' or 'zscore' (default 'minmax')

    Returns:
        pd.DataFrame: Normalized DataFrame
    """
    if method == "minmax":
        scaler = MinMaxScaler()
    elif method == "zscore":
        scaler = StandardScaler()
    else:
        raise ValueError("Method must be 'minmax' or 'zscore'")

    scaled_values = scaler.fit_transform(df.values)
    return pd.DataFrame(scaled_values, index=df.index, columns=df.columns)

def resample_to_monthly(df, agg_func="mean"):
    """
    Resample time-indexed data to monthly frequency.

    Parameters:
        df (pd.DataFrame): Time-indexed DataFrame
        agg_func (str): Aggregation function e.g., 'mean', 'sum' (default 'mean')

    Returns:
        pd.DataFrame: Monthly resampled data
    """
    return df.resample("M").agg(agg_func)

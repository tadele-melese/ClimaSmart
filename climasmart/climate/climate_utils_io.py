# climate/climate_utils_io.py
import pandas as pd
import xarray as xr

def read_climate_data(path: str) -> pd.DataFrame:
    """
    Read climate data from CSV or NetCDF.

    Parameters:
        path (str): File path.

    Returns:
        pd.DataFrame: Time series.
    """
    if path.endswith(".csv"):
        df = pd.read_csv(path, parse_dates=True, index_col=0)
    elif path.endswith(".nc"):
        ds = xr.open_dataset(path)
        df = ds.to_dataframe().dropna()
    else:
        raise ValueError("Unsupported file format")
    return df

def write_climate_data(df: pd.DataFrame, path: str, format: str = "csv") -> None:
    """
    Save climate data to CSV or Parquet.

    Parameters:
        df (pd.DataFrame): Time series.
        path (str): Output path.
        format (str): 'csv' or 'parquet'.
    """
    if format == "csv":
        df.to_csv(path)
    elif format == "parquet":
        df.to_parquet(path)
    else:
        raise ValueError("Unsupported format")

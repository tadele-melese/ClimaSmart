# download_from_opendap.py
import xarray as xr
import os

def download_opendap_dataset(url: str, variable: str, output_file: str):
    """
    Download and save data from OPeNDAP server using xarray.
    :param url: URL to dataset
    :param variable: variable name to extract
    :param output_file: local file path to save NetCDF
    """
    ds = xr.open_dataset(url)
    ds[variable].to_netcdf(output_file)


# Optional: cache decorator
try:
    from joblib import Memory
    memory = Memory(location=".climasmart_cache", verbose=0)
except ImportError:
    memory = None

if memory:
    download_opendap_dataset = memory.cache(download_opendap_dataset)
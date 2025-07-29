import numpy as np
import pandas as pd
import xarray as xr
import os
from typing import Union

# Optional imports
try:
    import pyeto
except ImportError:
    pyeto = None

from sklearn.preprocessing import StandardScaler

### 1. Evapotranspiration Estimation ###
def compute_evapotranspiration(temp: xr.DataArray,
                                radiation: xr.DataArray,
                                wind_speed: xr.DataArray,
                                humidity: xr.DataArray,
                                method="penman-monteith") -> xr.DataArray:
    """
    Compute reference evapotranspiration (ET0).
    Supported methods: 'penman-monteith' (default), 'hargreaves'
    """
    if method == "penman-monteith":
        if pyeto is None:
            raise ImportError("pyeto is required for Penman-Monteith method")
        # TODO: implement with pyeto using variables passed as xr.DataArrays
        raise NotImplementedError("Penman-Monteith method requires detailed inputs and calibration.")

    elif method == "hargreaves":
        tmin = temp.min(dim="time")
        tmax = temp.max(dim="time")
        tmean = temp.mean(dim="time")
        ra = radiation  # Assumes radiation is extraterrestrial or net radiation

        et0 = 0.0023 * ra * ((tmax - tmin) ** 0.5) * (tmean + 17.8)
        return et0

    else:
        raise ValueError("Method must be 'penman-monteith' or 'hargreaves'")


### 2. Resample Climate Data ###
def resample_climate_data(data: Union[pd.DataFrame, xr.Dataset], freq="M", agg="mean"):
    """
    Resample DataFrame or Dataset to given frequency (monthly/seasonal).
    :param freq: 'M', 'Q', 'A' etc.
    :param agg: 'mean', 'sum', etc.
    """
    if isinstance(data, pd.DataFrame):
        return getattr(data.resample(freq), agg)()
    elif isinstance(data, xr.Dataset):
        return getattr(data.resample(time=freq), agg)()
    else:
        raise TypeError("Only pandas.DataFrame and xarray.Dataset supported")


### 3. Merge Multi-Source Climate Data ###
def merge_multi_source(chirps: xr.DataArray,
                       era5: xr.Dataset,
                       modis: xr.DataArray) -> xr.Dataset:
    """
    Combine different climate sources by regridding/interpolating.
    Inputs must be aligned by time, space.
    """
    chirps = chirps.rename("precip")
    modis = modis.rename("ndvi")

    merged = xr.merge([chirps, era5, modis])
    return merged


### 4. Cache to Parquet or Zarr ###
def cache_to_parquet(data: Union[pd.DataFrame, xr.Dataset], path: str):
    """
    Save dataset locally to Parquet (for DataFrame) or Zarr (for xarray).
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

    if isinstance(data, pd.DataFrame):
        data.to_parquet(path, index=True)
    elif isinstance(data, xr.Dataset):
        data.to_zarr(path, mode="w")
    else:
        raise TypeError("Only pandas.DataFrame and xarray.Dataset supported")


### 5. Streamlit Climate Dashboard ###
def climate_dashboard():
    import streamlit as st
    import altair as alt

    st.title("🌍 Climate Monitoring Dashboard")

    uploaded = st.file_uploader("Upload CSV or NetCDF", type=["csv", "nc"])
    if uploaded:
        if uploaded.name.endswith(".csv"):
            df = pd.read_csv(uploaded, parse_dates=True, index_col=0)
        elif uploaded.name.endswith(".nc"):
            ds = xr.open_dataset(uploaded)
            df = ds.to_dataframe().dropna()
        else:
            st.warning("Unsupported format")
            return

        st.subheader("📈 Time Series Viewer")
        col = st.selectbox("Select variable", df.columns)
        chart = alt.Chart(df.reset_index()).mark_line().encode(
            x="index:T", y=col
        ).interactive()
        st.altair_chart(chart, use_container_width=True)

        st.subheader("📊 Heatmap Viewer")
        df["month"] = df.index.month
        df["year"] = df.index.year
        st.dataframe(df.groupby(["year", "month"])[col].mean().unstack())

        st.subheader("📉 Anomaly Plot")
        scaler = StandardScaler()
        df["anomaly"] = scaler.fit_transform(df[[col]])
        st.line_chart(df[["anomaly"]])

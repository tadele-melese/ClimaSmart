import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from climasmart.data.fetch_chirps import fetch_chirps
from climasmart.indices.spi import compute_spi
from climasmart.indices.spei import compute_spei
from climasmart.indices.vci import compute_vci
from climasmart.anomaly.forecast import forecast_lstm

st.set_page_config(layout="wide", page_title="ClimaSmart Dashboard")
st.title("🌍 ClimaSmart: Climate Monitoring Dashboard")

# Sidebar settings
st.sidebar.header("Settings")
index_type = st.sidebar.selectbox("Select Index", ["SPI", "SPEI", "VCI"])
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2000-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2024-12-31"))
timescale = st.sidebar.slider("Timescale (months)", 1, 12, 3)
forecast_months = st.sidebar.slider("Forecast Months", 1, 12, 6)

# Load rainfall data
st.subheader("1. Simulated Rainfall Data (CHIRPS)")
rainfall_data = fetch_chirps(start=str(start_date), end=str(end_date), region="ethiopia")
st.line_chart(rainfall_data)

# Compute selected climate index
st.subheader(f"2. {index_type} Computation")
if index_type == "SPI":
    index_result = compute_spi(rainfall_data, timescale=timescale)
elif index_type == "SPEI":
    pet = rainfall_data * 0.6  # Simulated PET, replace with real PET for production
    index_result = compute_spei(rainfall_data, pet, timescale=timescale)
elif index_type == "VCI":
    index_result = compute_vci(rainfall_data)

# Plot climate index
fig, ax = plt.subplots(figsize=(10, 4))
index_result.plot(ax=ax, title=f"{index_type} Index")
ax.axhline(0, color='gray', linestyle='--')
st.pyplot(fig)

# Forecast with LSTM
st.subheader("3. LSTM-Based Forecast")
forecast = forecast_lstm(index_result.dropna(), n_input=timescale, n_forecast=forecast_months)

fig2, ax2 = plt.subplots(figsize=(10, 4))
index_result.plot(ax=ax2, label='Observed')
forecast.plot(ax=ax2, label='Forecast', linestyle='--')
ax2.set_title(f"{index_type} Forecast for {forecast_months} Months Ahead")
ax2.legend()
st.pyplot(fig2)

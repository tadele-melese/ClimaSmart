# 🌦️ ClimaSmart

**ClimaSmart** is an open-source Python toolkit for climate monitoring, drought analysis, and anomaly detection. It integrates statistical indices (SPI, SPEI, VCI, PDSI), machine learning models (LSTM, Transformer), and geospatial tools (GEE, MODIS, shapefiles) into one user-friendly package.

> Designed for climate scientists, environmental researchers, and decision-makers working on drought, forecasting, and spatial climate analytics.

---

## ✨ Features

### ✅ Climate Indices

- **SPI**, **SPEI**, **VCI**, **PDSI**, **SC-PDSI**
- **Z-score Anomalies** from long-term baseline
- **Fire Weather Index (FWI)**
- **Evaporative Demand Drought Index (EDDI)**

### 🤖 Forecasting & Anomaly Detection

- LSTM & Transformer-based time series forecasting
- Drought onset & recovery detection
- SHAP/LIME model interpretability

### 🛰️ Remote Sensing Integration

- CHIRPS, ERA5, MODIS NDVI/ET support
- Google Earth Engine (GEE) integration
- NDVI anomaly detection

### 🗺️ Geospatial Analysis

- Load & process regions from Shapefiles, GeoJSON, or bounding boxes
- Compute zonal stats (mean, std, anomaly flags) over time
- Batch process multiple regions with parallel execution

### 📈 Visualization Tools

- Time series, composite maps, anomaly heatmaps
- Mann-Kendall trend maps
- Interactive Streamlit dashboards (optional)

---

## 📦 Installation

```bash
pip install climasmart
```

> If using remote sensing features, also authenticate Earth Engine:

```bash
earthengine authenticate
```

---

## 🧪 Example Usage

```python
from climasmart.indices import compute_spi
from climasmart.visualization import plot_index_series
from climasmart.anomaly import forecast_lstm
from climasmart.geospatial import Region

# Load data & region
region = Region.from_shapefile("ethiopia_districts.shp")
climate_data = region.load_raster("precip_2000_2020.tif")

# Calculate SPI and plot
spi = compute_spi(climate_data, scale=3)
plot_index_series(spi, title="3-month SPI")

# Forecast SPI using LSTM
forecast = forecast_lstm(spi)

# Export results
region.save_to_csv(spi, "outputs/spi_results.csv")
```

---

## 📂 Project Structure

```
climasmart/
├── indices/           # SPI, SPEI, VCI, PDSI, etc.
├── anomaly/           # LSTM, Transformer, SHAP
├── geospatial/        # Region handling, zonal stats
├── visualization/     # Maps, charts, dashboards
├── data/              # Fetch CHIRPS/ERA5
├── cli.py             # Command-line interface
├── climate         #  Merge Multi-Source Climate Data
├── streamlit_app.py   # Optional dashboard
```

---

## 🛠 Requirements

Python 3.8+

```text
numpy, pandas, xarray, scipy, scikit-learn, matplotlib, seaborn,
tensorflow, torch, statsmodels, streamlit,
rasterio, geopandas, shapely, geemap, earthengine-api,
pymannkendall, tqdm, shap, folium, ipyleaflet, dask
```

---

## 📖 Documentation

📚 Coming soon at [https://climasmart.readthedocs.io](https://climasmart.readthedocs.io)

For now, check out the [examples/](examples/) and [notebooks/](notebooks/) folders.

---

## 🧑‍💻 Author

**Tadele Melese**  
[GitHub](https://github.com/tadele-melese) | [Email](mailto:tadelemelese21m@gmail.com)

---

## 📄 License

MIT License. See [`LICENSE`](LICENSE).

---

## 🙌 Acknowledgments

- CHIRPS & ERA5 data providers
- Google Earth Engine (GEE)
- MODIS remote sensing products
- PyMannKendall, SHAP, TensorFlow, GeoPandas

---

> “Turning climate data into actionable insight.”

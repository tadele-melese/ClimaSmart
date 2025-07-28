# ClimaSmart 🌍

**ClimaSmart** is an open-source Python toolkit for climate data analysis, drought monitoring, and forecasting. It provides computation of key drought indices, vegetation condition metrics, and integrates Google Earth Engine for remote sensing data access. The package also supports advanced LSTM forecasting and interactive visualizations via Streamlit.

---

## Features

- Calculation of drought indices:

  - Standardized Precipitation Index (SPI)
  - Standardized Precipitation Evapotranspiration Index (SPEI)
  - Vegetation Condition Index (VCI)
  - Temperature and Rainfall anomalies

- Data preprocessing utilities (missing value handling, normalization, outlier detection)

- LSTM-based forecasting for climate indices

- Google Earth Engine (GEE) support for cloud-based remote sensing data access

- Interactive Streamlit dashboard for visualization and exploration

- Visualization modules for time series, heatmaps, spatial anomaly maps, and forecasts

---

## Installation

```bash
pip install climasmart
```

Or clone the repository and install dependencies:

bash
Copy
Edit
git clone https://github.com/tadele-melese/ClimaSmart.git
cd ClimaSmart
pip install -r requirements.txt

Quick Start
Compute SPI:
python
Copy
Edit
from climasmart.indices.spi import compute_spi
import pandas as pd

# Example: load your monthly precipitation time series as a pandas Series

precip = pd.Series([...], index=pd.date_range('2000-01-01', periods=120, freq='M'))
spi = compute_spi(precip, scale=3)
print(spi.tail())
Launch Streamlit dashboard:
bash
Copy
Edit
streamlit run streamlit_app.py
Usage Highlights
Preprocessing: Handle missing data, remove outliers, normalize data

Indices: Compute SPI, SPEI, VCI, PDSI (mock), and anomalies

Forecasting: Use LSTM models for climate index prediction

GEE Integration: Fetch satellite and climate data without downloading locally

Visualization: Plot time series, heatmaps, anomaly maps, and forecasts interactively

Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check issues or submit pull requests.

License
This project is licensed under the MIT License.

Contact
Created by Tadele Melese
Email: tadelemelese21m@gmail.com
GitHub: https://github.com/tadele-melese

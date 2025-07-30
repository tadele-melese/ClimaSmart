from .data import (
    fetch_chirps,
    initialize_ee,
    get_chirps_monthly,
    fill_missing_values,
    remove_outliers_iqr,
    normalize,
    resample_to_monthly,
)
from .indices import (
    compute_spi,
    compute_spei,
    compute_mock_pdsi,
    compute_vci,
    compute_temperature_anomaly,
    compute_rainfall_anomaly,
)
from .anomaly import forecast_lstm, detect_anomaly
from .visualize import (
    plot_index_series,
    plot_heatmap,
    plot_anomaly_map,
    plot_forecast,
)
from .utils import setup_logger, ensure_dir, safe_divide, date_range, series_to_dataframe, rolling_mean


# === ANOMALY MODULE ===
from .anomaly.detect_anomaly import *
from .anomaly.drought_event_detector import *
from .anomaly.explainability import *
from .anomaly.forecast import *
from .anomaly.forecast_transformer import *

# === CLIMATE MODULE ===
from .climate.climate_anomaly import *
from .climate.climate_metrics import *
from .climate.climate_normal import *
from .climate.climate_trend import *
from .climate.climate_utils_io import *
from .climate.cli import *
from .climate.utils import *

# === DATA MODULE ===
from .data.fetch_chirps import *
from .data.fetch_era5 import *
from .data.fetch_modis import *
from .data.fetch_sentinel import *
from .data.download_from_opendap import *
from .data.gee_support import *
from .data.preprocess import *

# === Geospatial ====
from .geospatial.region import *

# === indices ===

from .indices.climate_zscore import *
from .indices.eddi import *
from .indices.fwi import *
from .indices.ndvi_anomaly import *
from .indices.pdsi import *
from .indices.rainfall_anomaly  import *
from .indices.scpdsi import *
from .indices.spei import *
from .indices.spi import *
from .indices.temperature_anomaly import *
from .indices.vci import *

#===test===
from .tests.test_cli import *
from .tests.test_region import *

# ===Visualization ===
from .visualize.interactive_dashboard import *
from .visualize.plot_anomaly_map import *
from .visualize.plot_composit_map import *
from .visualize.plot_drought_events import *
from .visualize.plot_forecast import *
from .visualize.plot_heatmap import *
from .visualize.plot_timeseries import *
from .visualize.plot_trend_map import *

# === UTILS ===
from .utils import (
    setup_logger,
    ensure_dir,
    safe_divide,
    date_range,
    series_to_dataframe,
    rolling_mean,
)

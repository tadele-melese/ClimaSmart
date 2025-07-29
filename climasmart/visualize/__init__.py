from .plot_composite_map import plot_composite_anomaly_map
from .plot_trend_map import plot_trend_map
from .plot_drought_events import plot_drought_event_series
from .plot_timeseries import plot_index_series
from .plot_heatmap import plot_heatmap
from .plot_anomaly_map import plot_anomaly_map
from .plot_forecast import plot_forecast

# Optional dashboard support
try:
    from .interactive_dashboard import run_dashboard
except ImportError:
    run_dashboard = None

__all__ = [
    "plot_composite_anomaly_map",
    "plot_trend_map",
    "plot_drought_event_series",
    "plot_index_series",
    "plot_heatmap",
    "plot_anomaly_map",
    "plot_forecast",
    "run_dashboard",
]

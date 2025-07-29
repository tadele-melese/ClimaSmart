import xarray as xr
import matplotlib.pyplot as plt

def plot_composite_anomaly_map(data: xr.DataArray, events: list, window: int = 1, title="Composite Anomaly Map"):
    """
    Plot average anomaly map over specified years/events.
    
    Args:
        data (xr.DataArray): Climate variable with dimensions (time, lat, lon)
        events (list): List of years or datetime indices
        window (int): Averaging window in years or time steps
    """
    composite = sum([data.sel(time=str(year)).rolling(time=window, center=True).mean() for year in events]) / len(events)
    mean_composite = composite.mean(dim='time')

    mean_composite.plot(cmap='RdBu_r')
    plt.title(title)
    plt.show()

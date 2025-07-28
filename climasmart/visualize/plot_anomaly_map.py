import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import show
import numpy as np

def plot_anomaly_map(raster_path, vmin=None, vmax=None, title="Spatial Anomaly Map"):
    """
    Plot a spatial anomaly map from a raster file.

    Parameters:
        raster_path (str): File path to the raster (.tif)
        vmin, vmax (float): Color scale min and max
        title (str): Plot title

    Returns:
        matplotlib.figure.Figure: The generated figure
    """
    with rasterio.open(raster_path) as src:
        data = src.read(1)
        plt.figure(figsize=(10, 8))
        img = plt.imshow(data, cmap='RdBu_r', vmin=vmin, vmax=vmax)
        plt.colorbar(img, label='Anomaly Value')
        plt.title(title)
        plt.axis('off')
        plt.tight_layout()
        plt.show()

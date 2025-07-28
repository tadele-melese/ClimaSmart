import matplotlib.pyplot as plt
import pandas as pd

def plot_forecast(observed, forecast, title="Forecast vs Observed", xlabel="Time", ylabel="Value"):
    """
    Plot observed vs forecast time series.

    Parameters:
        observed (pd.Series): Observed historical data
        forecast (pd.Series): Forecasted future data
        title (str): Plot title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label

    Returns:
        matplotlib.figure.Figure: The generated figure
    """
    plt.figure(figsize=(12, 6))
    plt.plot(observed.index, observed.values, label="Observed", color="blue")
    plt.plot(forecast.index, forecast.values, label="Forecast", color="red", linestyle="--")
    plt.fill_between(forecast.index, forecast.values * 0.95, forecast.values * 1.05, color='red', alpha=0.2, label="Forecast Uncertainty")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.show()

import matplotlib.pyplot as plt
import pandas as pd

def plot_drought_event_series(index_series: pd.Series, threshold: float = -1.0, title="Drought Event Timeline"):
    """
    Plot a time series with annotated drought events (onset, duration, recovery).
    """
    drought = index_series < threshold

    plt.figure(figsize=(12, 4))
    plt.plot(index_series.index, index_series.values, label="Index")
    plt.axhline(threshold, color='red', linestyle='--', label='Drought Threshold')

    # Mark drought events
    for i in range(1, len(drought)):
        if drought.iloc[i] and not drought.iloc[i - 1]:
            plt.axvline(index_series.index[i], color='orange', linestyle=':', label='Onset')
        elif not drought.iloc[i] and drought.iloc[i - 1]:
            plt.axvline(index_series.index[i], color='green', linestyle='--', label='Recovery')

    plt.legend()
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Index Value")
    plt.tight_layout()
    plt.show()


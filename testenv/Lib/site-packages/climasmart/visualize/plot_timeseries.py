
import matplotlib.pyplot as plt

def plot_index_series(series, title='Climate Index'):
    plt.figure(figsize=(12,4))
    series.plot()
    plt.axhline(0, color='gray', linestyle='--')
    plt.title(title)
    plt.grid(True)
    plt.show()

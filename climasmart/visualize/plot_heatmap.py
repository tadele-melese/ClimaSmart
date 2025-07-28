import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_heatmap(df, title="Heatmap of Climate Variables"):
    """
    Plot heatmap of a DataFrame (e.g., correlations or time-series values).

    Parameters:
        df (pd.DataFrame): Data to plot (rows = time or samples, columns = variables)
        title (str): Plot title

    Returns:
        matplotlib.figure.Figure: The generated figure
    """
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(title)
    plt.tight_layout()
    plt.show()

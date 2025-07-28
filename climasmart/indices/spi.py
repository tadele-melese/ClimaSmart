
import numpy as np
import pandas as pd
from scipy.stats import gamma

def compute_spi(precip_series, timescale=3):
    rolling = precip_series.rolling(window=timescale).sum()
    rolling = rolling.dropna()

    # Fit gamma distribution and calculate SPI
    spi_values = []
    for val in rolling:
        valid_vals = rolling[rolling > 0]
        alpha, loc, beta = gamma.fit(valid_vals)
        cdf = gamma.cdf(val, alpha, loc=loc, scale=beta)
        spi = (cdf - 0.5) * 2  # approximate z-score
        spi_values.append(spi)

    spi_series = pd.Series(spi_values, index=rolling.index)
    return spi_series

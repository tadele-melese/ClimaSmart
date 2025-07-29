
import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy.optimize import curve_fit

def loglogistic_cdf(x, alpha, beta, gamma):
    return 1 / (1 + (x / alpha) ** (-beta)) ** gamma

def compute_spei(precip_series, pet_series, timescale=3):
    climatic_balance = precip_series - pet_series
    rolling = climatic_balance.rolling(window=timescale).sum().dropna()

    valid_vals = rolling[rolling != 0]
    shape_params, _ = curve_fit(loglogistic_cdf, np.sort(valid_vals), np.linspace(0.01, 0.99, len(valid_vals)))

    cdf_vals = loglogistic_cdf(rolling, *shape_params)
    spei = pd.Series(norm.ppf(cdf_vals), index=rolling.index)
    return spei

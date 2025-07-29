# FWI system is complex; this is a placeholder.
# Full model would require temperature, wind, humidity, and precipitation.
def compute_fwi(temp, rh, wind, precip):
    """
    Placeholder: Compute a simplified Fire Weather Index (FWI).
    """
    dryness = temp * (1 - rh / 100)
    wind_factor = wind / 10
    rain_effect = np.exp(-precip / 10)

    fwi = dryness * wind_factor * rain_effect
    return fwi

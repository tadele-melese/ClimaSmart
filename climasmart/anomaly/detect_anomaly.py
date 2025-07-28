
def detect_anomaly(index_series, threshold=-1.5):
    return index_series[index_series <= threshold]

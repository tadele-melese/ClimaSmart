import pandas as pd

def detect_drought_events(index_series: pd.Series, threshold: float = -1.0):
    """
    Identify drought periods based on threshold (e.g., SPI < -1.0).
    Returns: list of (start_date, end_date) tuples
    """
    below = index_series < threshold
    events = []
    in_event = False
    start = None

    for t, is_drought in below.items():
        if is_drought and not in_event:
            start = t
            in_event = True
        elif not is_drought and in_event:
            end = t
            events.append((start, end))
            in_event = False

    if in_event:
        events.append((start, index_series.index[-1]))

    return events

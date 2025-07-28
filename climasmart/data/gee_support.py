
import ee
import geemap
import pandas as pd
import datetime

# Authenticate Earth Engine
def initialize_ee():
    try:
        ee.Initialize()
    except Exception as e:
        ee.Authenticate()
        ee.Initialize()

# Fetch CHIRPS monthly data for a region and date range
def get_chirps_monthly(region, start_date, end_date):
    initialize_ee()

    chirps = ee.ImageCollection("UCSB-CHG/CHIRPS/DAILY")         .filterDate(start_date, end_date)         .filterBounds(region)

    def monthly_sum(img):
        date = ee.Date(img.get("system:time_start"))
        month_start = date.format("YYYY-MM")
        monthly = img.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=region,
            scale=5000,
            maxPixels=1e13
        )
        return ee.Feature(None, {
            'date': month_start,
            'precip': monthly.get('precipitation')
        })

    daily_list = chirps.toList(chirps.size())
    features = daily_list.map(lambda img: monthly_sum(ee.Image(img)))
    feature_collection = ee.FeatureCollection(features)

    results = feature_collection.reduceColumns(
        reducers=ee.Reducer.toList(2),
        selectors=['date', 'precip']
    )

    dates = results.get('list').get(0)
    values = results.get('list').get(1)

    dates = ee.List(dates).getInfo()
    values = ee.List(values).getInfo()

    series = pd.Series(values, index=pd.to_datetime(dates))
    series.name = "CHIRPS Precip"
    return series

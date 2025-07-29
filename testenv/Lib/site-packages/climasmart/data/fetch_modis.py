# fetch_modis.py
import ee

def fetch_modis_ndvi(start_date: str, end_date: str, region):
    """
    Fetch MODIS NDVI (MOD13Q1) from Earth Engine.
    :param start_date: Start date (YYYY-MM-DD)
    :param end_date: End date (YYYY-MM-DD)
    :param region: ee.Geometry polygon
    :return: ee.ImageCollection
    """
    ee.Initialize()
    ndvi = (ee.ImageCollection("MODIS/006/MOD13Q1")
            .filterDate(start_date, end_date)
            .select("NDVI")
            .map(lambda img: img.divide(10000).copyProperties(img, ["system:time_start"]))
            .map(lambda img: img.clip(region)))
    return ndvi


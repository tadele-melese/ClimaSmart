import ee

def fetch_sentinel2(region, start_date, end_date, cloud_pct=20):
    """Fetch Sentinel-2 surface reflectance with optional cloud filtering."""
    sentinel = (ee.ImageCollection('COPERNICUS/S2_SR')
                .filterBounds(region)
                .filterDate(start_date, end_date)
                .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', cloud_pct)))
    return sentinel

def compute_ndvi_sentinel(image):
    """Compute NDVI from a Sentinel-2 image."""
    ndvi = image.normalizedDifference(['B8', 'B4']).rename('NDVI')
    return image.addBands(ndvi)

def fetch_ndvi_sentinel(region, start_date, end_date, cloud_pct=20):
    """Fetch pre-processed NDVI images from Sentinel-2."""
    s2 = fetch_sentinel2(region, start_date, end_date, cloud_pct)
    s2_ndvi = s2.map(compute_ndvi_sentinel)
    return s2_ndvi.select('NDVI')

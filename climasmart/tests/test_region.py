from climasmart.geospatial.region import Region

def test_load_shapefile():
    region = Region.from_shapefile("tests/data/sample_zones.shp")
    assert region.gdf is not None
    assert not region.gdf.empty

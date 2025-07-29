import geopandas as gpd
from shapely.geometry import box

class Region:
    def __init__(self, gdf: gpd.GeoDataFrame):
        self.gdf = gdf

    @classmethod
    def from_shapefile(cls, path: str):
        gdf = gpd.read_file(path)
        return cls(gdf)

    @classmethod
    def from_geojson(cls, path: str):
        gdf = gpd.read_file(path)
        return cls(gdf)

    @classmethod
    def from_bbox(cls, bounds: tuple):
        """
        bounds = (minx, miny, maxx, maxy)
        """
        geom = box(*bounds)
        gdf = gpd.GeoDataFrame(geometry=[geom], crs="EPSG:4326")
        return cls(gdf)

    def to_crs(self, crs):
        self.gdf = self.gdf.to_crs(crs)
        return self

    def plot(self, **kwargs):
        return self.gdf.plot(**kwargs)

    def get_geometry(self):
        return self.gdf.geometry

    def __repr__(self):
        return f"<Region with {len(self.gdf)} geometries>"

# fetch_era5.py

import os
import cdsapi
import ee

def download_era5_cdsapi(
    variable: str,
    year: int,
    month: int,
    day: int,
    time: list,
    area: list,
    target_file: str,
    pressure_level: str = None,
    dataset: str = "reanalysis-era5-single-levels"
):
    """
    Download ERA5 climate data using CDS API.
    
    Parameters:
        variable (str or list): Variable(s) to download (e.g., '2m_temperature')
        year (int): Year of the data
        month (int): Month (1–12)
        day (int): Day (1–31)
        time (list): List of time strings (e.g., ['00:00', '06:00', '12:00', '18:00'])
        area (list): [North, West, South, East] geographic extent
        target_file (str): Output NetCDF file path
        pressure_level (str): Optional pressure level (e.g., '850'), only used if downloading pressure level data
        dataset (str): Dataset ID (default is 'reanalysis-era5-single-levels')
    """
    c = cdsapi.Client()

    request = {
        "product_type": "reanalysis",
        "format": "netcdf",
        "variable": variable if isinstance(variable, list) else [variable],
        "year": str(year),
        "month": f"{month:02d}",
        "day": f"{day:02d}",
        "time": time,
        "area": area,
    }

    if "pressure-levels" in dataset:
        request["pressure_level"] = str(pressure_level)

    c.retrieve(dataset, request, target_file)


def fetch_era5_gee(region, start_date, end_date):
    """
    Fetch ERA5-Land monthly climate variables using Google Earth Engine.

    Parameters:
        region (ee.Geometry): Earth Engine geometry
        start_date (str): Start date (e.g., "2020-01-01")
        end_date (str): End date (e.g., "2021-01-01")

    Returns:
        ee.ImageCollection: ERA5-Land monthly collection
    """
    dataset = (ee.ImageCollection("ECMWF/ERA5_LAND/MONTHLY")
               .filterDate(start_date, end_date)
               .filterBounds(region))
    
    # Available bands include:
    # 'dewpoint_temperature_2m', 'temperature_2m', 'total_precipitation',
    # 'u_component_of_wind_10m', 'v_component_of_wind_10m',
    # 'surface_net_solar_radiation', etc.

    return dataset


def fetch_era5_daily_mean(region, start_date, end_date, band='temperature_2m'):
    """
    Compute daily mean values from ERA5-Land hourly data (via GEE).

    Parameters:
        region (ee.Geometry): Region of interest
        start_date (str): e.g., '2021-01-01'
        end_date (str): e.g., '2021-12-31'
        band (str): Variable to extract

    Returns:
        ee.ImageCollection: Daily mean images
    """
    hourly = (ee.ImageCollection("ECMWF/ERA5_LAND/HOURLY")
              .filterDate(start_date, end_date)
              .filterBounds(region)
              .select(band))

    def to_daily_mean(img):
        date = ee.Date(img.get("system:time_start")).format('YYYY-MM-dd')
        return img.set("date", date)

    hourly = hourly.map(to_daily_mean)

    daily_mean = hourly.reduce(ee.Reducer.mean()).clip(region)
    return daily_mean


# Optional: helper function for list of supported variables
def supported_era5_variables():
    return [
        "2m_temperature", "2m_dewpoint_temperature", "total_precipitation",
        "surface_net_solar_radiation", "10m_u_component_of_wind", "10m_v_component_of_wind",
        "surface_pressure", "evaporation", "runoff", "volumetric_soil_water_layer_1"
    ]

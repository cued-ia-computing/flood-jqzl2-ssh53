import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    


import numpy as np 
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def test_stations_level_over_threshold():
    tol = np.random.randn()
    stations = build_station_list()
    update_water_levels(stations)
    x = stations_level_over_threshold(stations, tol)
    for i in range(0, len(x)):
        assert x[i][1] > tol
        if i == 0:
            pass
        elif i > 0:
            assert x[i][1] < x[i - 1][1]

    
import numpy as np 
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stations_level_over_threshold():
    tol = abs(np.random.randn())
    stations = build_station_list()
    update_water_levels(stations)
    x = stations_level_over_threshold(stations, tol)
    for i in range(0, len(x)):
        assert x[i][1] > tol
        if i == 0:
            pass
        elif i > 0:
            assert x[i][1] <= x[i - 1][1]

def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    N = random.randint(1, len(stations))
    highest_stations = stations_highest_rel_level(stations, N)
    
    for i in stations, j in highest_stations:
        if i == j:
            pass 
        
        elif i != j:
            assert i.relative_water_level() <= highest_stations[N-1].relative_water_level()
    
    for k in range(0, len(highest_stations)):
        if k == 0:
            pass
        elif k > 0:
            assert highest_stations[k].relative_water_level() <= highest_stations[k - 1].relative_water_level()


    



    
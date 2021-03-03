from floodsystem.geo import stations_by_distance, rivers_with_station, stations_by_river, stations_within_radius, rivers_by_station_number
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit

def test_stations_by_distance():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    x = stations_by_distance(stations, p)
    for i in range(0, len(x)):
        if i == 0:
            pass
        
        else:
            assert x[i][1] >= x[i-1][1]
    
def test_rivers_with_station():
    stations = build_station_list()
    x = rivers_with_station(stations)
    for river in x:
        y = False
        count = 0
        for i in x:
            if i == river:
                count += 1
            else:
                pass
        for station in stations:
            if station.river == river:
                y = True
                
            else:
                pass
        assert y == True 
        assert count == 1
        
def test_stations_by_river():
    stations = build_station_list()
    x = stations_by_river(stations)
    for river, stations_list in x.items():
        for station in stations_list:
            assert station.river == river

def test_stations_within_radius():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 0
    x = stations_within_radius(stations, centre, r)

    assert len(x) == 0

def test_rivers_by_station_number():
    
    N = 2
    stations = build_station_list()
    x = rivers_by_station_number(stations, N)
    rivers = rivers_with_station(stations)
    riverdict = stations_by_river(stations)
    
    for river in rivers:
        assert (x[0][1]) >= len(riverdict[river])
        assert (x[0]) >= (x[1])

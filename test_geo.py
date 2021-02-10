from floodsystem.geo import stations_by_distance, rivers_with_station, stations_by_river, stations_within_radius
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit

def test_stations_by_distance():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    x = stations_by_distance(stations, p)
    y = []
    for i in x:
        y.append((i[0].name, i[0].town))
    assert y[:10] == [('Cambridge Jesus Lock', 'Cambridge'), ('Bin Brook', 'Cambridge'), 
    ("Cambridge Byron's Pool", 'Grantchester'), ('Cambridge Baits Bite', 'Milton'), 
    ('Girton', 'Girton'), ('Haslingfield Burnt Mill', 'Haslingfield'), 
    ('Oakington', 'Oakington'), ('Stapleford', 'Stapleford'), 
    ('Comberton', 'Comberton'), ('Dernford', 'Great Shelford')]
    
    

def test_rivers_with_station():
    stations = build_station_list()
    x = rivers_with_station(stations)

def test_stations_by_river():
    stations = build_station_list()
    x = stations_by_river(stations)

def test_stations_within_radius():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 0
    x = stations_within_radius(stations, centre, r)

    assert len(x) == 0
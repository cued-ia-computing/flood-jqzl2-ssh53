from floodsystem.geo import stations_by_distance, rivers_with_station, stations_by_river, stations_within_radius
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit

def test_stations_by_distance():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    y = []
    for i in x:
        y.append((i[0].name, i[0].town, i[1]))
    assert y[:10] == [('Cambridge Jesus Lock', 'Cambridge', 0.8402364350834995), ('Bin Brook', 'Cambridge', 2.502274086951454), 
    ("Cambridge Byron's Pool", 'Grantchester', 4.0720438555077125), ('Cambridge Baits Bite', 'Milton', 5.115589516578674), 
    ('Girton', 'Girton', 5.227070345811418), ('Haslingfield Burnt Mill', 'Haslingfield', 7.044388165868453), 
    ('Oakington', 'Oakington', 7.128249171700346), ('Stapleford', 'Stapleford', 7.265694306995238), 
    ('Comberton', 'Comberton', 7.7350743760373675), ('Dernford', 'Great Shelford', 7.993861351711722)]
    
    

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
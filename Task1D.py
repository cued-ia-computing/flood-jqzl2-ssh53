from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

def run():

    stations = build_station_list()

    x = sorted(rivers_with_station(stations))

    print("*** Number of rivers with at least one monitoring station ***")
    print(len(x))
    print("*** First 10 rivers with at least one monitoring station in alphabetical order ***")
    print(x[:10])

    y = stations_by_river(stations)

    Aire_stations = y["River Aire"]
    Cam_stations = y["River Cam"]
    Thames_stations = y["River Thames"]

    def station_names(river_stations):
        station_names = []
        
        for station in river_stations:
            station_names.append(station.name)
        
        print(sorted(station_names))

    print("*** Monitoring stations on River Aire ***")
    station_names(Aire_stations)
    print("*** Monitoring stations on River Cam***")
    station_names(Cam_stations)
    print(" Monitoring stations on River Thames")
    station_names(Thames_stations)
    
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()

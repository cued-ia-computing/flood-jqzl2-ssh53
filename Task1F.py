from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():

    stations = build_station_list()
    
    x = inconsistent_typical_range_stations(stations)

    station_names = []

    for inconsistent_typical_range_station in x:
        station_names.append(inconsistent_typical_range_station.name)
    
    station_names = sorted(station_names)

    print(station_names)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
    





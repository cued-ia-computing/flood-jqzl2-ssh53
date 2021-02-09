from floodsystem.geo import rivers_by_station_number, stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    
    stations = build_station_list()
    N = 9

    x = rivers_by_station_number(stations, N)

    print(x)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
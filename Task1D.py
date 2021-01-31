from floodsytem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

def run():

    stations = build_station_list()

    x = sorted(rivers_with_station(stations))

    print(len(x))
    print(x[:10])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

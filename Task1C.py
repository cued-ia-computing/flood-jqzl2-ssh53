from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    
    stations = build_station_list()
    x = (52.2053, 0.1218)
    r = 10
    stations_in_radius = stations_within_radius(stations, x, r)
    
    print(stations_in_radius)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()

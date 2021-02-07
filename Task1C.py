from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10
    x = stations_within_radius(stations, centre, r)
    
    print(x)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()

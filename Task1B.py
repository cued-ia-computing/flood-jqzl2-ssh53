from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    
    stations = build_station_list()
    p = (52.2053, 0.1218)
    x = stations_by_distance(stations, p)
    y = []
    for i in x:
        y.append((i[0].name, i[0].town, i[1]))
    
    print(y[:10])
    print(y[-10:])



if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()




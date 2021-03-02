from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():

    stations = build_station_list()
    print(type(stations[0].latest_level))
    update_water_levels(stations)
    print(type(stations[0].latest_level))

    x = stations_highest_rel_level(stations, 10)

    for i in x:
        print(i[0].name + " " + str(i[1]))

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()

    update_water_levels(stations)

    x = stations_highest_rel_level(stations, 10)

    for i in x:
        print(i.name + " " + str(i.relative_water_level()))

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()

from floodsystem.geo import towns_with_station, stations_by_town
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import rate_of_river_level_change
import datetime
import math

def run():
    stations = build_station_list()
    update_water_levels(stations)
    x = stations_by_town(stations)
    risk_of_towns = []
    risk_levels = ("Severe", "High", "Moderate", "Low")
    
    for town in x:
        y = stations_level_over_threshold(x[town], 1.0)
        risk_stations = 0
        
        if len(y) == 0:
            risk_of_towns.append((town, risk_levels[-1])) # If a town has no monitoring stations where the water level is exceeding the typical high, decide that the risk of flooding in that town is low.
        
        elif len(y) > 0:
            z = []
            for i in y: 
                z.append(i[0])
            if len(z) >= 5:    
                N = 5

            elif len(z) < 5:
                N = len(z)

            z = stations_highest_rel_level(z, N)
            for station in z:
                dt = 5
                dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
                rate = rate_of_river_level_change(dates, levels)
                forecasted_level = station.latest_level + rate
                forecasted_rel_level = forecasted_level / (station.typical_range[1] - station.typical_range[0])

                if forecasted_rel_level >= 3: # Count the number of stations which are recording significantly higher than normal levels, setting a relative level of 3 or above as significantly high.
                    risk_stations += 1
                
                elif forecasted_rel_level < 3:
                    pass
            
            if (risk_stations / len(x[town])) <= (1 / 3):  # Evaluate whether a town is at moderate, high or severe risk of flooding by calculating the proportion of its monitoring stations which are experiencing significantly higher than normal levels.
                risk_of_towns.append((town, risk_levels[2]))
            
            elif (risk_stations / len(x[town])) > (1 / 3) and (risk_stations / len(x[town])) <= (2 / 3):
                risk_of_towns.append((town, risk_levels[1]))
            
            elif (risk_stations / len(x[town])) > (2 / 3) and (risk_stations / len(x[town])) <= 1:
                risk_of_towns.append((town, risk_levels[0]))
    
    print("*** Towns with the greatest risk of flooding ***")

    for town in risk_of_towns:
        if town[1] == risk_levels[0] or town[1] == risk_levels[1]: # Give warnings for towns at high and severe risk.
            print(town[0], town[1])
        
        else:
            pass

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
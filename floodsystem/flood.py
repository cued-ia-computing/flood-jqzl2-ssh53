from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    x = []
    
    for station in stations:
        if station.typical_range_consistent() == False:
            pass
        
        elif station.typical_range_consistent() == True:
            if station.relative_water_level() > tol:
                tuple = (station, station.relative_water_level)
                x.append(tuple)
            
            else:
                pass
    
    x = sorted_by_key(x, i, reverse = True)

    return x

                

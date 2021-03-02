import matplotlib.pyplot as plt 
import datetime
import numpy as np 

def plot_water_levels(station, dates, levels):

    typical_low = np.full((len(dates),), station.typical_range[0])
    typical_high = np.full((len(dates),), station.typical_range[1])
    
    plt.plot(dates, levels)
    plt.plot(dates, typical_low)
    plt.plot(dates, typical_high)
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    
    plt.tight_layout()

    plt.show()

    return
    



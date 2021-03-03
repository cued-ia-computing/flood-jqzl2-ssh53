import matplotlib.pyplot as plt 
import datetime
import numpy as np 
from floodsystem.analysis import polyfit
from matplotlib.dates import date2num, num2date

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


def plot_water_level_with_fit(station, dates, levels, p):

    plt.plot(dates, levels)

    poly, d0 = polyfit(dates, levels, p)

    d = date2num(dates)
    x = d-d[0]
    
    l = poly(x)

    typical_low = np.full((len(dates),), station.typical_range[0])
    typical_high = np.full((len(dates),), station.typical_range[1])
    

    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation = 45)

    plt.plot(dates, levels)
    plt.plot(dates, l)
    plt.title(station.name)
    plt.plot(dates, typical_low)
    plt.plot(dates, typical_high)

    plt.show()



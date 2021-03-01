import matplotlib.pyplot as plt 
import datetime

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    plt.plot(dates, station.typical_range[0])
    plt.plot(dates, station.typical_range[1])
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    
    plt.tight_layout()

    plt.show()
    



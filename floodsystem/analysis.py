from matplotlib.dates import date2num, num2date
import numpy as np

def polyfit(dates, levels, p):
 
    x = date2num(dates)
    x = np.array(x)
    y = np.array(levels)
    p_coeff = np.polyfit(x - x[0], y, p)
    poly = np.poly1d(p_coeff)
    d0 = x[0]
    
    return (poly, d0)

def rate_of_river_level_change(dates, levels, p = 1):
    (poly, d0) = polyfit(dates, levels, p)
    derivative = poly.deriv()
    x = date2num(dates)
    x = np.array(x)
    rate = derivative(x[-1] - d0)
    return rate





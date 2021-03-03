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
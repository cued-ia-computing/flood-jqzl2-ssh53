# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

# Task 1B
def stations_by_distance(stations, p):
    
    stations_by_distance = []
    
    for station in stations:
        stations_by_distance.append((station.name, haversine(station.coord, p)))
    
    stations_by_distance = utils.sorted_by_key(stations_by_distance)

    return stations_by_distance



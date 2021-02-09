# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    
    stations_by_distance = []
    
    for station in stations:
        stations_by_distance.append((station.name, station.town, haversine(station.coord, p)))
    
    stations_by_distance = sorted_by_key(stations_by_distance, 2)

    return stations_by_distance

def rivers_with_station(stations):
    
    rivers_with_station = []

    for station in stations:
        rivers_with_station.append(station.river)
    
    rivers_with_station = set(rivers_with_station)
    
    return rivers_with_station

def stations_by_river(stations):

   stations_by_river = {}

   rivers = rivers_with_station(stations)

   for river in rivers:
       stations_by_river[river] = []

       for station in stations:
           if station.river == river:
               stations_by_river[river].append(station)
            
           else:
               pass

   return stations_by_river
    

def stations_within_radius(stations, centre, r):

    rivers = rivers_with_station(stations)
    stations_within_radius = []

    for station in stations:
        distance = haversine(centre, station.coord)
        if r >= distance:
            stations_within_radius.append(station.name)

    return sorted(stations_within_radius)


def rivers_by_station_number(stations, N):

    rivers_by_station_number = {}
    station_number = []

    for river in rivers:
        rivers_by_station_number[river] = []

    for station in stations:
        rivers_by_station_number[station_number] = len(stations_by_river[river])

    return sorted(rivers_by_station_number)
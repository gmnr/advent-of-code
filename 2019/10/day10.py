#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
solution for day 10
"""

__author__ = "gmnr"
__license__ = "GPL"


from math import degrees as d, atan2, sqrt


with open("input.txt", "r") as f:
    data = f.read()


def convertToMatrix(string):
    """Convert the puzzle input into a matrix of nested list"""
    arr = string.split("\n")
    arr = [list(x) for x in arr]
    return arr


def coordinates(lst):
    """Get the coordinates of every asteroid"""
    res = []
    for y in range(len(lst)):
        for x in range(len(lst[y])):
            if lst[y][x] == "#":
                res.append((x, y))
    return res


def findSlope(tup1, tup2):
    x1, y1 = tup1
    x2, y2 = tup2
    dy = y2 - y1
    dx = x2 - x1
    slope = d(atan2(dy, dx))
    distance = sqrt(dx**2 + dy**2)
    return ((slope + 360) % 360, distance)


def computeDetection(lst):
    """find the number of"""
    results = {}
    for station in lst:
        slopes = {}
        for asteroid in lst:
            if station == asteroid:
                continue
            slope, distance = findSlope(station, asteroid)
            slope = round((slope + 90) % 360, 1)
            slopes.setdefault(slope, []).append((asteroid, round(distance)))
        results.update({station: slopes})
    return results


def findMax(dic):
    """find the maximum value in the dictionary"""
    obs = {k: len(v) for k, v in dic.items()}
    return max(obs, key=obs.get)


coord = coordinates(convertToMatrix(data))
monitor = computeDetection(coord)
station = findMax(monitor)
print(station, "->", len(monitor[station]))


# order the keys by degree and by distance
unordered_station = monitor[station]
fov = {}
for k in sorted(unordered_station.keys()):
    fov.update({k: sorted(unordered_station[k], key=lambda x: x[1])})

destruction_order = []
while True:
    for k, v in fov.items():
        destruction_order.append(v[0][0])
        fov[k].pop(0)
        continue
    break

# find the coordinates of the 200th element
x, y = destruction_order[199]
print(f"({x}, {y}) -> {x * 100 + y}")

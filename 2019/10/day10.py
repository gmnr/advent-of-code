#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
solution for day 10
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


from math import degrees as d, atan2


with open('input.txt', 'r') as f:
    data = f.read()


def convertToMatrix(string):
    """Convert the puzzle input into a matrix of nested list"""
    arr = string.split('\n')
    arr = [list(x) for x in arr]
    return arr


def coordinates(lst):
    """Get the coordinates of every asteroid"""
    res = []
    for y in range(len(lst)):
        for x in range(len(lst[y])):
            if lst[y][x] == '#':
                res.append((x, y))
    return res


def findSlope(tup1, tup2):
    x1, y1 = tup1
    x2, y2 = tup2
    dy = y2 - y1
    dx = x2 - x1
    slope = d(atan2(dy, dx))
    return round((slope + 360) % 360, 1)


def computeDetection(lst):
    results = {}

    for station in lst:
        slopes = {}
        for asteroid in lst:
            if station == asteroid:
                continue
            slope = (findSlope(station, asteroid) + 90) % 360  # rotate so the degree is the same
            slopes.setdefault(slope, []).append(asteroid)
        results.update({station: slopes})
    observables = {k: len(v) for k, v in results.items()}
    return observables


def findMax(dic):
    """find the maximum value in the dictionary"""
    return max(dic, key=dic.get)

# data = ".#..#\n.....\n#####\n....#\n...##"

coord = coordinates(convertToMatrix(data))
monitor = computeDetection(coord)
print(findMax(monitor), '-->', monitor[findMax(monitor)])

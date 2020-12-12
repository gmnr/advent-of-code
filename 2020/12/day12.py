#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 12 2020
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

from collections import defaultdict as dd, deque
from operator import add

def distanceFromStart(end):
    x, y = end
    return abs(x) + abs(y)

def parse(inst):
    d, val = inst[:1], inst[1:]
    return (d, int(val))

def turn(facing, dirs, val):
    times = int(val / 90)
    times = times if dirs == "L" else -times
    cards = deque(["N", "E", "S", "W"])
    s_idx = cards.index(facing)
    cards.rotate(-s_idx)
    cards.rotate(times)
    return cards[0]

def move(coords, amount):
    return tuple(map(lambda x: x * amount, coords))

dirs = {
    "N": (0, 1),
    "S": (0, -1),
    "W": (-1, 0),
    "E": (1, 0),
}

def calc_coord(data):
    journey = dd(int)
    last = (0, 0)
    journey[last] = "E"
    for i in data:
        d, val = parse(i)
        old_d = journey[last]
        if d == "F":
            c = dirs[old_d]
        elif d in ["N", "S", "W", "E"]:
            c = dirs[d]
        else:
            facing = turn(journey[last], d, val)
            journey[last] = facing
            continue
        last = tuple(map(add, last, move(c, val)))
        journey[last] = old_d
    return distanceFromStart(last)

def move_ship(coords, way, amt):
    for _ in range(amt):
        coords = tuple(map(add, coords, way))
    return coords

def rotate_waypoint(coord, d, deg):
    if deg == 90:
        x, y = coord
        coord = (y , -x)
    elif deg == 270:
        x, y = coord
        coord = (-y, x)

    if d == "L" or deg == 180:
        x, y = coord
        coord = (-x, -y)
    return coord

def calc_waypoints(data):
    waypoints = dd(int)
    j_last = (0, 0)
    w_last = (10, 1)
    for i in data:
        d, val = parse(i)
        old_w = waypoints[w_last]
        if d in ["N", "S", "W", "E"]:
            c = dirs[d]
            w_last = tuple(map(add, w_last, move(c, val)))
            waypoints[w_last] = d
        elif d in ["R", "L"]:
            w_last = rotate_waypoint(w_last, d, val)
        else:
            j_last = move_ship(j_last, w_last, val)
    return distanceFromStart(j_last)

# pt 1
print(calc_coord(data))
# pt 2
print(calc_waypoints(data))

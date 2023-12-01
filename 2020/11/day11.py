#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 11 2020
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import defaultdict as dd
from operator import add


def build_coord(data):
    coord = dd(lambda: "x")
    for y in range(len(data)):
        for x in range(len(data[y])):
            coord[(x, y)] = data[y][x]
    return coord


def check_occ(coord, coords):
    x, y = coord
    neigh = (
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x + 1, y + 1),
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
    )
    cnt_occ = 0
    for c in neigh:
        if coords[c] == "#":
            cnt_occ += 1
    return cnt_occ


def check_sight(start, coords):
    cnt_occ = 0
    directions = {
        "N": (0, -1),
        "NE": (1, -1),
        "E": (1, 0),
        "SE": (1, 1),
        "S": (0, 1),
        "SO": (-1, 1),
        "O": (-1, 0),
        "NO": (-1, -1),
    }

    for d in directions.keys():
        coord = start
        while True:
            coord = tuple(map(add, directions[d], coord))
            if coords[coord] == "#":
                cnt_occ += 1
                break
            elif coords[coord] in ["x", "L"]:
                break
    return cnt_occ


def count(dictionary, val):
    return len([x for x in dictionary.values() if x == val])


def findVacant1(floor, coord):
    floor = floor
    while True:
        old_floor = floor.copy()
        for c in coord:
            if old_floor[c] == ".":
                continue
            elif old_floor[c] == "L":
                if check_occ(c, old_floor) == 0:
                    floor[c] = "#"
            elif old_floor[c] == "#":
                if check_occ(c, old_floor) >= 4:
                    floor[c] = "L"
        if count(floor, "#") == count(old_floor, "#"):
            break
    return count(floor, "#")


def findVacant2(floor, coord):
    floor = floor
    while True:
        old_floor = floor.copy()
        for c in coord:
            if old_floor[c] == ".":
                continue
            elif old_floor[c] == "L":
                if check_sight(c, old_floor) == 0:
                    floor[c] = "#"
            elif old_floor[c] == "#":
                if check_sight(c, old_floor) >= 5:
                    floor[c] = "L"
        if count(floor, "#") == count(old_floor, "#"):
            break
    return count(floor, "#")


floor = build_coord(data)
coord = list(floor.keys())

# pt 1
print(findVacant1(floor, coord))
# pt 2
print(findVacant2(build_coord(data), coord))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 11 2017
"""

__author__ = "gmnr"
__license__ = "GPL"

with open("input.txt", "r") as f:
    data = f.read()[:-1].split(",")

from operator import add

mov = {
    "n": (0, 1),
    "ne": (1, 1),
    "se": (1, -1),
    "s": (0, -1),
    "sw": (-1, -1),
    "nw": (-1, 1),
}

pos = (0, 0)
walk = []
for step in data:
    pos = tuple(map(add, pos, mov[step]))
    walk.append(pos)


def distance(start, end):
    x1, y1 = start
    x2, y2 = end

    xSteps = abs(x1 - x2)
    ySteps = abs(y1 - y2)

    return max(xSteps, ySteps)


# pt 1
print(distance((0, 0), pos))
# pt 2
print(max([distance((0, 0), x) for x in walk]))

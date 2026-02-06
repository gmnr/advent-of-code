#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day09 2025
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from itertools import combinations


test = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

data = aoc.read_input(test)


def make_rectangle(a, b):
    ax, ay = a
    bx, by = b
    return (abs(ax - bx) + 1) * (abs(ay - by) + 1)


coord = []
for c in data:
    a, b = c.split(",")
    coord.append((int(a), int(b)))

# pt 1
areas = []
for c in combinations(coord, 2):
    a, b = c
    areas.append(make_rectangle(a, b))
print(areas)
print(max(areas))

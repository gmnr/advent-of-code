#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day03 2018
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import defaultdict as dd
from itertools import product
import re

fabric = dd(int)
rectangles = dd(list)


def parse(line):
    id_, _, coords, dims = line.split()
    x, y = [int(i) for i in coords[:-1].split(",")]
    w, h = [int(i) for i in dims.split("x")]
    return [x, y, w, h, id_[1:]]


def square_coord(x, y, width, height):
    return product(range(x, x + width), range(y, y + height))


for line in data:
    x, y, w, h, id_ = parse(line)
    overlaps = square_coord(x, y, w, h)
    for x, y in overlaps:
        fabric[(x, y)] += 1
        rectangles[id_] += [(x, y)]

# pt 1
overlapping_areas = [k for k, v in fabric.items() if v >= 2]
print(len(overlapping_areas))
# pt 2
for r in rectangles:
    overlap = False
    for c in rectangles[r]:
        if c in overlapping_areas:
            overlap = True
            break
    if not overlap:
        print(r)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day05 2021
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

from collections import defaultdict
from math import atan2, degrees

def is_diagonal(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    rad = atan2(y1 - y2, x1 - x2)
    deg = degrees(rad)
    if abs(deg) == 45 or abs(deg) == 135:
        return deg
    return False

def parse_coords(coord):
    return tuple(map(int, coord.split(',')))

def parse(data):
    vents = []
    diag_vents = []
    for l in data:
        c1, c2 = map(parse_coords, l.split(' -> '))
        for c in gen_line(c1, c2):
            if is_diagonal(c1, c2):
                diag_vents.append(c)
            else:
                vents.append(c)
    return vents, diag_vents

def gen_line(c1, c2):
    x1, y1 = c1
    x2, y2 = c2

    if x1 == x2:
        y_max = max(y1, y2)
        y_min = min(y1, y2)
        for y in range(y_max - y_min + 1):
            yield (x1, y_min+y)
    
    elif y1 == y2:
        x_max = max(x1, x2)
        x_min = min(x1, x2)
        for x in range(x_max - x_min + 1):
            yield (x_min+x, y1)

    if deg := is_diagonal(c1, c2):
        coords = sorted([c1, c2], key=lambda x: x[0])
        deg = is_diagonal(*coords)

        if deg == 135:
            c1, c2 = coords
            x1, y1 = c1
            x2, y2 = c2
            delta = x2 - x1
            for _ in range(delta):
                if _ == 0:
                    yield x1, y1
                x1 += 1
                y1 -= 1
                yield (x1, y1)

        elif deg == -135:
            c1, c2 = coords
            x1, y1 = c1
            x2, y2 = c2
            delta = x2 - x1
            for _ in range(delta):
                if _ == 0:
                    yield x1, y1
                x1 += 1
                y1 += 1
                yield (x1, y1)

    return False

# pt1
grid = defaultdict(int)
vents, diag_vents = parse(data)
for v in vents:
    grid[v] += 1
print(sum(1 for x in grid.values() if x > 1))

# pt2
for v in diag_vents:
    grid[v] += 1
print(sum(1 for x in grid.values() if x > 1))

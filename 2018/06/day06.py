#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day06 2018
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

import re
from itertools import chain
from collections import Counter

def parse_coords(data):
    return [tuple(map(int, re.findall('\d+', x))) for x in data]

def distance(c1, c2):
    x1, y1 = c1; x2, y2 = c2
    return abs(x1 - x2) + abs(y1 - y2)

def closest(point, points):
    p1, p2 = sorted(points, key=lambda p: distance(p, point))[:2]
    return p1 if distance(p1, point) < distance(p2, point) else None

def counts(points, margin=100):
    xs = range(-margin, max(map(lambda x: x[0], points)) + margin)
    ys = range(-margin, max(map(lambda x: x[1], points)) + margin)
    perimeter = [(x, y) for x in xs for y in ys]
    count = Counter(closest(x, points) for x in perimeter)
    for p in border(xs, xs):
        c = closest(p, points)
        if c in count:
            del count[c]
    return count

def border(xside, yside):
    return chain(((xside[0], y)  for y in yside),
                 ((xside[-1], y) for y in yside),
                 ((x, yside[0])  for x in xside),
                 ((x, yside[-1]) for x in xside))

def total(point, points):
    return sum(distance(point, p) for p in points)

def dimension(points, limit=10_000):
    max_x = max(x for x, y in points)
    max_y = max(y for x, y in points)
    perimeter = [(x, y) for x in range(max_x + 1) for y in range(max_y + 1)]
    return len([x for x in perimeter if total(x, points) < limit])

# pt1
coords = parse_coords(data)
counted = counts(coords)
print(max(counted.values()))
# pt2
print(dimension(coords))

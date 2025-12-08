#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day08 2025
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from itertools import combinations
from math import prod

data = aoc.read_input()

# pt 1
boxes = []
for line in data:
    x, y, z = line.split(",")
    boxes.append((int(x), int(y), int(z)))

distances = {}
for c in combinations(boxes, 2):
    a, b = c
    distances[(a, b)] = aoc.euclidean_dist(a, b)

steps = 0
conn = {x: (x,) for x in boxes}
distances = sorted(distances.items(), key=lambda x: x[1])
for c in distances:

    if steps == 1000:
        break

    coord, d = c
    a, b = coord
    if conn[a] != conn[b]:
        new_conn = conn[a] + conn[b]
        for c in new_conn:
            conn[c] = new_conn

    steps += 1

conn = sorted([len(x) for x in set(conn.values())], reverse=True)
print(prod(conn[:3]))

# pt 2
conn = {x: (x,) for x in boxes}
for c in distances:

    coord, d = c
    a, b = coord
    if conn[a] != conn[b]:
        new_conn = conn[a] + conn[b]

        if len(new_conn) == len(boxes):
            print(a[0] * b[0])

        for c in new_conn:
            conn[c] = new_conn

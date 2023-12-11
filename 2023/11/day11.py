#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day11 2023
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from itertools import combinations

data = aoc.read_input()

# pt 1
galaxies = []
for y, row in enumerate(data):
    for x, p in enumerate(row):
        if p == "#":
            galaxies.append((x, y))

seen_rows = set()
seen_cols = set()

rows = set(range(len(data)))
cols = set(range(len(data[0])))

for g in galaxies:
    x, y = g
    seen_rows.add(y)
    seen_cols.add(x)

empty_rows = rows - seen_rows
empty_cols = cols - seen_cols


def expand(galaxies, gap):
    expanded_galaxies = []
    for g in galaxies:
        x, y = g
        cx = cy = 0
        for ex in empty_cols:
            if ex <= x:
                cx += gap

        for ey in empty_rows:
            if ey <= y:
                cy += gap

        expanded_galaxies.append((x + cx, y + cy))
    return expanded_galaxies


# pt 1
pairs = combinations(expand(galaxies, 1), 2)
dist = 0
for p in pairs:
    dist += aoc.manhattan_dist(*p)
print(dist)

# pt 2
pairs = combinations(expand(galaxies, 1_000_000 - 1), 2)
dist = 0
for p in pairs:
    dist += aoc.manhattan_dist(*p)
print(dist)

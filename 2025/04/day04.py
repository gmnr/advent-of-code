#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day04 2025
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from collections import Counter

data = aoc.read_input()

grid = aoc.to_grid(data)
to_remove = []

# pt 1
movable = 0
for c in grid:
    if grid[c] != "@":
        continue
    adjacent = aoc.gen_coordinates(c, n=8)
    vals = []
    for x in adjacent:
        if x not in grid:
            continue
        vals.append(grid[x])

    vals = Counter(vals)
    if vals["@"] < 4:
        movable += 1
        to_remove.append(c)
print(movable)

# pt 2
removed = 0
while to_remove:
    for x in to_remove:
        grid[x] = "."
        removed += 1
        to_remove.pop()
    to_remove = []
    for c in grid:
        if grid[c] != "@":
            continue
        adjacent = aoc.gen_coordinates(c, n=8)
        vals = []
        for x in adjacent:
            if x not in grid:
                continue
            vals.append(grid[x])

        vals = Counter(vals)
        if vals["@"] < 4:
            to_remove.append(c)
print(removed)

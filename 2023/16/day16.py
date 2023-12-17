#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day16 2023
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from collections import deque

data = aoc.read_input()

h = len(data)
w = len(data[0])


def traverse(grid, h, w, r, c, dr, dc):
    energized = set()
    seen_pattern = set()
    paths = deque([(r, c, dr, dc)])

    while paths:
        r, c, dr, dc = paths.pop()

        while 0 <= r < h and 0 <= c < w and (r, c, dr, dc) not in seen_pattern:
            seen_pattern.add((r, c, dr, dc))
            energized.add((r, c))
            char = grid[r][c]
            if char == "/":
                dr, dc = -dc, -dr
            elif char == "\\":
                dr, dc = dc, dr
            elif char == "-":
                if dr != 0:
                    dr, dc = 0, 1
                    paths.append((r, c - 1, 0, -1))
            elif char == "|":
                if dc != 0:
                    dr, dc = 1, 0
                    paths.append((r - 1, c, -1, 0))

            r += dr
            c += dc
    return len(energized)


# pt 1
print(traverse(data, h, w, 0, 0, 0, 1))

# pt 2
best = 0
for r in range(len(data)):
    best = max(best, traverse(data, h, w, r, 0, 0, 1))
    best = max(best, traverse(data, h, w, r, w - 1, 0, -1))
for c in range(len(data[0])):
    best = max(best, traverse(data, h, w, 0, c, 1, 0))
    best = max(best, traverse(data, h, w, h - 1, c, -1, 0))
print(best)

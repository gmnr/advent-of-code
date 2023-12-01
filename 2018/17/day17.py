#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day17 2018
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

import re
import sys

sys.setrecursionlimit(3000)


def flow(grid, x, y, d):
    if grid[y][x] == ".":
        grid[y][x] = "|"
    if y == len(grid) - 1:
        return
    if grid[y][x] == "#":
        return x
    if grid[y + 1][x] == ".":
        flow(grid, x, y + 1, 0)
    if grid[y + 1][x] in "~#":
        if d:
            return flow(grid, x + d, y, d)
        else:
            left_x = flow(grid, x - 1, y, -1)
            right_x = flow(grid, x + 1, y, 1)
            if grid[y][left_x] == "#" and grid[y][right_x] == "#":
                for fillX in range(left_x + 1, right_x):
                    grid[y][fillX] = "~"
    else:
        return x


def solve(data):
    d = []
    for line in data:
        a, b, c = map(int, re.findall("\d+", line))
        d += [(a, a, b, c)] if line[0] == "x" else [(b, c, a, a)]

    Z = list(zip(*d))
    minX, maxX, minY, maxY = min(Z[0]), max(Z[1]), min(Z[2]), max(Z[3])

    grid = [["."] * (maxX - minX + 2) for _ in range(maxY + 1)]
    for x1, x2, y1, y2 in d:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[y][x - minX + 1] = "#"
    springX, springY = 500 - minX + 1, 0
    grid[0][springX] = "+"

    flow(grid, springX, springY, 0)

    still = flowing = 0
    for y in range(minY, maxY + 1):
        for x in range(len(grid[0])):
            if grid[y][x] == "|":
                flowing += 1
            elif grid[y][x] == "~":
                still += 1

    return still + flowing, still


all, still = solve(data)
# pt 1
print(all)
# pt 2
print(still)

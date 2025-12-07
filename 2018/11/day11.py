#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day11 2018
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    SERIAL = [int(x) for x in f.read().splitlines()][0]


def build_grid(size):
    return {(x, y): 0 for x in range(1, size + 1) for y in range(1, size + 1)}


def find_power(cell):
    x, y = cell
    rack_id = x + 10
    return int(str((rack_id * y + SERIAL) * rack_id)[-3]) - 5


def area(coord, grid, size):
    tot = 0
    x, y = coord
    for j in range(y, y + size):
        for i in range(x, x + size):
            tot += grid[(i, j)]
    return tot


def max_squares(grid, size):
    squares = {}
    g_max = max(grid, key=lambda i: i)[0]
    limit = g_max - size + 1
    for y in range(1, limit):
        for x in range(1, limit):
            squares[(x, y, size)] = area((x, y), grid, size)
    max_square = max(squares, key=lambda i: squares[i])
    return max_square, squares[max_square]


def max_variable_squares(grid):
    iteration = {}
    for size in range(12, 16):
        idx, val = max_squares(grid, size)
        iteration[idx] = val
    return max(iteration, key=lambda i: iteration[i])


grid = build_grid(300)
for cell in grid:
    grid[cell] = find_power(cell)
# pt1
idx, val = max_squares(grid, 3)
x, y, size = idx
print(",".join(str(x) for x in [x, y]))
# pt 2
res = max_variable_squares(grid)
print(",".join(str(x) for x in res))

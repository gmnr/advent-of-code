#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day08 2022
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc

data = aoc.read_input()


def parse(data):
    return [tuple(map(int, tuple(x))) for x in data]


def get_col(x, grid):
    col = []
    for line in grid:
        col.append(line[x])
    return col


def is_visible(coord, grid):
    x, y = coord
    dirs = []

    val = grid[y][x]
    col = get_col(x, grid)
    row = grid[y]

    if x == 0 or y == 0 or x == len(col) - 1 or y == len(row) - 1:
        dirs.append(True)

    for i in range(0, x):
        r = row[i]
        if r >= val:
            dirs.append(False)
            break
    else:
        dirs.append(True)

    for i in range(len(row) - 1, x, -1):
        r = row[i]
        if r >= val:
            dirs.append(False)
            break
    else:
        dirs.append(True)

    for i in range(0, y):
        c = col[i]
        if c >= val:
            dirs.append(False)
            break
    else:
        dirs.append(True)

    for i in range(len(col) - 1, y, -1):
        c = col[i]
        if c >= val:
            dirs.append(False)
            break
    else:
        dirs.append(True)

    return any(dirs)


def count_visible(grid):
    visible = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            coord = (x, y)
            if is_visible(coord, grid):
                visible.append(coord)
    return len(visible)


def scenic_score(coord, grid):
    x, y = coord

    val = grid[y][x]
    col = get_col(x, grid)
    row = grid[y]

    up = 0
    for i in range(y - 1, -1, -1):
        v = col[i]
        up += 1
        if v >= val:
            break

    right = 0
    for i in range(x + 1, len(row)):
        v = row[i]
        right += 1
        if v >= val:
            break

    down = 0
    for i in range(y + 1, len(col)):
        v = col[i]
        down += 1
        if v >= val:
            break

    left = 0
    for i in range(x - 1, -1, -1):
        v = row[i]
        left += 1
        if v >= val:
            break

    return up * right * down * left


def calculate_score(grid):
    score = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            score.append(scenic_score((x, y), grid))
    return max(score)


# pt 1
grid = parse(data)
print(count_visible(grid))

# pt 2
print(calculate_score(grid))

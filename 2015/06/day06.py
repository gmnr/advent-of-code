#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day06 2015
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from itertools import chain
from copy import deepcopy

grid = [[0 for x in range(1000)] for y in range(1000)]
new_grid = deepcopy(grid)


def light(fy, fx, sy, sx, op, grid):
    for y in range(fy, sy + 1):
        for x in range(fx, sx + 1):
            if op == "on":
                grid[y][x] = 1
            elif op == "off":
                grid[y][x] = 0
            else:
                grid[y][x] = int(not grid[y][x])
    return grid


def new_light(fy, fx, sy, sx, op, grid):
    for y in range(fy, sy + 1):
        for x in range(fx, sx + 1):
            if op == "on":
                grid[y][x] += 1
            elif op == "off":
                if grid[y][x] == 0:
                    continue
                else:
                    grid[y][x] -= 1
            else:
                grid[y][x] += 2
    return grid


def parse_input(line):
    line = line.split()
    if len(line) == 5:
        _, stat, first, _, second = line
    else:
        stat, first, _, second = line
    return stat, [int(x) for x in first.split(",")], [int(x) for x in second.split(",")]


def count_lights(grid):
    tot = list(chain.from_iterable(grid))
    return sum(tot)


# pt 1
for line in data:
    stat, first, second = parse_input(line)
    grid = light(*first, *second, stat, grid)
print(count_lights(grid))
# pt 2
for line in data:
    stat, first, second = parse_input(line)
    new_grid = new_light(*first, *second, stat, new_grid)
print(count_lights(new_grid))

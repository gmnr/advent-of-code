#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 17 2020
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from operator import itemgetter
from itertools import product


def limits(space, n_dim):
    for i in range(n_dim):
        low = min(map(itemgetter(i), space)) - 1
        high = max(map(itemgetter(i), space)) + 2
        yield range(low, high)


def alive_neighbors(space, coords):
    ranges = ((c - 1, c, c + 1) for c in coords)
    alive = sum(p in space for p in product(*ranges))
    alive -= coords in space
    return alive


def step(space, n_dim):
    new_space = set()
    for coords in product(*limits(space, n_dim)):
        alive = alive_neighbors(space, coords)
        if (coords in space and alive in [2, 3]) or alive == 3:
            new_space.add(coords)
    return new_space


space = set()
for (
    y,
    row,
) in enumerate(data):
    for x, cell in enumerate(row):
        if cell == "#":
            space.add((x, y, 0))
for _ in range(6):
    space = step(space, 3)
print(len(space))

fourth_dimension = set()
for y, row in enumerate(data):
    for x, cell in enumerate(row):
        if cell == "#":
            fourth_dimension.add((x, y, 0, 0))
for _ in range(6):
    fourth_dimension = step(fourth_dimension, 4)
print(len(fourth_dimension))

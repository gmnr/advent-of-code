#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day06 2024
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from itertools import cycle

data = aoc.read_input()

coord = {}
guard = (0, 0)
for y, line in enumerate(data):
    for x, c in enumerate(line):
        coord[(x, y)] = c
        if c == "^":
            guard = (x, y)


def patrol(pos, coord):
    visited = {pos: None}

    DIRS = {"^": (0, -1), ">": (1, 0), "<": (-1, 0), "v": (0, 1)}
    turns = cycle(["^", ">", "v", "<"])

    for d in turns:

        new_pos = tuple(map(sum, zip(pos, DIRS[d])))

        while coord[new_pos] != "#":

            visited[new_pos] = None
            pos = new_pos
            new_pos = tuple(map(sum, zip(pos, DIRS[d])))

            if new_pos not in coord:
                return visited
    return visited


def looped(pos, coord):
    visited = {(pos, "^"): None}

    DIRS = {"^": (0, -1), ">": (1, 0), "<": (-1, 0), "v": (0, 1)}
    turns = cycle(["^", ">", "v", "<"])

    for d in turns:

        new_pos = tuple(map(sum, zip(pos, DIRS[d])))

        if (new_pos, d) in visited.keys():
            return True

        while coord[new_pos] != "#":

            visited[(new_pos, d)] = None
            pos = new_pos
            new_pos = tuple(map(sum, zip(pos, DIRS[d])))

            if new_pos not in coord:
                return False


# pt 1
visited = patrol(guard, coord)
print(len(visited.keys()))

# pt 2
loops = 0
for i, p in enumerate(visited.keys()):
    if i == 0:
        continue

    trial = dict(coord)
    trial[p] = "#"

    if looped(guard, trial):
        loops += 1
print(loops)

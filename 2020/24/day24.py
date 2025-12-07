#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day24 2020
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from operator import add, itemgetter
from collections import Counter
from itertools import product
import re

dirs = {
    "e": (2, 0),
    "ne": (1, 1),
    "se": (1, -1),
    "w": (-2, 0),
    "sw": (-1, -1),
    "nw": (-1, 1),
}


def parse_instr(line):
    regex = r"ne|e|nw|w|sw|se"
    return re.findall(regex, line)


def move(start, instr):
    for inst in parse_instr(instr):
        start = tuple(map(add, start, dirs[inst]))
    return start


def hex_neigh(tiles, coord):
    inter = [tuple(map(add, coord, dirs[c])) for c in dirs]
    return len([x for x in inter if x in tiles])


def limits(tiles):
    low_x = min(map(itemgetter(0), tiles)) - 1
    low_y = min(map(itemgetter(1), tiles)) - 1
    high_x = max(map(itemgetter(0), tiles)) + 2
    high_y = max(map(itemgetter(1), tiles)) + 2
    return range(low_x, high_x), range(low_y, high_y)


def evolve(tiles):
    new_tiles = set()
    for p in product(*limits(tiles)):
        neigh = hex_neigh(tiles, p)
        if p in tiles and not (neigh == 0 or neigh > 2):
            new_tiles.add(p)
        elif p not in tiles and neigh == 2:
            new_tiles.add(p)
    return new_tiles


# pt 1
tiles = []
for i in data:
    tiles.append(move((0, 0), i))
black_tiles = [k for k, v in Counter(tiles).items() if v % 2 != 0]
print(len(black_tiles))
# pt 2
tiles = set(black_tiles)
for _ in range(100):
    tiles = evolve(tiles)
print(len(tiles))

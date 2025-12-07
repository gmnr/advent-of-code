#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 14 2017
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()[0]

from collections import deque as dq
from itertools import islice as isl
from functools import reduce


# imported (manually) from day 10 2017 solution
def hash_knot(string):
    rope = dq([x for x in range(256)])
    c = 0
    skip = 0
    inst = [ord(x) for x in string]
    inst += [17, 31, 73, 47, 23]

    for _ in range(64):
        for l in inst:
            rope.rotate(-c)
            sel = list(isl(rope, l))
            rest = list(isl(rope, l, len(rope)))
            sel = sel[::-1]
            rope = dq(sel + rest)
            rope.rotate(c)
            c += l + skip
            skip += 1
    res = list(rope)
    chunks = [res[i : i + 16] for i in range(0, len(res), 16)]
    msg = [hex(reduce(lambda x, y: x ^ y, ch)) for ch in chunks]
    return "".join([x[2:].zfill(2) for x in msg])


def convert_to_bit(ch):
    return format(int(ch, 16), "04b")


def build(string):
    grid = []
    for row in range(128):
        msg = string + "-" + str(row)
        hx = hash_knot(msg)
        s = ""
        for h in hx:
            s += convert_to_bit(h)
        grid.append(s)
    return grid


# pt1
mesh = build(data)
print(len([x for x in "".join(mesh) if x == "1"]))


# pt2
def wrap(grid):
    new_grid = []
    new_grid.insert(0, ["0"] * 130)
    for el in grid:
        el = "0" + el + "0"
        new_grid.append(list(el))
    new_grid.append(["0"] * 130)
    return new_grid


def neighbors(point):
    x, y = point
    return ((x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1))


def flood(grid, x, y, val, R):
    if grid[y][x] == val:
        grid[y][x] = R
        for x2, y2 in neighbors((x, y)):
            flood(grid, x2, y2, val, R)


def flood_all(grid, val="1"):
    R = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid) - 1):
            if grid[y][x] == val:
                R += 1
                flood(grid, x, y, val, R)
    return R


grid = wrap(mesh)
print(flood_all(grid))

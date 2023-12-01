#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 18 2015
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import defaultdict as dd


def build_coord(data):
    coord = dd(lambda: "x")
    for y in range(len(data)):
        for x in range(len(data[y])):
            coord[(x, y)] = data[y][x]
    return coord


def check_occ(coord, coords):
    x, y = coord
    neigh = (
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x + 1, y + 1),
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
    )
    cnt_occ = 0
    for c in neigh:
        if coords[c] == "#":
            cnt_occ += 1
    return cnt_occ


anim = build_coord(data)
fix = build_coord(data)
coord = list(anim.keys())


def compute1(coord, iters):
    anim = coord
    for _ in range(iters):
        old_anim = anim.copy()
        for c in coord:
            if old_anim[c] == "#":
                if check_occ(c, old_anim) in [2, 3]:
                    continue
                else:
                    anim[c] = "."
            elif old_anim[c] == ".":
                if check_occ(c, old_anim) == 3:
                    anim[c] = "#"
                else:
                    continue
    return len([x for x in anim.values() if x == "#"])


def compute2(coord, iters, fixed):
    anim = coord
    for _ in range(iters):
        old_anim = anim.copy()
        for c in coord:
            if c in fixed:
                continue
            if old_anim[c] == "#":
                if check_occ(c, old_anim) in [2, 3]:
                    continue
                else:
                    anim[c] = "."
            elif old_anim[c] == ".":
                if check_occ(c, old_anim) == 3:
                    anim[c] = "#"
                else:
                    continue
    return len([x for x in anim.values() if x == "#"])


def fix_corners(data, coord):
    l = len(data) - 1
    r = len(data[0]) - 1
    fixed = [(0, 0), (0, l), (r, 0), (r, l)]
    for i in fixed:
        coord[i] = "#"
    return fixed


# pt 1
print(compute1(anim, 100))
# pt 2
fixed = fix_corners(data, fix)
print(compute2(fix, 100, fixed))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day22 2021
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

import re
from itertools import product
from collections import Counter


def parse(data):
    regex = r"-?\d+"
    instr = []
    for line in data:
        match = re.findall(regex, line)
        ax, ay, bx, by, cx, cy = map(int, match)
        switch, *_ = line.split()
        instr.append((switch, ax, ay, bx, by, cx, cy))
    return instr


def calc_area(coord):
    ax, ay, bx, by, cx, cy = coord
    yield product(range(ax, ay + 1), range(bx, by + 1), range(cx, cy + 1))


def reboot(instr):
    cuboid = set()
    for i in instr:
        switch, *coord = i
        for c in calc_area(coord):
            if switch.startswith("on"):
                cuboid |= set(c)
            else:
                cuboid -= set(c)
    return cuboid


def all_reboot(instr):
    cuboid = Counter()
    for i in instr:
        switch, ax, ay, bx, by, cx, cy = i
        switch = 1 if switch == "on" else 0

        update = Counter()
        for (ex0, ex1, ey0, ey1, ez0, ez1), esgn in cuboid.items():
            ix0 = max(ax, ex0)
            ix1 = min(ay, ex1)
            iy0 = max(bx, ey0)
            iy1 = min(by, ey1)
            iz0 = max(cx, ez0)
            iz1 = min(cy, ez1)
            if ix0 <= ix1 and iy0 <= iy1 and iz0 <= iz1:
                update[(ix0, ix1, iy0, iy1, iz0, iz1)] -= esgn
        if switch > 0:
            update[(ax, ay, bx, by, cx, cy)] += switch
        cuboid.update(update)
    return cuboid


instr = parse(data)
# pt 1
procedure_area = instr[:20]
print(len(reboot(procedure_area)))

# pt 2
cubes = all_reboot(instr)
print(
    sum(
        (ay - ax + 1) * (by - bx + 1) * (cy - cx + 1) * sgn
        for (ax, ay, bx, by, cx, cy), sgn in cubes.items()
    )
)

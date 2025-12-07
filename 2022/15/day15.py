#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day15 2022
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc

scan = [[(sx, sy), (bx, by)] for sx, sy, bx, by in aoc.read_input(parser=aoc.ints)]
beacons = set([x[1] for x in scan])


def diamond(scan, beacon, target):
    d = aoc.manhattan_dist(scan, beacon)
    sx, sy = scan

    if target not in range(sy - d, sy + d + 1):
        return []

    if sy <= target:
        delta = sy + d - target
    else:
        delta = target - (sy - d)

    delta = abs(delta)
    return sx - delta, sx + delta


def frequency(p):
    px, py = p
    return px * 4_000_000 + py


def compose(ranges, lim):
    x, y = None, None
    ranges = sorted(ranges)
    for i, c in enumerate(ranges):
        cx, cy = c
        if i == 0:
            x, y = c

        if cx <= y:
            if cy >= y:
                y = cy
        else:
            return cx - 1

        if x <= 0 and y >= lim:
            return x, y


# pt 1
target = 10
diamonds = []
for s in scan:
    scanner, beacon = s
    diamonds.extend(diamond(scanner, beacon, target))
diamonds = [x for x in diamonds if x != []]
beacons_on_line = len([x for x in beacons if x[1] == target])
print(len(range(min(diamonds), max(diamonds) + 1)) - beacons_on_line)

# pt 2
lim = 4_000_000
for y in range(lim + 1):
    ranges = []
    for s in scan:
        scanner, beacon = s
        new = diamond(scanner, beacon, y)
        if new:
            ranges.append(new)
    if isinstance(compose(ranges, lim), tuple):
        continue
    else:
        p = (compose(ranges, lim), y)
        break
print(frequency(p))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day10 2018
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

import re
from collections import namedtuple
from operator import add, sub


def parse(data):
    points = []
    for line in data:
        pos, vel = re.findall(r"<(.+?)>", line)
        pos = tuple([int(x) for x in pos.split(", ")])
        vel = tuple([int(x) for x in vel.split(", ")])
        points.append((pos, vel))
    return points


def apply(pos, vel, subtract=False):
    if subtract:
        return tuple(map(sub, pos, vel))
    else:
        return tuple(map(add, pos, vel))


def box_size(points):
    coords = [x[0] for x in points]
    max_x = max(p[0] for p in coords)
    max_y = max(p[1] for p in coords)
    min_x = min(p[0] for p in coords)
    min_y = min(p[1] for p in coords)
    return max_x - min_x + max_y - min_y


def move_points(points, iterations=12_000):
    size = {}
    for it in range(1, iterations):
        new_points = []
        for i in points:
            new_pos = apply(i[0], i[1])
            new_points.append((new_pos, i[1]))
        points = new_points
        size[it] = [box_size(points), points]
    min_size = min(size, key=lambda x: size[x][0])
    return min_size, show(size[min_size][1])


def show(points):
    coords = [x[0] for x in points]
    min_x = min(p[0] for p in coords)
    min_y = min(p[1] for p in coords)

    trasl_x = (min_x, 0)
    trasl_y = (0, min_y)
    wip = [apply(i, trasl_x, True) for i in coords]
    coords = [apply(i, trasl_y, True) for i in wip]

    max_x = max(p[0] for p in coords)
    max_y = max(p[1] for p in coords)
    empty = [[" "] * (max_x + 1) for y in range(max_y + 1)]

    for y in range(len(empty)):
        for x in range(len(empty[0]) + 1):
            if (x, y) in coords:
                empty[y][x] = "*"
    for m in empty:
        print("".join(m))


points = parse(data)
# pt1
iteration, _ = move_points(points)
# pt2
print(iteration)

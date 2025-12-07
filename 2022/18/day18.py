#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day18 2022
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from collections import deque
from itertools import combinations, product

cubes = aoc.read_input(parser=aoc.ints)


def count_faces(data):
    tot = len(data) * 6

    for a, b in combinations(data, 2):
        if sum(abs(x - y) for x, y in zip(a, b)) == 1:
            tot -= 2

    return tot


def neighbors(x, y, z):
    yield (x + 1, y, z)
    yield (x - 1, y, z)
    yield (x, y + 1, z)
    yield (x, y - 1, z)
    yield (x, y, z + 1)
    yield (x, y, z - 1)


def out_of_bounds(cubes, src, rangex, rangey, rangez):
    seen = set()
    queue = deque([src])
    faces = 0

    while queue:
        p = queue.pop()
        if p in seen:
            continue

        seen.add(p)
        x, y, z = p

        if x not in rangex or y not in rangey or z not in rangez:
            return 0, seen

        for n in neighbors(x, y, z):
            if n in cubes:
                faces += 1
            else:
                if n not in seen:
                    queue.append(n)

    return faces, seen


# pt 1
surface = count_faces(cubes)
print(surface)

# pt 2
minx = miny = minz = 999
maxx = maxy = maxz = 0

for x, y, z in cubes:
    minx, maxx = min(x, minx), max(x, maxx)
    miny, maxy = min(y, miny), max(y, maxy)
    minz, maxz = min(z, minz), max(z, maxz)

rangex = range(minx, maxx + 1)
rangey = range(miny, maxy + 1)
rangez = range(minz, maxz + 1)

allseen = set()

for c in product(rangex, rangey, rangez):
    if c not in cubes:
        if c not in allseen:
            touch, seen = out_of_bounds(cubes, c, rangex, rangey, rangez)
            surface -= touch
            allseen |= seen
print(surface)

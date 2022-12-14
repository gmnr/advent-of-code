#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day14 2022
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


import helper.advent as aoc

data = aoc.read_input()

def parse(data):
    cave = set()
    for l in data:
        rocks = list(map(aoc.ints, l.split(' -> ')))
        for i in range(len(rocks)-1):
            for c in gen_rocks(rocks[i], rocks[i+1]):
                cave.add(c)
    return cave

def gen_rocks(a, b):
    s = sorted([a, b])
    xa, ya = s[0]
    xb, yb = s[1]
    if xa == xb:
        for n in range(ya, yb+1):
            yield (xa, n)
    else:
        for n in range(xa, xb+1):
            yield (n, ya)

def bounds(cave):
    cave.add((500, 0))
    bounds = set()

    min_x = min(cave, key=lambda x: x[0])[0]
    max_x = max(cave, key=lambda x: x[0])[0]
    min_y = min(cave, key=lambda x: x[1])[1]
    max_y = max(cave, key=lambda x: x[1])[1]

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            bounds.add((x, y))

    return bounds

def fall(cave, set_sand, bounds):
    x, y = (500, 0)
    blocked = {*cave, *set_sand}

    while True:
        x, y = x, y+1

        if (x, y) in blocked:
            x, y = x-1, y

            if (x, y) in blocked:
                x, y = x+2, y

                if (x, y) in blocked:
                    return x-1, y-1

        if (x, y) not in bounds:
            return False

# pt 1
cave = parse(data)
set_sand = set()
bound = bounds(cave)

while True: 
    grain = fall(cave, set_sand, bound)
    if grain == False:
        break
    set_sand.add(grain)

print(len(set_sand))

# pt 2
floor = max(cave, key=lambda x: x[1])[1] + 2
floor_len = 2 * floor + 1

for x in range(500-floor, 500+floor+1):
    cave.add((x, floor))

set_sand = set()
bound = bounds(cave)

while True: 
    grain = fall(cave, set_sand, bound)
    if grain == False or grain == (500, 0):
        break
    set_sand.add(grain)

print(len(set_sand)+1)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day12 2022
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from string import ascii_lowercase as ascii

data = aoc.read_input()
area = [[ascii.find(i) if x not in ["S", "E"] else i for i in x] for x in data]

for y, l in enumerate(data):
    for x, i in enumerate(l):
        if i == "S":
            start = (x, y)
        elif i == "E":
            end = (x, y)


def gen_height(area, node):
    coord = aoc.gen_coordinates(node)

    max_y = len(area) - 1
    max_x = len(area[0]) - 1

    nx, ny = node
    node_value = abs(area[ny][nx])

    for c in coord:
        cx, cy = c

        if (cx < 0 or cy < 0) or (cy > max_y or cx > max_x):
            continue

        c_value = abs(area[cy][cx])

        if c_value == "E":
            yield c

        if c_value - node_value > 1:
            continue

        yield c


def traverse(area, start, end):
    queue = [(0, start)]
    visited = set()

    while queue:
        dist, node = queue.pop(0)

        if node == end:
            return dist

        if node not in visited:
            visited.add(node)

            for n in gen_height(area, node):
                if n in visited:
                    continue

                queue.append((dist + 1, n))


# pt 1
print(traverse(area, start, end))

# pt 2
all_a = []
for y, l in enumerate(data):
    for x, i in enumerate(l):
        if i == "a":
            all_a.append((x, y))

all_dist = [traverse(area, x, end) for x in all_a]
print(min([x for x in all_dist if x != None]))

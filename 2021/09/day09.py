#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day09 2021
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

from math import prod

def parse(data):
    caves = {}

    for y, line in enumerate(data):
        for x, heat in enumerate(line):
            caves[(x, y)] = int(heat)

    return caves

def nb4(pt):
    x, y = pt
    return [(x+dx, y+dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]] 

def find_low(caves):
    low_points = {}
    for c, c_v in caves.items():
        nb = nb4(c)
        heats = []
        for n in nb:
            if n not in caves:
                continue
            heats.append(caves[n])
        if c_v < min(heats):
            low_points[c] = c_v
    return low_points

def spill(c, caves):
    visited = [c]
    queue = [c]

    while queue:
        m = queue.pop(0)

        for neigh in nb4(m):
            if neigh not in caves:
                continue
            elif neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)
    return visited

def spill_basins(caves, low_points):
    caves = {k: v for k, v in caves.items() if v != 9}
    basins_size = []
    for c in low_points.keys():
        basin = spill(c, caves)
        basins_size.append(len(basin))
    return basins_size

caves = parse(data)
# pt 1
low_points = find_low(caves)
print(sum(x + 1 for x in low_points.values()))
# pt 2
basins = spill_basins(caves, low_points)
print(prod(sorted(basins)[-3:]))

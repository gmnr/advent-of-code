#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day18 2024
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc

data = aoc.read_input()
corrupted = [aoc.ints(x) for x in data]

kylo_corrupted = set(corrupted[:1024])

start = (0, 0)
end = (70, 70)

grid = set()
for y in range(71):
    for x in range(71):
        grid.add((x, y))


# pt 1
path = grid - kylo_corrupted
prev, cost = aoc.astar(start, end, path)
print(cost[end])

# pt 2
for i in range(1024, len(corrupted)):
    obstacles = set(corrupted[:i])
    path = grid - obstacles

    prev, cost = aoc.astar(start, end, path)
    if end not in cost:
        print(",".join([str(x) for x in corrupted[i - 1]]))
        break

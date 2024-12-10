#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day10 2024
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc

data = aoc.read_input()

map = {}
starts = []
ends = []
for y, line in enumerate(data):
    for x, c in enumerate(line):
        map[(x, y)] = int(c)
        if c == "0":
            starts.append((x, y))
        if c == "9":
            ends.append((x, y))


def is_reachable(map, start, end, path=[]):
    path += [start]

    if start == end:
        paths.append(path)
    for n in aoc.gen_coordinates(start):
        if n in map:
            if map[n] - map[start] == 1:
                is_reachable(map, n, end, path)


# pt 1 & 2
trails = 0
rating = 0
for s, e in [(s, e) for s in starts for e in ends]:
    paths = []
    is_reachable(map, s, e)
    if paths:
        trails += 1
        rating += len(paths)
print(trails)
print(rating)

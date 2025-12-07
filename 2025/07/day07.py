#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day07 2025
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from collections import Counter

data = aoc.read_input()

# pt 1
vert = set([data[0].find("S")])
cnt = 0
for line in data[1:]:
    new_vert = set()
    for v in vert:
        if line[v] == "^":
            new_vert.update([v + 1, v - 1])
            cnt += 1
        else:
            new_vert.add(v)
    vert = new_vert
print(cnt)

# pt 2
paths = Counter({data[0].find("S"): 1})
for line in data[1:]:
    for b, n in list(paths.items()):
        if line[b] == "^":
            paths[b] = 0
            paths[b - 1] += n
            paths[b + 1] += n
print(sum(paths.values()))

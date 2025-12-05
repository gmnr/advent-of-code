#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day05 2025
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc

data = aoc.read_input(sep="\n\n")

fresh_list = data[0].splitlines()
available = [int(x) for x in data[1].splitlines()]

# pt 1
fresh_range = []
for r in fresh_list:
    a, b = r.split("-")
    fresh_range.append(range(int(a), int(b) + 1))

fresh = 0
for a in available:
    for r in fresh_range:
        if a in r:
            fresh += 1
            break
print(fresh)

# pt 2
ranges = []
for ran in data[0].splitlines():
    a, b = ran.split("-")
    ranges.append((int(a), int(b)))

elem = 0
pos = 0
for a, b in sorted(ranges):
    new_pos = max(pos, b)
    if a <= pos:
        elem += new_pos - pos
    else:
        elem += b - a + 1
    pos = new_pos
print(elem)

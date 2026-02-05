#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day20 2016
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc

data = aoc.read_input()

lowest = []
ranges = []
for r in data:
    a, b = r.split("-")
    a, b = int(a), int(b)

    if (l := a - 1) > 0:
        lowest.append(l)

    ranges.append((a, b))

valid = []
for l in lowest:
    for r in ranges:
        a, b = r

        if l < a or l > b:
            continue
        else:
            break
    else:
        valid.append(l)

# pt1
print(min(valid))

# pt2
print(len(valid))

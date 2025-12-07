#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day15 2016
"""

__author__ = "gmnr"
__license__ = "GPL"


from helper import advent as aoc

data = aoc.read_input()

discs = []
for x in data:
    disc, pos, _, start = aoc.ints(x)
    discs.append((pos, start + disc))


def solve():
    t = 0
    while True:
        res = []
        for d in discs:
            ratio = d[0]
            pos = d[1] + t
            res.append(pos % ratio)
        if res == [0] * len(discs):
            return t
        t += 1


# pt 1
print(solve())

# pt 2
discs.append((11, 7))
print(solve())

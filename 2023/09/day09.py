#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day09 2023
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc

data = aoc.read_input()

# pt 1 & 2
vals = []
neg_vals = []

for line in data:
    seq = aoc.ints(line)
    deltas = [seq]
    while True:
        s = []
        d = deltas[-1]
        if set(d) == {0}:
            c = 0
            neg_c = 0
            for x in range(len(deltas) - 1, 0, -1):
                c += deltas[x][-1]
                neg_c = deltas[x][0] - neg_c
            vals.append(deltas[0][-1] + c)
            neg_vals.append(deltas[0][0] - neg_c)
            break
        for i in range(len(deltas[-1]) - 1):
            s.append(d[i + 1] - d[i])
        deltas.append(s)
print(sum(vals))
print(sum(neg_vals))

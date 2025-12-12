#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day12 2025
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from math import prod


data = aoc.read_input(sep='\n\n')

shapes, grids = data[:-1], data[-1]
shapes = [x.count('#') for x in shapes]

cnt = 0
for grid in grids.splitlines():
    size, *idx = grid.split()
    size = prod(int(x) for x in size[:-1].split('x'))

    space = 0
    for i in range(len(idx)):
        space += shapes[i] * int(idx[i])

    if size >= space:
        cnt += 1
print(cnt)

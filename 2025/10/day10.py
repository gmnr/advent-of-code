#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day10 2025
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from itertools import combinations

data = aoc.read_input()

presses = 0
for line in data:
    diagram, *schematics, requirements = line.split()

    diagram = [int(x == '#') for x in diagram[1:-1]]
    schematics = [aoc.ints(x) for x in schematics]

    stop = False
    for l in range(1, len(diagram)):

        if stop:
            stop = False
            break

        for p in combinations(schematics, l):
            start = [ 0 ] * len(diagram)

            for b in  p:

                for led in b:
                    start[led] += 1

            start = [x % 2 for x in start]

            if start == diagram:
                presses += l
                stop = True
                break
print(presses)

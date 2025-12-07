#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day19 2016
"""

__author__ = "gmnr"
__license__ = "GPL"


from helper import advent as aoc
from collections import deque

data = aoc.first(aoc.read_input(parser=int))

# pt 1
elves = deque([x for x in range(1, data + 1)])
while len(elves) > 1:
    elves.rotate(-1)
    elves.popleft()
print(aoc.first(elves))

# pt 2
elves = deque([x for x in range(1, data + 1)])
opposite = len(elves) // 2
elves.rotate(-opposite)
while len(elves) > 1:
    elves.popleft()
    old = opposite
    opposite = len(elves) // 2
    rotate_amount = old - opposite
    elves.rotate(rotate_amount - 1)
print(aoc.first(elves))

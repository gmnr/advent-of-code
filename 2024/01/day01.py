#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day01 2024
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from collections import Counter

data = aoc.read_input()

# pt 1
left = []
right = []
for pair in data:
    x1, x2 = pair.split()
    left.append(int(x1))
    right.append(int(x2))

left = sorted(left)
right = sorted(right)
together = zip(left, right)
print(sum((abs(x - y) for x, y in together)))

# pt 2
mult = Counter(right)

cnt = 0
for x in left:
    try:
        cnt += x * mult[x]
    except:
        pass
print(cnt)

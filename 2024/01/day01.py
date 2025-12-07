#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day01 2024
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from collections import Counter

data = aoc.read_input()

# pt 1
left, right = [], []
for pair in data:
    l, r = map(int, pair.split())
    left.append(l)
    right.append(r)

left.sort()
right.sort()
print(sum((abs(l - r) for l, r in zip(left, right))))

# pt 2
mult = Counter(right)

cnt = 0
for x in left:
    try:
        cnt += x * mult[x]
    except:
        pass
print(cnt)

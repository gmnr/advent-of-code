#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day03 2016
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


from helper import advent as aoc
from itertools import combinations, chain

data = aoc.read_input(parser=aoc.ints)

def check_triangle(triangle):
    combs = combinations(triangle, 2)
    largest = max(triangle)
    if all([sum(x) > largest for x in combs]):
        return True
    return False

# pt 1
cnt = 0
for triangle in data:
    if check_triangle(triangle):
        cnt += 1
print(cnt)

# pt 2
transposed_data = list(chain.from_iterable(aoc.transpose(data)))
cnt = 0
for i in range(0, len(transposed_data), 3):
    triangle = transposed_data[i:i+3]
    if check_triangle(triangle):
        cnt += 1
print(cnt)

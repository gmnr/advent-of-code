#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day24 2021
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

stack = []
upper = 99999999999999
lower = 11111111111111

for i in range(14):
    a = int(data[18 * i + 5].split()[-1])
    b = int(data[18 * i + 15].split()[-1])

    if a > 0:
        stack += [(i, b)]
        continue

    j, b = stack.pop()

    upper -= abs((a + b) * 10 ** (13 - [i, j][a > -b]))
    lower += abs((a + b) * 10 ** (13 - [i, j][a < -b]))

# pt 1
print(upper)

# pt 2
print(lower)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day25 2015
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().strip()

import re

row = int(re.search(r'row (\d+)', data).group(1))
column = int(re.search(r'column (\d+)', data).group(1))

code = 20151125

def get_next(v):
    return v * 252533 % 33554393

def nth_iteration(row, column):
    corner = sum_corner(row + column)
    # n_elems = row + column - 1
    if row == 1:
        return corner
    else:
        return corner - row

def sum_corner(val):
    return sum(i for i in range(1, val))

# pt1
iterations = nth_iteration(row, column)
for _ in range(iterations):
    code = get_next(code)
print(code)

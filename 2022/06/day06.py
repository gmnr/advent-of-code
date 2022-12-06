#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day06 2022
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


import helper.advent as aoc

data = aoc.read_input()[0]

def find_marker(data, end):
    for n in range(len(data)):
        s = data[n:n+end]
        if len(set(s)) == end:
            return n + end

# pt 1
print(find_marker(data, 4))

# pt 2
print(find_marker(data, 14))

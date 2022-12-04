#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day04 2022
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


import helper.advent as aoc

data = aoc.read_input()

def pair_ranges(data):
    contained = 0
    overlap = 0
    for i in data:
        p1, p2 = i.split(',')

        p1_l, p1_u = map(int, p1.split('-'))
        p2_l, p2_u = map(int, p2.split('-'))

        r1 = range(p1_l, p1_u + 1)
        r2 = range(p2_l, p2_u + 1)

        if r1.start <= r2.start and r1.stop >= r2.stop:
            contained += 1
            overlap += 1
        elif r2.start <= r1.start and r2.stop >= r1.stop:
            contained += 1
            overlap += 1
        elif r1.start < r2.stop and r2.start < r1.stop:
            overlap += 1

    return contained, overlap

contained, overlap = pair_ranges(data)

# pt 1
print(contained)

# pt 2
print(overlap)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day01 2016
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


from helper import advent as aoc
from collections import deque

data = aoc.read_input(sep=', ')

def manhattan(a, b):
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)

def find_bunny(instr):
    cardinal = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
    fx = 0
    fy = 0
    destinations = []

    for i in instr:
        dir, amt = i[0], i[1:]
        amt = int(amt)

        if dir == 'R':
            cardinal.rotate(1)
        else:
            cardinal.rotate(-1)

        d = cardinal[0]
        dx, dy = d

        for _ in range(amt):
            fx += dx
            fy += dy
            destinations.append((fx, fy))

    return (fx, fy), destinations

# pt 1
destination, destinations = find_bunny(data)
print(manhattan((0, 0), destination))

# pt 2
seen = []
first = True
for i in destinations:
    if i in seen:
        recurrent = i
        break
    seen.append(i)

print(manhattan((0, 0), recurrent))

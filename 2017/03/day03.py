#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 03 2017
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = int(f.read().rstrip())

from collections import defaultdict

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

def neighboor(point):
    "The eight neighbors (with diagonals)."
    x = point.x
    y = point.y
    return ((x+1, y), (x-1, y), (x, y+1), (x, y-1),
            (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1))

def distance(p, q=(0, 0)):
    return abs(p.x - q[0]) + abs(p.y - q[1])

def spiral(part_b=False):
    matrix = defaultdict(int)
    facing = Point(1, 0)
    pos = Point(0, 0)

    stepped = 0
    max_step = 1
    turn_count = 0
    num = 0


    while True:
        if part_b:
            num = sum(matrix[n[0], n[1]] for n in neighboor(pos))
            if num == 0:
                num = 1
        else:
            num += 1

        matrix[pos.x, pos.y] = num
        yield (pos, num)

        pos = Point(pos.x + facing.x, pos.y + facing.y)
        stepped += 1

        if stepped >= max_step:
            stepped = 0
            turn_count += 1
            if turn_count == 2:
                max_step += 1
                turn_count = 0
            facing = Point(facing.y, -facing.x)

# pt 1
print(next(distance(pos) for (pos, val) in spiral() if val == data))
# pt 2
print(next(val for (pos, val) in spiral(part_b=True) if val > data))

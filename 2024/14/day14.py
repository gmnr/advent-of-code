#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day14 2024
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc

data = aoc.read_input(parser=aoc.ints)

X, Y = 101, 103
# pt 1
robots = []
cycles = 100
for r in data:
    x, y, vx, vy = r
    new_x = (x + vx * cycles) % X
    new_y = (y + vy * cycles) % Y
    robots.append((new_x, new_y))

midx = X // 2
midy = Y // 2

q1 = [x for x in robots if x[0] < midx and x[1] < midy]
q2 = [x for x in robots if x[0] > midx and x[1] < midy]
q3 = [x for x in robots if x[0] < midx and x[1] > midy]
q4 = [x for x in robots if x[0] > midx and x[1] > midy]
print(len(q1) * len(q2) * len(q3) * len(q4))


# pt 2
def visual(r):
    for y in range(Y):
        s = ""
        for x in range(X):
            if (x, y) in robots:
                s += "#"
            else:
                s += " "
        print(s)


cycles = 6870
print(cycles)
robots = []
for r in data:
    x, y, vx, vy = r
    new_x = (x + vx * cycles) % X
    new_y = (y + vy * cycles) % Y
    robots.append((new_x, new_y))
visual(robots)

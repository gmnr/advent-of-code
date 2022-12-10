#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day09 2022
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


import helper.advent as aoc
from math import dist

data = aoc.read_input()

def approach(c1, c2):
    x1, y1 = c1
    x2, y2 = c2

    if x1 == x2:
        if y1 > y2:
            return (x2, y2 + 1)
        else:
            return (x2, y2 - 1)

    elif y1 == y2:
        if x1 > x2:
            return (x2 + 1, y2)
        else:
            return (x2 - 1, y2)

    elif abs((y1 - y2) / (x1 - x2)) == float(1):
        cross = [(x1 + dx, y1 + dy) for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
        d = [dist(i, c2) for i in cross]
        points = list(zip(cross, d))
        return  min(points, key=lambda x: x[1])[0]

    else:
        adj = list(aoc.gen_coordinates(c1))
        d = [dist(i, c2) for i in adj]
        points = list(zip(adj, d))
        return  min(points, key=lambda x: x[1])[0]

def move(h, t, d, is_tail=False):
    moves = {
            'U': (0, 1),
            'R': (1, 0),
            'D': (0, -1),
            'L': (-1, 0)
            }

    if not is_tail:
        h = tuple(map(sum, zip(h, moves[d])))

    if t not in aoc.gen_coordinates(h, 8) and t != h:
        t = approach(h, t)

    return h, t

# pt 1
tails = []
h, t = (0, 0), (0, 0)
for i in data:
    d, s = i.split()
    for _ in range(int(s)):
        h, t = move(h, t, d)
        tails.append(t)
print(len(set(tails)))

# pt 2
nodes = [(0, 0)] * 10
last_tails = []
for i in data:
    d, s = i.split()
    for _ in range(int(s)):
        for n in range(len(nodes) - 1):
            if n == 0:
                nodes[n], nodes[n+1] = move(nodes[n], nodes[n+1], d)
            else:
                nodes[n], nodes[n+1] = move(nodes[n], nodes[n+1], d, True)
            if n+1 == len(nodes) - 1:
                last_tails.append(nodes[n+1])
print(len(set(last_tails)))

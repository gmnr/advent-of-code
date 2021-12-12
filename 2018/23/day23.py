#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day23 2018
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

import re
from queue import PriorityQueue as pq

def parse(data):
    regex = r'-?\d+'
    nanobots = []
    for line in data:
        match = tuple(map(int, re.findall(regex, line)))
        nanobots.append(match)
    return nanobots

def triple_man(a, b):
    ax, ay, az, _ = a
    bx, by, bz, _ = b
    return abs(ax-bx) + abs(ay-by) + abs(az-bz)

nanobots = parse(data)
# pt 1
strongest = max(nanobots, key=lambda x: x[3])
print(sum(1 if triple_man(strongest, x) <= strongest[3] else 0 for x in nanobots))

# pt 2
q = pq()
for n in nanobots:
    x, y, z, r = n
    d = abs(x) + abs(y) + abs(z)
    q.put((max(0, d - r), 1))
    q.put((d + r + 1, -1))
count = 0
max_count = 0
res = 0
while not q.empty():
    dist, e = q.get()
    count += e
    if count > max_count:
        res = dist
        max_count = count
print(res)

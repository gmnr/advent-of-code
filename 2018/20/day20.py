#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day20 2018
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read()[1:-2]

from collections import defaultdict as dd

dir = {'N': (0, 1), 'W': (1, 0), 'E': (-1, 0), 'S': (0, -1)}
pos = []
px, py = x, y = 0, 0
store = dd(int)

for c in data:
    if c == '(':
        pos.append((x, y))
    elif c == ')':
        x, y = pos.pop()
    elif c == '|':
        x, y = pos[-1]
    else:
        dx, dy = dir[c]
        x, y = x + dx, y + dy
        store[x, y] = min(store[x, y], store[px, py] + 1) if store[x, y] else store[px, py] + 1
    px, py = x, y

res = store.values()
print(store)
# pt 1
print(max(res))
# pt 2
print(len([x for x in res if x >= 1000]))

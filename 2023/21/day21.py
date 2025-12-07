#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day21 2023
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from collections import deque

data = aoc.read_input()


def bfs(src, steps, grid):
    queue = deque([(0, src)])
    visited = set()
    p = steps % 2
    res = 0
    h = len(data)

    while queue:
        dist, c = queue.popleft()
        if dist > steps:
            break

        if c in visited:
            continue

        if dist % 2 == p:
            res += 1

        visited.add(c)

        for n in aoc.gen_coordinates(c):
            r, c = n
            if grid[r % h][c % h] == "#":
                continue
            queue.append((dist + 1, n))

    return res


def quad(y, n):
    a = (y[2] - (2 * y[1]) + y[0]) // 2
    b = y[1] - y[0] - a
    c = y[0]
    return (a * n**2) + (b * n) + c


# pt 1
for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char == "S":
            start = (r, c)
            break

print(bfs(start, 64, data))

# pt 2
goal = 26501365
size = len(data)
edge = size // 2
y = [bfs(start, (edge + i * size), data) for i in range(3)]
print(quad(y, ((goal - edge) // size)))

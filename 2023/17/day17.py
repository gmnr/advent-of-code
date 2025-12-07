#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day17 2023
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
import heapq

data = aoc.read_input()

crucible = {}
for y, row in enumerate(data):
    for x, char in enumerate(row):
        crucible[(x, y)] = int(char)


def traverse(min_steps, max_steps):
    queue = [
        (crucible[(1, 0)], (1, 0), (1, 0), 0),
        (crucible[(0, 1)], (0, 1), (0, 1), 0),
    ]
    visited = set()
    target = max(crucible)

    while queue:
        heat, (x, y), (dx, dy), steps = heapq.heappop(queue)

        if (x, y) == target and min_steps <= steps:
            return heat

        if ((x, y), (dx, dy), steps) in visited:
            continue
        visited.add(((x, y), (dx, dy), steps))

        if steps < (max_steps - 1) and (x + dx, y + dy) in crucible:
            current = (x + dx, y + dy)
            heapq.heappush(
                queue, (heat + crucible[current], current, (dx, dy), steps + 1)
            )

        if min_steps <= steps:
            lx, ly, rx, ry = dy, -dx, -dy, dx
            l_pos, r_pos = (x + lx, y + ly), (x + rx, y + ry)

            for xx, yy, pos in zip((lx, rx), (ly, ry), (l_pos, r_pos)):
                if pos in crucible:
                    heapq.heappush(queue, (heat + crucible[pos], pos, (xx, yy), 0))


# pt 1
print(traverse(0, 3))

# pt 2
print(traverse(3, 10))

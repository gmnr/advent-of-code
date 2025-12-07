#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day17 2016
"""

__author__ = "gmnr"
__license__ = "GPL"


from helper import advent as aoc
from hashlib import md5


s = aoc.read_input()[0]

openchars = "bcdef"

grid = set((x, y) for x in range(4) for y in range(4))
directions = [(0, "U", (0, -1)), (1, "D", (0, 1)), (2, "L", (-1, 0)), (3, "R", (1, 0))]
start, target = (0, 0), (3, 3)


def to_target(state):
    pos, path = state
    return aoc.manhattan_dist(pos, target)


def moves(state):
    (x, y), path = state
    hashx = md5(bytes(s + path, "utf-8")).hexdigest()
    for i, p, (dx, dy) in directions:
        pos2 = (x + dx, y + dy)
        if hashx[i] in openchars and pos2 in grid:
            yield (pos2, path + p)


def longest_search(state, target, moves):
    longest = 0
    frontier = [state]
    while frontier:
        state = (pos, path) = frontier.pop()
        if pos == target:
            longest = max(longest, len(path))
        else:
            frontier.extend(moves(state))
    return longest


# pt 1
print(aoc.astar((start, ""), to_target, moves)[-1][1])

# pt 2
print(longest_search((start, ""), target, moves))

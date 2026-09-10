#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day24 2016
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc

data = aoc.read_input()
maze = []
to_visit = []

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "#":
            continue
        else:
            maze.append((x, y))

            if char != "." and char != "0":
                to_visit.append((x, y))

            if char == "0":
                START = (x, y)


def h(state, _):
    _, visited = state
    return len(to_visit) - len(visited)


def h_to_start(state, _):
    coord, visited = state
    return len(to_visit) - len(visited) + aoc.manhattan_dist(coord, START)


def moves(state):
    curr, visited = state
    for next in aoc.neighbors(curr):
        if next in maze:
            if next in to_visit:
                yield next, visited | frozenset({next})
            else:
                yield next, visited


# # pt 1
initial_state = (START, frozenset())
goal_state = (START, frozenset(to_visit))
path = aoc.astar_search(initial_state, goal_state, moves, h)
print(len(path) - 1)

# pt 2
path = aoc.astar_search(initial_state, goal_state, moves, h_to_start)
print(len(path) - 1)

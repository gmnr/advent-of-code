#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day22 2016
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from collections import namedtuple, deque
from itertools import permutations

data = aoc.read_input()


def bfs_mem_size(start, end, grid) -> int:
    frontier = deque([(start.coord, 0)])
    visited = {start}

    while frontier:
        current, steps = frontier.popleft()
        for next in aoc.gen_coordinates(current):

            if next not in grid:
                continue

            candidate = grid[next]
            if candidate.used < start.avail and candidate not in visited:
                frontier.append((candidate.coord, steps + 1))
                visited.add(candidate)

            if current == end.coord:
                return steps
    return 0


# pt 1
nodes = []
Node = namedtuple("Node", "coord, size, used, avail, perc")

for node in data:
    if not node.startswith("/dev"):
        continue
    x, y, *size_parameters = aoc.ints(node)
    nodes.append(Node((x, y), *size_parameters))

cnt = 0
for combo in permutations(nodes, 2):
    a, b = combo
    if a.used > 0 and a.used <= b.avail:
        cnt += 1
print(cnt)

# pt 2
target = max(nodes, key=lambda x: x.coord[0])
start = aoc.first(node for node in nodes if node.used == 0)
grid = {node.coord: node for node in nodes}

reach_target = bfs_mem_size(start, target, grid)
move_from_corner = (target.coord[0] - 1) * 5
print(reach_target + move_from_corner)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day15 2021
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import defaultdict
import heapq


def parse(data):
    maze = {}
    for y, line in enumerate(data):
        for x, val in enumerate(line):
            maze[x, y] = val
    return maze


def nb4(coord):
    x, y = coord
    return [(x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]


def dijkstra(maze, start, end):
    queue = [(0, start)]
    distances = defaultdict(lambda: 999_999, {start: 0})
    visited = set()

    while queue:
        dist, node = heapq.heappop(queue)
        if node == end:
            return dist

        if node in visited:
            continue
        visited.add(node)

        for n in nb4(node):
            if n not in maze or n in visited:
                continue

            new_dist = dist + int(maze[n])
            if new_dist < distances[n]:
                distances[n] = new_dist
                heapq.heappush(queue, (new_dist, n))
    return None


def build_new(maze, tile_size):
    new_maze = {}
    tx, ty = tile_size
    off_y = 0
    for i in range(5):
        off_x = 0
        for j in range(5):
            for k, v in maze.items():
                x, y = k
                new_x = x + off_x
                new_y = y + off_y
                new_val = int(v) + i + j
                if new_val > 9:
                    new_val = new_val % 9
                new_maze[new_x, new_y] = new_val
            off_x += tx + 1
        off_y += ty + 1
    return new_maze


# pt 1
maze = parse(data)
target = max(maze.keys())
print(dijkstra(maze, (0, 0), target))

# pt 2
new_maze = build_new(maze, target)
target = max(new_maze.keys())
print(dijkstra(new_maze, (0, 0), target))

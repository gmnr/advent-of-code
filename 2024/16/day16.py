#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day16 2024
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc

test = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

data = aoc.read_input(test)

maze = set()
start = end = 0
for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c in ("S", ".", "E"):
            maze.add((x, y))

            if c == "S":
                start = (x, y)

            if c == "E":
                end = (x, y)

print(maze)
print(start, end)

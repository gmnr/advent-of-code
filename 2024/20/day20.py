#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day20 2024
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc


test = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

data = aoc.read_input(test)

maze = set()
bounds = set()
start = end = 0
for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c in (".", "S", "E"):
            maze.add((x, y))

            if c == "S":
                start = (x, y)

            if c == "E":
                end = (x, y)
        else:
            bounds.add((x, y))


normal_path = 0
front = [start]
while front:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
solution for day 11 of 2019
"""

__author__ = "gmnr"
__license__ = "GPL"


import sys
from collections import defaultdict

sys.path.append("..")
from intcode import Intcode

with open("input.txt", "r") as f:
    data = f.read()


def run_robot(init=0):
    grid = defaultdict(int)
    grid[(0, 0)] = init

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    idx = 0
    x, y = 0, 0

    vm = Intcode(data)
    process = vm.run()

    try:
        val = next(process)

        while not vm.halted:
            if val == "INPUT_REQUIRED":

                curr_color = grid[(x, y)]
                val = process.send(curr_color)
                continue

            paint = val
            grid[(x, y)] = paint

            turn = next(process)
            if turn == 0:
                idx = (idx - 1) % 4
            else:
                idx = (idx + 1) % 4

            dx, dy = directions[idx]
            x += dx
            y += dy

            val = next(process)

    except StopIteration:
        pass
    return grid


# pt1
grid = run_robot()
print(len(grid))

# pt2
grid = run_robot(1)
x_coords = [x for x, y in grid.keys()]
y_coords = [y for x, y in grid.keys()]

min_x, max_x = min(x_coords), max(x_coords)
min_y, max_y = min(y_coords), max(y_coords)

for y in range(max_y, min_y - 1, -1):
    row = ""
    for x in range(min_x, max_x + 1):
        row += "#" if grid[(x, y)] == 1 else " "
    print(row)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day18 2023
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc

data = aoc.read_input()


def calculate_area(vertices):
    area = 0
    for i in range(1, len(vertices)):
        a, b = vertices[i - 1], vertices[i]
        ax, ay = a
        bx, by = b
        area += (ax * by) - (bx * ay)
    return abs(area // 2)


d = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
color_dir = {"0": "R", "1": "D", "2": "L", "3": "U"}

# pt 1
r = c = 0
vertices = [(r, c)]
perimeter = 0

cr = cc = 0
color_vertices = [(cr, cc)]
color_perimeter = 0

for line in data:
    direction, steps, color = line.split()
    dr, dc = tuple(map(lambda x: int(x) * int(steps), d[direction]))
    r = r + dr
    c = c + dc
    vertices.append((r, c))
    perimeter += int(steps)

    color_steps, color_direction = int(color[2:-2], 16), color_dir[color[-2]]
    dr, dc = tuple(map(lambda x: x * color_steps, d[color_direction]))
    cr = cr + dr
    cc = cc + dc
    color_vertices.append((cr, cc))
    color_perimeter += color_steps

# pt 1
area = calculate_area(vertices)
interiors = area - perimeter // 2 + 1
print(perimeter + interiors)

# pt 2
color_area = calculate_area(color_vertices)
color_interiors = color_area - color_perimeter // 2 + 1
print(color_perimeter + color_interiors)

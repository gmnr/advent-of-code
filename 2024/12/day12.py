#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day12 2024
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc

data = aoc.read_input()

grid = {}
for y, line in enumerate(data):
    for x, c in enumerate(line):
        grid[(x, y)] = c


def get_perimeter(points):
    perimeter = 0
    for p in points:
        for adjacent in aoc.gen_coordinates(p):
            if adjacent not in points:
                perimeter += 1
    return perimeter


def fill_plot(start, plot, plots):
    frontier = [start]
    res = [start]

    while frontier:
        curr = frontier.pop()
        for c in aoc.gen_coordinates(curr):
            if c not in plots or c in res:
                continue
            else:
                if grid[c] == plot:
                    res.append(c)
                    frontier.append(c)
                    plots.remove(c)

    return res, plots


def get_sides(points):
    sides = 0

    for p in points:

        mask = [x in points for x in aoc.gen_coordinates(p, 8)]
        if not mask[5] and not mask[4]:
            sides += 1
        if not mask[4] and not mask[7]:
            sides += 1
        if not mask[7] and not mask[6]:
            sides += 1
        if not mask[6] and not mask[5]:
            sides += 1
        if mask[5] and mask[4] and not mask[0]:
            sides += 1
        if mask[4] and mask[7] and not mask[2]:
            sides += 1
        if mask[7] and mask[6] and not mask[3]:
            sides += 1
        if mask[6] and mask[5] and not mask[1]:
            sides += 1

    return sides


separated_plots = []
# pt 1
plots = set(grid.keys())
for k, v in grid.items():
    if k in plots:
        p, plots = fill_plot(k, v, plots)
        separated_plots.append(p)

total = 0
for s in separated_plots:
    total += len(s) * get_perimeter(s)
print(total)

# pt 2
total = 0
for s in separated_plots:
    total += len(s) * get_sides(s)
print(total)

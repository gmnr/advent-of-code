#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day19 2017
"""

__author__ = "gmnr"
__license__ = "GPL"

with open("input.txt", "r") as f:
    data = f.read().splitlines()


def follow_path(data):
    diagram = []
    for line in data:
        diagram.append(list(line))

    x, y = diagram[0].index("|"), 0
    dx, dy = 0, 1
    while diagram[y][x] != " ":
        yield diagram[y][x]
        if diagram[y][x] == "+":
            dx, dy = new_dir(diagram, x, y)
        diagram[y][x] = "."
        x += dx
        y += dy


def new_dir(diagram, x, y):
    for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
        if diagram[y + dy][x + dx] not in [".", " "]:
            return dx, dy


# pt1
print("".join(c for c in follow_path(data) if c.isalnum()))
# pt2
print(sum(1 for _ in follow_path(data)))

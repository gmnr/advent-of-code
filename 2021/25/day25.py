#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day25 2021
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()


def parse(data):
    sea_floor = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            sea_floor[x, y] = (c, False)
    return sea_floor


def move(coord, c, floor, ref):
    x, y = coord

    if c == ">":
        dir = (1, 0)
        reset = (0, y)
    else:
        dir = (0, 1)
        reset = (x, 0)

    new_pos = tuple(map(sum, zip(coord, dir)))

    if new_pos in floor:
        if ref[new_pos][0] == ".":
            floor[new_pos] = (c, True)
            floor[coord] = (".", False)
    else:
        if ref[reset][0] == ".":
            floor[reset] = (c, True)
            floor[coord] = (".", False)

    return floor


def reset(floor):
    for k, v in floor.items():
        c, _ = v
        floor[k] = (c, False)
    return floor


def step(floor):
    ref = floor.copy()

    for k, v in ref.items():
        c, flag = v
        if c == ">" and not flag:
            floor = move(k, c, floor, ref)
        else:
            continue

    moved = any([x[1] for x in floor.values()])
    floor = reset(floor)
    ref = floor.copy()

    for k, v in ref.items():
        c, flag = v
        if c == "v" and not flag:
            floor = move(k, c, floor, ref)
        else:
            continue

    moved = moved or any([x[1] for x in floor.values()])
    floor = reset(floor)

    return floor, moved


# pt 1
floor = parse(data)
max_x, max_y = max(floor)
cnt = 0
while True:
    floor, moved = step(floor)
    cnt += 1
    if not moved:
        break
print(cnt)

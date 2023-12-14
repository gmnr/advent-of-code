#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day13 2023
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc

data = aoc.read_input(sep="\n\n")

tiles = []
for d in data:
    tile = []
    for r in d.splitlines():
        row = []
        for c in r:
            if c == "#":
                row.append(1)
            else:
                row.append(0)
        tile.append(row)
    tiles.append(tile)


def reflection(tile):
    m = len(tile) // 2
    for i in range(1, m + 1):
        mirr1 = tile[:i]
        mirr2 = tile[i : i + i][::-1]

        if mirr1 == mirr2:
            return i

        mirr1 = tile[len(tile) - i - i : len(tile) - i]
        mirr2 = tile[len(tile) - i :][::-1]
        if mirr1 == mirr2:
            return len(tile) - i

    return 0


def count_smudges(x, y):
    diff = 0
    for linx, liny in zip(x, y):
        for cx, cy in zip(linx, liny):
            if cx != cy:
                diff += 1
        if diff > 1:
            break

    return diff


def smudge_reflection(tile):
    m = len(tile) // 2
    for i in range(1, m + 1):
        mirr1 = tile[:i]
        mirr2 = tile[i : i + i][::-1]
        diff = count_smudges(mirr1, mirr2)

        if diff == 1:
            return i

        mirr1 = tile[len(tile) - i - i : len(tile) - i]
        mirr2 = tile[len(tile) - i :][::-1]
        diff = count_smudges(mirr1, mirr2)

        if diff == 1:
            return len(tile) - i

    return 0


# pt 1
cnt = 0
for t in tiles:
    cnt += reflection(aoc.rotate90(t))
    cnt += reflection(t) * 100
print(cnt)

# pt 2
cnt = 0
for t in tiles:
    cnt += smudge_reflection(aoc.rotate90(t))
    cnt += smudge_reflection(t) * 100
print(cnt)

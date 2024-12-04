#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day04 2024
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from collections import defaultdict

data = aoc.read_input()


def gen_radius(coord):
    x, y = coord
    dirs = (
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    )
    for d in dirs:
        xd, yd = d
        yield from ((x + xd * s, y + yd * s) for s in range(4))


def is_XMAS(coord, chars):
    word = []
    words = []
    for c in gen_radius(coord):
        word.append(chars[c])
        if len(word) == 4:
            if "".join(word) == "XMAS" or "".join(word[::-1]) == "XMAS":
                words.append((coord, c))
                word = []
            else:
                word = []
    return words


def gen_X(coord):
    x, y = coord
    dirs = (
        (1, 1),
        (1, -1),
        (0, 0),
        (-1, 1),
        (-1, -1),
    )
    yield from ((x + dx, y + dy) for dx, dy in dirs)


def is_X(coord, chars):
    word = []
    comparison = ["MMASS", "SSAMM", "MSAMS", "SMASM"]
    for c in gen_X(coord):
        word.append(chars[c])
    if "".join(word) in comparison:
        return True


chars = defaultdict(str)
for y, row in enumerate(data):
    for x, c in enumerate(row):
        chars[(x, y)] = c

# pt 1
words = []
for c in list(chars):
    if is_XMAS(c, chars):
        words.extend(is_XMAS(c, chars))
print(len(list(set(frozenset(c) for c in words))))

# pt 2
all_A = [k for k, v in chars.items() if v == "A"]
cnt = 0
for c in list(chars):
    if is_X(c, chars):
        cnt += 1
print(cnt)

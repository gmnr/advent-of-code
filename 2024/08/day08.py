#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day08 2024
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from collections import defaultdict
from itertools import combinations
from dataclasses import dataclass


@dataclass(frozen=True)
class P:
    x: int
    y: int


data = aoc.read_input()
antennas = defaultdict(list)
max_x = len(data[0])
max_y = len(data)
for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c == ".":
            continue
        antennas[c] += [P(x, y)]


def inside(p):
    return 0 <= p.x < max_x and 0 <= p.y < max_y


def find_res(a, b):
    resonance = set()

    dx = b.x - a.x
    dy = b.y - a.y

    if inside(P(a.x - dx, a.y - dy)):
        resonance.add(P(a.x - dx, a.y - dy))

    if inside(P(b.x + dx, b.y + dy)):
        resonance.add(P(b.x + dx, b.y + dy))

    return resonance


def find_all_res(a, b):
    resonance = {a, b}

    dx = b.x - a.x
    dy = b.y - a.y

    cx, cy = a.x, a.y
    while True:
        cx -= dx
        cy -= dy

        if not inside(P(cx, cy)):
            break
        resonance.add(P(cx, cy))

    cx, cy = a.x, a.y
    while True:
        cx += dx
        cy += dy

        if not inside(P(cx, cy)):
            break
        resonance.add(P(cx, cy))
    return resonance


single_res = set()
total_res = set()
for k in antennas:
    resonators = antennas[k]
    for combo in combinations(resonators, 2):
        single_res.update(find_res(*combo))
        total_res.update(find_all_res(*combo))
# pt 1
print(len(single_res))

# pt 2
print(len(total_res))

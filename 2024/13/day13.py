#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day13 2024
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc

prizes = aoc.read_input(sep="\n\n")


def play_arcade(ax, ay, bx, by, px, py, pt2=False):
    A = 3
    B = 1

    if pt2:
        px += 10_000_000_000_000
        py += 10_000_000_000_000

    b = (py * ax - px * ay) / (by * ax - bx * ay)
    a = (px - b * bx) / ax

    if int(a) == a and int(b) == b:
        return int(a * A + b * B)
    else:
        return 0


# pt 1
coins = 0
for line in prizes:
    coins += play_arcade(*aoc.ints(line))
print(coins)

# pt 2
coins = 0
for line in prizes:
    coins += play_arcade(*aoc.ints(line), True)
print(coins)

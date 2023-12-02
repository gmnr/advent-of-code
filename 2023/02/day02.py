#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day02 2023
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
import math
import re

data = aoc.read_input()


def is_possible(g_set):
    POSSIBLE = {"red": 12, "green": 13, "blue": 14}
    BAG = {"red": 0, "green": 0, "blue": 0}
    regex = r"red|green|blue"

    colors = re.findall(regex, g_set)
    ints = aoc.ints(g_set)
    for x in zip(colors, ints):
        BAG[x[0]] = x[1]

    for k, v1 in BAG.items():
        v2 = POSSIBLE[k]
        if v1 > v2:
            return False

    return True


games = []
for game in data:
    _, g = game.split(":")
    games.append(g)

# pt 1
checksum = 0
possible_games = []
for n, g in enumerate(games, 1):
    sets = g.split(";")
    checksum += n
    for s in sets:
        if not is_possible(s):
            checksum -= n
            break
print(checksum)

# pt 2
powers = 0
regex = r"\d+ red|\d+ green|\d+ blue"
for g in games:
    values = re.findall(regex, g)
    BAG = {"red": 0, "green": 0, "blue": 0}
    for v in values:
        num, color = v.split()
        num = int(num)
        if num > BAG[color]:
            BAG[color] = num
    powers += math.prod(BAG.values())
print(powers)

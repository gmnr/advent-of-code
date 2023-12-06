#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day06 2023
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
import math
import re


data = aoc.read_input()
races = zip(aoc.ints(data[0]), aoc.ints(data[1]))


def get_race(l, d):
    c = 0
    for t in range(l):
        move_time = l - t
        length = t * move_time
        if length > d:
            c += 1
    return c


# pt 1
wins = []
for l, d in races:
    wins.append(get_race(l, d))
print(math.prod(wins))

# pt 2
longer_race = []
for d in data:
    r = re.findall(r"\d+", d)
    r = "".join(r)
    longer_race.append(int(r))

wins = []
l, d = longer_race
wins.append(get_race(l, d))
print(math.prod(wins))

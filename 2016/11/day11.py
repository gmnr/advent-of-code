#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day11 2016
"""

__author__ = "gmnr"
__license__ = "GPL"


from helper import advent as aoc
import re

data = aoc.read_input()


def parse(data):
    floors = []
    for line in data:
        matches = re.findall(r"microchip|generator", line)
        floors.append(len(matches))
    return floors


def move(items):
    moves = 0
    while items[-1] != sum(items):
        low_floor = 0
        while items[low_floor] == 0:
            low_floor += 1
        moves += 2 * (items[low_floor] - 1) - 1
        items[low_floor + 1] += items[low_floor]
        items[low_floor] = 0
    return moves


# p1
floors = parse(data)
print(move(floors))

# pt 2
floors = parse(data)
floors[0] = floors[0] + 4
print(move(floors))

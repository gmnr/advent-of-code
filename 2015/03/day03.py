#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 03 2015
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()[0]

from operator import add


def santa(itinerary):
    coord = set()
    curr = (0, 0)
    dirs = {"^": (0, 1), ">": (1, 0), "<": (-1, 0), "v": (0, -1)}
    for mov in itinerary:
        nxt = tuple(map(add, dirs[mov], curr))
        coord.add(nxt)
        curr = nxt
    return len(coord)


def robo_santa(itinerary):
    coord = set()
    curr1 = (0, 0)
    curr2 = (0, 0)
    dirs = {"^": (0, 1), ">": (1, 0), "<": (-1, 0), "v": (0, -1)}
    turn1 = True
    for mov in itinerary:
        if turn1:
            nxt = tuple(map(add, dirs[mov], curr1))
            coord.add(nxt)
            curr1 = nxt
            turn1 = False
        else:
            nxt = tuple(map(add, dirs[mov], curr2))
            coord.add(nxt)
            curr2 = nxt
            turn1 = True
    return len(coord)


print(santa(data))
print(robo_santa(data))

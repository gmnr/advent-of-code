#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day20 2015
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = int(f.read().rstrip())

from collections import defaultdict as dd


def solve_houses(upper):
    houses = dd(int)

    for elf in range(1, target):
        for house in range(elf, upper, elf):
            houses[house] += elf * 10

            if houses[elf] >= target:
                return elf


def solve_houses_elves(upper):
    houses = dd(int)

    for elf in range(1, target):
        for house in range(elf, min(elf * 50 + 1, upper), elf):
            houses[house] += elf * 11

        if houses[elf] >= target:
            return elf


target = data
# pt1
print(solve_houses(1000000))
# pt2
print(solve_houses_elves(1000000))

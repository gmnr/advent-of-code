#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day12 2023
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from functools import cache

data = aoc.read_input()

springs = []
for x in data:
    line, inst = x.split()
    springs.append((line, aoc.ints(inst)))


@cache
def possible_arrange(line, inst):
    line = line.lstrip(".")
    if line == "":
        if inst == tuple():
            return 1
        else:
            return 0

    if inst == tuple():
        if line.find("#") == -1:
            return 1
        else:
            return 0

    if line[0] == "#":
        if len(line) < inst[0] or "." in line[0 : inst[0]]:
            return 0

        elif len(line) == inst[0]:
            if len(inst) == 1:
                return 1
            else:
                return 0

        elif line[inst[0]] == "#":
            return 0

        else:
            return possible_arrange(line[inst[0] + 1 :], inst[1:])

    return possible_arrange("#" + line[1:], inst) + possible_arrange(line[1:], inst)


# pt 1
print(sum(possible_arrange(line, inst) for line, inst in springs))

# pt 2
print(sum(possible_arrange("?".join([line] * 5), inst * 5) for line, inst in springs))

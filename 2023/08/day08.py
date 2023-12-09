#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day08 2023
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from collections import deque
from math import lcm
import re


data = aoc.read_input()


def steps(e):
    inst = {"L": 0, "R": 1}
    c = 0
    while e[-1] != "Z":
        i = instructions[0]
        instructions.rotate(-1)
        e = elements[e][inst[i]]
        c += 1
    return c


# pt 1
instructions = deque(list(data[0]))
elements = {}
ending_a = []
for d in data[2:]:
    lookup, left, right = re.findall("[A-Z]+", d)
    elements[lookup] = (left, right)
    if lookup[-1] == "A":
        ending_a.append(lookup)
print(steps("AAA"))

# pt 2
paths = []
for e in ending_a:
    paths.append(steps(e))
print(lcm(*paths))

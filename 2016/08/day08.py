#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day08 2016
"""

__author__ = "gmnr"
__license__ = "GPL"


from helper import advent as aoc
from collections import deque
import re

data = aoc.read_input()

screen = [["."] * 50] * 6
regex = r"\d+"


def rot90(mat):
    return list(zip(*mat[::-1]))


def unrot90(mat):
    return list(zip(*mat))[::-1]


def light(w, h):
    for i in range(h):
        screen[i] = ["#"] * w + list(screen[i][w:])
    return screen


for instr in data:
    x, y = re.findall(regex, instr)
    x, y = int(x), int(y)

    if instr.startswith("rect"):
        light(x, y)

    if instr.startswith("rotate column"):
        screen = rot90(screen)

        target = deque(screen[x])
        target.rotate(-y)
        screen[x] = list(target)

        screen = unrot90(screen)

    if instr.startswith("rotate row"):
        target = deque(screen[x])
        target.rotate(y)
        screen[x] = list(target)

# pt 1
flat = [x for el in screen for x in el]
print(flat.count("#"))

# pt 2
for i in screen:
    print("".join(i))

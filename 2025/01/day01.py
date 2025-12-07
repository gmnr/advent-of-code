#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day01 2025
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc


data = aoc.read_input()

# pt 1
pos = 50
zeros = 0
for instr in data:
    change = int(instr[1:])
    if instr.startswith("R"):
        if pos + change > 99:
            pos = (pos + change) % 100
        else:
            pos += change

    else:
        if pos - change < 0:
            pos = (pos - change) % 100
        else:
            pos -= change

    if pos == 0:
        zeros += 1
print(zeros)

# pt 2
pos = 50
zeros = 0
for instr in data:
    change = int(instr[1:])
    if instr.startswith("R"):
        for _ in range(change):
            pos += 1
            if pos > 99:
                pos = 0
                zeros += 1
    else:
        for _ in range(change):
            pos -= 1
            if pos == 0:
                zeros += 1
            elif pos < 0:
                pos = 99
print(zeros)

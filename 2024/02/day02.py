#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day02 2024
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc

data = aoc.read_input()


def check_safe(line):
    delta = []
    for x in range(1, len(line)):
        delta.append(line[x] - line[x - 1])
    if max(delta) > 3 or min(delta) < -3:
        return False
    if all(x > 0 for x in delta) or all(x < 0 for x in delta):
        return True


# pt 1
safe = 0
dampener = []
for line in data:
    line = aoc.ints(line)
    if check_safe(line):
        safe += 1
    else:
        dampener.append(line)
print(safe)

# pt 2
dampened = 0
for line in dampener:
    for i in range(len(line)):
        dampened_line = line[:i] + line[i + 1 :]
        if check_safe(dampened_line):
            dampened += 1
            break
print(safe + dampened)

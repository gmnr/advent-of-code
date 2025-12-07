#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day03 2024
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
import re
import math


with open("input.txt", "r") as f:
    data = f.read()


# pt 1
regex = r"mul\(\d+\,\d+\)"
operations = re.findall(regex, data)

cnt = 0
for op in operations:
    cnt += math.prod(aoc.ints(op))
print(cnt)

# pt 2
regex = r"mul\(\d+\,\d+\)|do\(\)|don't\(\)"
operations = re.findall(regex, data)

cnt = 0
enable = True
for op in operations:
    if op == "don't()":
        enable = False
    elif op == "do()":
        enable = True
        continue

    if enable:
        cnt += math.prod(aoc.ints(op))
print(cnt)

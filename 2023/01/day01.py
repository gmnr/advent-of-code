#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day01 2023
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
import re

data = aoc.read_input()
regex = r"\d|one|two|three|four|five|six|seven|eight|nine"

table = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# pt 1
acc = 0
for m in data:
    match = re.findall(regex, m)
    match = [x for x in match if x not in table.keys()]
    v1, v2 = match[0], match[-1]
    acc += int(v1 + v2)
print(acc)

# pt 2
acc = 0
for m in data:
    match = re.findall(regex, m)
    match = [table[x] if x in table.keys() else x for x in match]
    v1, v2 = match[0], match[-1]
    acc += int(v1 + v2)
print(acc)

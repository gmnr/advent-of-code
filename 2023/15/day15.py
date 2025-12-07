#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day15 2023
"""

__author__ = "gmnr"
__license__ = "GPL"


from collections import defaultdict
import helper.advent as aoc
import re

data = aoc.read_input(sep=",")


def HASH(s):
    val = 0

    for c in s:
        val += ord(c)
        val = val * 17 % 256

    return val


# pt 1
cnt = 0
for i in data:
    cnt += HASH(i)
print(cnt)

# pt 2
boxes = {i: defaultdict(dict) for i in range(0, 256)}
for i in data:
    key = re.findall(r"\w+", i)[0]
    box = HASH(key)

    if "=" in i:
        _, val = i.split("=")
        boxes[box][key] = val
    elif "-" in i:
        if key in boxes[box]:
            del boxes[box][key]

cnt = 0
for i, b in enumerate(boxes):
    for j, l in enumerate(boxes[b].values()):
        cnt += (i + 1) * (j + 1) * int(l)
print(cnt)

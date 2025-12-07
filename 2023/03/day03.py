#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day03 2023
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
import math
import re

data = aoc.read_input()

len_x = len(data[0])
len_y = len(data)

engine_map = {}
for y in range(len_y):
    for x in range(len_x):
        engine_map[(x, y)] = data[y][x]

nums = {}
cnt = 0
for y in range(len_y):
    finds = re.findall(r"\d+", data[y])
    if not finds:
        continue
    for val, match in zip(finds, re.finditer(r"\d+", data[y])):
        nums[cnt] = (val, [(m, y) for m in range(match.start(), match.end())])
        cnt += 1

poi = [k for k, v in engine_map.items() if re.match(r"[^a-zA-Z0-9_\\.]", v)]

# pt 1
checksum = 0
for _, point in nums.items():
    num, coords = point
    found = False
    for p in coords:
        for n in aoc.gen_coordinates(p, 8):
            if n in poi:
                checksum += int(num)
                found = True
                break
        if found:
            found = False
            break
print(checksum)

# pt 2
gears = [k for k, v in engine_map.items() if re.match(r"\*", v)]

counts = []
for g in gears:
    g_count = []
    for n in aoc.gen_coordinates(g, 8):
        for _, point in nums.items():
            num, coords = point
            if n in coords:
                g_count.append(int(num))
                break
    counts.append(set(g_count))

counts = [x for x in counts if len(x) == 2]
print(sum(math.prod(x) for x in counts))

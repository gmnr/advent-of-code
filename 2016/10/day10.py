#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day10 2016
"""

__author__ = "gmnr"
__license__ = "GPL"


from helper import advent as aoc
from collections import defaultdict as dd
import re

data = aoc.read_input()


def parse(instructions):
    regex = r"value \d*|bot \d*|output \d*"
    instr = dd(list)
    bots = dd(list)

    for i in instructions:
        res = re.findall(regex, i)
        string = "".join(res)
        if len(res) == 2:
            val, bot = aoc.ints(string)
            bots[bot].append(val)
        else:
            agent, *dest = res
            agent = aoc.ints(agent)[0]
            instr[agent] = dest

    complete = []
    incomplete = []
    for b in bots:
        if len(bots[b]) == 2:
            complete.append(b)
        else:
            incomplete.append(b)

    return instr, complete, incomplete, bots


instr, complete, incomplete, bots = parse(data)
output = dd(list)

# part 1
for c in complete:
    low, high = sorted(bots[c])
    if low == 17 and high == 61:
        print(c)
    string = "".join(instr[c])
    s_low, s_high = instr[c]
    i_low, i_high = aoc.ints(string)

    if s_low.startswith("o"):
        output[i_low].append(low)
    else:
        bots[i_low].append(low)
        if i_low in incomplete:
            incomplete.remove(i_low)
            complete.append(i_low)
        else:
            incomplete.append(i_low)

    if s_high.startswith("o"):
        output[i_high].append(high)
    else:
        bots[i_high].append(high)
        if i_high in incomplete:
            incomplete.remove(i_high)
            complete.append(i_high)
        else:
            incomplete.append(i_high)

    bots[c] = []

# part 2
res = 1
for i in range(3):
    res *= output[i][0]
print(res)

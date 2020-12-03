#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 3 2020
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().split('\n')[:-1]

import math
from functools import reduce


def findTrees(c, r, data):
    c_counter = 0
    cnt = 0
    if r == 2:
        data = data[::2]
    for terr in data:
        if c_counter >= len(terr):
            terr = terr * math.ceil(c_counter / len(terr))
            terr += terr[0]
        if terr[c_counter] == '#':
            cnt += 1
        c_counter += c
    return cnt


# part 1
print(findTrees(3, 1, data))

# part 2
rule1 = [1,3,5,7,1]
rule2 = [1,1,1,1,2]
res = []
for zips in zip(rule1, rule2):
    res.append(findTrees(*zips, data))
res = reduce(lambda x, y: x * y, res)
print(res)

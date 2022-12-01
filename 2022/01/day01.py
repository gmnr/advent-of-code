#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day01 2022
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


import helper.advent as aoc
from collections import defaultdict

data = aoc.read_input()

elves = defaultdict(int)
cnt = 0
for i in data:
    if i == '':
        cnt += 1
        continue
    else:
        i = int(i)
        elves[cnt] += i
    
# pt 1
print(max(elves.values()))

# pt 2
print(sum(sorted(elves.values())[-3:]))

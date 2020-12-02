#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day01 2015
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open("input.txt", "r") as f:
    data = f.read().strip()

solution1 = sum([+1 if x == '(' else -1 for x in data])

tot = 0
for k, v in enumerate(data):
    tot += (-1, 1)[v == '(']
    if tot == -1:
        solution2 = k + 1
        break

print(solution1)
print(solution2)

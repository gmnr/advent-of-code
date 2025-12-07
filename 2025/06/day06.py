#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day06 2025
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from math import prod

with open("input.txt") as f:
    data = f.read().splitlines()

# pt 1
operations = []
for l in data:
    line = []
    for c in l.split():
        if c == "+" or c == "*":
            operations.append(l.split())
            break
        line.append(int(c))
    if line != []:
        operations.append(line)

cnt = 0
for line in aoc.rotate90(operations):
    if line[0] == "+":
        oper = sum
    else:
        oper = prod
    cnt += oper(line[1:])
print(cnt)

# pt 2
side = []
i = 0
while i < len(data[0]):
    col = ""
    for l in data:
        col += l[i]
    side.append(col)
    i += 1

cnt = 0
part = []
for op in side:
    if op[-1] == "*":
        oper = prod
        op = op[:-1]
    elif op[-1] == "+":
        oper = sum
        op = op[:-1]

    if op == " " * len(op):
        cnt += oper(part)
        part = []
        continue

    part.append(int(op.split()[0]))
cnt += oper(part)
print(cnt)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 09 2020
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from itertools import permutations as perm

data = [int(x) for x in data]


def sumPerm(lst):
    perms = perm(lst, 2)
    return [sum(x) for x in perms]


offset = 25
for i in range(len(data)):
    if i < offset:
        continue
    preamble = data[i - offset : i]
    perms = sumPerm(preamble)
    if data[i] not in perms:
        target = data[i]
        print(target)
        break

for i in range(len(data)):
    res = []
    acc = 0
    while acc < target:
        res.append(data[i])
        acc += data[i]
        i += 1
    if acc == target:
        break

print(f"{min(res) + max(res)}")

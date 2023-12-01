#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 12 2017
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import defaultdict as dd

groups = dd(list)

for rule in data:
    prg, conn = rule.split(" <-> ")
    prg = int(prg)
    conn = [int(x) for x in conn.split(", ")]
    groups[prg] = conn


def countGroup(target, seen=[]):
    for i in groups[target]:
        if i in seen:
            continue
        else:
            seen.append(i)
            countGroup(i, seen)
    return len(seen)


# pt 1
print(countGroup(0))
# pt 2
c = []
for i in list(groups.keys()):
    c.append(countGroup(i))
print(len(set(c)))

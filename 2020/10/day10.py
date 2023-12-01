#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 10 2020
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from functools import reduce
from collections import defaultdict as dd

data = [int(x) for x in data]
data = sorted(data)
adapter = max(data) + 3
data.insert(0, 0)
data.append(adapter)

one = 0
three = 0
for i in range(len(data)):
    if i == (len(data) - 1):
        break
    diff = data[i + 1] - data[i]
    if diff > 1:
        three += 1
    else:
        one += 1


def score(data):
    res = []
    idx = 0
    lookup = dd(lambda: 1)
    for i, val in enumerate(data):
        if data[i] - data[i - 1] > 2:
            res.append(data[idx:i])
            idx = i
    res.append(data[idx:])
    lookup[3] = 2
    lookup[4] = 4
    lookup[5] = 7
    mapped = map(lambda x: lookup[len(x)], res)
    return reduce(lambda x, y: x * y, mapped)


# pt 1
print(one * three)
# pt 2
print(score(data))

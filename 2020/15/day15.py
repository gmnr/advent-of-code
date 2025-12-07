#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 15 2020
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().rstrip().split(",")

from collections import defaultdict as dd, deque as dq


def playGame(data, target):
    spoken = dd(lambda: dq([], maxlen=2))
    spoken.update({int(k): dq([v + 1], maxlen=2) for v, k in enumerate(data)})
    last = list(spoken.keys())[-1]
    for i in range(len(data), target):
        val = i + 1
        if len(spoken[last]) == 1:
            last = 0
            spoken[0].append(val)
            continue
        else:
            last = spoken[last][1] - spoken[last][0]
            spoken[last].append(val)
    return last


# pt 1
print(playGame(data, 2020))
# pt 2 ~ 40 secs
print(playGame(data, 30_000_000))

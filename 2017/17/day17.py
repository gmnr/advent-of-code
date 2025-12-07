#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day17 2017
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = int(f.read().rstrip())

from collections import deque


def spinlock(arr, step, val):
    arr.rotate(-step)
    arr.insert(1, val)
    arr.rotate(-1)
    return arr


# pt 1
arr = deque([0])
for i in range(1, 2018):
    arr = spinlock(arr, data, i)
print(arr[1])
# pt 2
n_arr = deque([0])
for i in range(1, 50_000_000):
    arr = spinlock(n_arr, data, i)
idx = arr.index(0)
print(arr[idx + 1])

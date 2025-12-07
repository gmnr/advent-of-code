#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day01 2021
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

data = [int(x) for x in data]


def count_increase(data):
    cnt = 0
    comparison = data[0]
    for n in data:
        if n > comparison:
            cnt += 1
        comparison = n
    return cnt


# pt 1
print(count_increase(data))

# pt 2
values = [sum([data[i], data[i + 1], data[i + 2]]) for i in range(len(data) - 2)]
print(count_increase(values))

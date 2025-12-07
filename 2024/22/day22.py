#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day22 2024
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc

test = """1
10
100
2024
"""

data = aoc.read_input()

buyers = [int(x) for x in data]


def secret(num):
    res = num
    op = num * 64
    res = res ^ op
    res = res % 16777216
    op = res // 32
    res = res ^ op
    res = res % 16777216
    op = res * 2048
    res = res ^ op
    res = res % 16777216
    return res


# pt 1
new_buyers = []
for b in buyers:
    for _ in range(2000):
        b = secret(b)
    new_buyers.append(b)
print(sum(new_buyers))

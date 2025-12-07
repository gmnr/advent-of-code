#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day20 2022
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from collections import deque

data = aoc.read_input()
# print(data)

test = """1
2
-3
3
-2
0
4""".splitlines()

test = [int(x) for x in test]

test = deque(test)

for _ in range(3_000):
    v = test[0]
    test.rotate(v)

    print(test)


idx = list(test).index(0)
res = test[idx + 1]
print(res)

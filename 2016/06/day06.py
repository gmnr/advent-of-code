#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day06 2016
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


from helper import advent as aoc
from collections import Counter

data = aoc.read_input()
transposed = aoc.transpose(data)

# pt 1
message = ""
for l in transposed:
    most_frequent = Counter(l)
    message += most_frequent.most_common(1)[0][0]
print(message)

# pt 2
message = ""
for l in transposed:
    most_frequent = Counter(l)
    message += most_frequent.most_common()[-1][0]
print(message)

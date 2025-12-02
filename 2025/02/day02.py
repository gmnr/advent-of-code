#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day02 2025
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from textwrap import wrap

data = aoc.read_input(sep=",")


def is_invalid(x):
    check = str(x)
    mid = len(check) // 2
    if check[:mid] == check[mid:]:
        return x
    else:
        return False


def is_all_invalid(x):
    check = str(x)

    for i in range(1, (len(check) // 2) + 1):
        chunks = wrap(check, i)
        if all(c == chunks[0] for c in chunks):
            return x
    return False


# pt 1
invalid = 0
for ranges in data:
    first, last = ranges.split("-")
    first = int(first)
    last = int(last)
    for n in range(first, last + 1):
        if is_invalid(n):
            invalid += n
print(invalid)

# pt 2
invalid = 0
for ranges in data:
    first, last = ranges.split("-")
    first = int(first)
    last = int(last)
    for n in range(first, last + 1):
        if is_all_invalid(n):
            invalid += n
print(invalid)

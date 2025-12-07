#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day02 2025
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc

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
    n = len(check)

    for i in range(1, (n // 2) + 1):
        new_s = check[:i]
        if new_s * (n // i) == check:
            return check

    return False


# pt 1
invalid = 0
for ranges in data:
    first, last = ranges.split("-")
    for n in range(int(first), int(last) + 1):
        if is_invalid(n):
            invalid += n
print(invalid)

# pt 2
invalid = 0
for ranges in data:
    first, last = ranges.split("-")
    for n in range(int(first), int(last) + 1):
        if is_all_invalid(n):
            invalid += n
print(invalid)

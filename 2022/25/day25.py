#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day25 2022
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc

data = aoc.read_input()


def snafu(s):
    lookup = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    return sum(lookup[v] * 5**i for i, v in enumerate(s[::-1]))


def rev_snafu(n):
    res = ""

    while n:
        n, digit = divmod(n, 5)
        res += "012=-"[digit]
        n += digit > 2

    return res[::-1]


# pt 1
sequence = sum(snafu(s) for s in data)
print(rev_snafu(sequence))

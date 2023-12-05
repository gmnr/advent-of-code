#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day16 2016
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


from helper import advent as aoc

data = [int(x) for x in aoc.read_input()[0]]
length = 272


def solve(s, l):
    while len(s) < l:
        a = b = s
        b = b[::-1]
        b = [(1, 0)[i] for i in b]
        s = a + [0] + b

    s = s[:length]
    pairs = [(s[i], s[i + 1]) for i in range(0, len(s), 2)]
    s = [int(x[0] == x[1]) for x in pairs]

    while len(s) % 2 == 0:
        pairs = [(s[i], s[i + 1]) for i in range(0, len(s), 2)]
        s = [int(x[0] == x[1]) for x in pairs]
    return s


# pt 1
res = solve(data, length)
print("".join([str(x) for x in res]))

# pt 2
length = 35651584
res = solve(data, length)
print("".join([str(x) for x in res]))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day13 2022
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from functools import cmp_to_key

data = aoc.read_input(sep="\n\n")


def compare(l, r):
    l_int = type(l) is int
    r_int = type(r) is int

    if l_int and r_int:
        return l - r

    if l_int != r_int:
        if l_int:
            return compare([l], r)
        else:
            return compare(l, [r])

    for x, y in zip(l, r):
        res = compare(x, y)
        if res != 0:
            return res

    return len(l) - len(r)


# pt 1
cnt, pairs = 1, []
for pair in data:
    left, right = [eval(x) for x in pair.splitlines()]
    if compare(left, right) < 0:
        pairs.append(cnt)
    cnt += 1
print(sum(pairs))

# pt 2
packets = []
for pair in data:
    p1, p2 = pair.splitlines()
    packets.extend([p1, p2])

packets = [eval(x) for x in packets]

dividers = [[[2]], [[6]]]
packets.extend(dividers)
packets.sort(key=cmp_to_key(compare))

dv1, dv2 = dividers
print((packets.index(dv1) + 1) * (packets.index(dv2) + 1))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 10 2017
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read()

from collections import deque as dq
from itertools import islice as isl
from functools import reduce


def dumb():
    print("suck it ")


string = dq([x for x in range(256)])
c = 0
skip = 0
lenghts = [int(x) for x in data[:-1].split(",")]

for l in lenghts:
    string.rotate(-c)
    sel = list(isl(string, l))
    rest = list(isl(string, l, len(string)))
    sel = sel[::-1]
    string = dq(sel + rest)
    string.rotate(c)
    c += l + skip
    skip += 1


def hash_knot(string):
    rope = dq([x for x in range(256)])
    c = 0
    skip = 0
    inst = [ord(x) for x in string]
    inst += [17, 31, 73, 47, 23]

    for _ in range(64):
        for l in inst:
            rope.rotate(-c)
            sel = list(isl(rope, l))
            rest = list(isl(rope, l, len(rope)))
            sel = sel[::-1]
            rope = dq(sel + rest)
            rope.rotate(c)
            c += l + skip
            skip += 1
    res = list(rope)
    chunks = [res[i : i + 16] for i in range(0, len(res), 16)]
    msg = [hex(reduce(lambda x, y: x ^ y, ch)) for ch in chunks]
    return "".join([x[2:].zfill(2) for x in msg])


# pt 1
string = list(string)
print(string[0] * string[1])
# pt 2
print(hash_knot(data[:-1]))

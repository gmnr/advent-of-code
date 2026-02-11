#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Soluton for day21 2016
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from collections import deque
from itertools import permutations

instr = aoc.read_input()
s = "abcdefgh"


def swap(instr, s):
    if "position" in instr:
        a, b = aoc.ints(instr)
        al, bl = s[a], s[b]
        s = list(s)
        s[b], s[a] = al, bl
        s = "".join(s)
    else:
        a, b = (x for x in instr.split() if len(x) == 1)
        s = s.replace(a, "1")
        s = s.replace(b, "2")
        s = s.replace("2", a)
        s = s.replace("1", b)
    return s


def reverse(instr, s):
    a, b = aoc.ints(instr)
    tmp = list(s)
    seg = "".join(tmp[a : b + 1][::-1])
    return s[:a] + seg + s[b + 1 :]


def rotate(instr, s):
    if "based" in instr:
        l = [x for x in instr.split() if len(x) == 1]
        p = s.find(l[0])
        s = deque(s)
        s.rotate(1)
        s.rotate(p)
        if p >= 4:
            s.rotate(1)
    else:
        steps = aoc.ints(instr)[0]
        if "left" in instr:
            d = -1
        else:
            d = 1
        s = deque(s)
        s.rotate(d * steps)
    s = "".join(list(s))
    return s


def move(instr, s):
    a, b = aoc.ints(instr)
    s = list(s)
    l = [s.pop(a)]
    s = s[:b] + l + s[b:]

    s = "".join(s)
    return s


def solve(instructions, s):
    for i in instructions:
        match i.split()[0]:
            case "swap":
                s = swap(i, s)
            case "rotate":
                s = rotate(i, s)
            case "reverse":
                s = reverse(i, s)
            case "move":
                s = move(i, s)
    return s


# pt 1
print(solve(instr, s))

# pt 2
scrambled = "fbgdceah"
for l in permutations(s, 8):
    if solve(instr, "".join(l)) == scrambled:
        print("".join(l))

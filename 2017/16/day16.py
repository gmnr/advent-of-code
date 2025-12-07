#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day16 2017
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().rstrip().split(",")

from collections import deque

programs = deque("abcdefghijklmnop")


def dance(prg, inst):
    if inst.startswith("s"):
        amt = int(inst[1:])
        prg.rotate(amt)
    elif inst.startswith("x"):
        t1, t2 = [int(x) for x in inst[1:].split("/")]
        tmp = list(prg)
        tmp[t1], tmp[t2] = tmp[t2], tmp[t1]
        prg = deque(tmp)
    elif inst.startswith("p"):
        t1, t2 = inst[1:].split("/")
        tmp = list(prg)
        i1 = tmp.index(t1)
        i2 = tmp.index(t2)
        tmp[i1], tmp[i2] = tmp[i2], tmp[i1]
        prg = deque(tmp)
    return prg


# pt 1
for inst in data:
    programs = dance(programs, inst)
print("".join(programs))
# pt 2
rep = 1
while "".join(programs) != "abcdefghijklmnop":
    for inst in data:
        programs = dance(programs, inst)
    rep += 1
period = 1_000_000_000 % (rep)

p = deque("abcdefghijklmnop")
for _ in range(period):
    for inst in data:
        p = dance(p, inst)
print("".join(p))

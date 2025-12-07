#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day12 2016
"""

__author__ = "gmnr"
__license__ = "GPL"


from helper import advent as aoc

data = aoc.read_input()


def read(v, regs):
    try:
        return int(v)
    except:
        return regs[v]


def parse(data, pt2=False):
    regs = {"a": 0, "b": 0, "c": 0, "d": 0}

    if pt2:
        regs["c"] = 1

    c = 0

    while c <= len(data) - 1:
        instr = data[c]
        cmd, *args = instr.split()

        if cmd.startswith("inc"):
            regs[args[0]] += 1
        elif cmd.startswith("dec"):
            regs[args[0]] -= 1
        elif cmd.startswith("cpy"):
            out, dest = args
            regs[dest] = read(out, regs)
        elif cmd.startswith("jnz"):
            check, dist = args
            if read(check, regs) != 0:
                c += read(dist, regs) - 1

        c += 1

    return regs


# pt 1
r = parse(data)
print(r["a"])

# pt 2
r = parse(data, True)
print(r["a"])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day25 2016
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from itertools import cycle

data = aoc.read_input()


def read(v, regs):
    return regs[v] if v in regs else int(v)


def parse(data, regs, steps):
    c = 0

    for _ in range(steps):
        instr = data[c]
        cmd, *args = instr.split()

        if cmd.startswith("inc"):
            regs[args[0]] += 1
        elif cmd.startswith("dec"):
            regs[args[0]] -= 1
        elif cmd.startswith("cpy"):
            out, dest = args
            if dest is int:
                continue
            regs[dest] = read(out, regs)
        elif cmd.startswith("jnz"):
            check, dist = args
            if read(check, regs) != 0:
                c += read(dist, regs) - 1
        elif cmd.startswith("tgl"):
            pointer = regs[args[0]] + c

            if pointer > len(data) - 1:
                c += 1
                continue

            line = data[pointer]
            if len(line.split()) == 2:
                if "inc" in data[pointer]:
                    data[pointer] = line.replace("inc", "dec")
                else:
                    instruction, arg = line.split()
                    data[pointer] = " ".join(["inc", arg])

            if len(line.split()) > 2:
                if "jnz" in data[pointer]:
                    data[pointer] = line.replace("jnz", "cpy")
                else:
                    instruction, *arg = line.split()
                    data[pointer] = " ".join(["jnz", *arg])

        elif cmd.startswith("out"):
            yield read(args[0], regs)

        c += 1

    return regs


def repeats(a, code, steps=10**6, sigexit=100):
    sig = parse(code, {"a": a, "b": 0, "c": 0, "d": 0}, steps)

    for i, (sig, expected) in enumerate(zip(sig, cycle((0, 1)))):
        if sig != expected:
            return False
    return i >= sigexit


# pt 1
print(aoc.first(a for a in range(1, 10**5) if repeats(a, data)))

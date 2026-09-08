#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day23 2016
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc


def read(v, regs):
    try:
        return int(v)
    except:
        return regs[v]


def parse(data, regs):
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

        c += 1

    return regs


# pt 1
r = parse(list(aoc.read_input()), {"a": 7, "b": 0, "c": 0, "d": 0})
print(r["a"])

# pt 2
r = parse(list(aoc.read_input()), {"a": 12, "b": 0, "c": 0, "d": 0})
print(r["a"])

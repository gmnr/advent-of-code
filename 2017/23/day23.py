#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day23 2017
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import defaultdict as dd
from math import sqrt


def parse_line(line):
    line = line.split()
    instr, reg, val = line
    if val[-1].isdigit():
        return (instr, reg, int(val))
    else:
        return (instr, reg, val)


def run(data, pt2=False):
    c = 0
    regs = {v: 0 for v in "abcdefgh"}
    mul_invoc = 0

    while c < len(data):
        program = parse_line(data[c])
        instr, reg, val = program[0], program[1], program[-1]
        val = val if isinstance(val, int) else regs[val]

        if instr == "set":
            regs[reg] = val
        elif instr == "sub":
            regs[reg] -= val
        elif instr == "mul":
            regs[reg] = regs[reg] * val
            mul_invoc += 1
        else:
            amount = int(reg) if reg.isdigit() else regs[reg]
            if amount != 0:
                c += val
                continue
        c += 1

    return mul_invoc


def prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


# pt1
print(run(data))
# pt2
reg_b = 109900
reg_c = 126900
reg_h = 0

for reg_b in range(109900, reg_c + 1, 17):
    if not prime(reg_b):
        reg_h += 1
print(reg_h)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 08 2017
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import defaultdict as dd
import operator as o

regs = dd(int)

operators = {">": o.gt, "<": o.lt, "==": o.eq, ">=": o.ge, "<=": o.le, "!=": o.ne}

maxes = []


def parseInst(instruction):
    oper, condition = instruction.split(" if ")
    target, operator, t_val = condition.split()
    reg, cmd, val = oper.split()
    return (reg, cmd, int(val), target, operator, int(t_val))


def command(reg, cmd, val):
    if cmd == "inc":
        regs[reg] += val
    else:
        regs[reg] -= val
    maxes.append(regs[reg])


for inst in data:
    reg, cmd, val, target, op, t_val = parseInst(inst)
    if operators[op](regs[target], t_val):
        command(reg, cmd, val)

print(max(regs.values()))
print(max(maxes))

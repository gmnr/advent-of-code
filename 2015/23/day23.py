#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day23 2015
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()


def half(instr, reg):
    r = instr[-1]
    reg[r] = int(reg[r] / 2)


def triple(instr, reg):
    r = instr[-1]
    reg[r] = reg[r] * 3


def increment(instr, reg):
    r = instr[-1]
    reg[r] += 1


def jump(instr, reg):
    off = int(instr[-1])
    return off


def even(instr, reg):
    r = instr[1][:-1]
    off = int(instr[-1])
    if reg[r] % 2 == 0:
        return off


def one(instr, reg):
    r = instr[1][:-1]
    off = int(instr[-1])
    if reg[r] == 1:
        return off


def exec(line):
    ops = {
        "hlf": half,
        "tpl": triple,
        "inc": increment,
        "jmp": jump,
        "jie": even,
        "jio": one,
    }

    instr = line.split()
    cmd = instr[0]
    out = ops[cmd](instr, registers)
    if cmd in ["jmp", "jie", "jio"]:
        return out


def run(data, regs):
    c = 0
    while c < len(data):
        out = exec(data[c])
        if out:
            c += out
        else:
            c += 1
    return regs["b"]


# pt1
registers = {"a": 0, "b": 0}
print(run(data, registers))
# pt2
registers = {"a": 1, "b": 0}
print(run(data, registers))

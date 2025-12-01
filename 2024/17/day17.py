#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day17 2024
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc

test = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

data = aoc.read_input(sep="\n\n")


A, B, C = aoc.ints(data[0])
reg = list(aoc.ints(data[1]))


def adv(c):
    global A
    global B
    global C
    if c <= 3:
        op = c
    elif c == 4:
        op = A
    elif c == 5:
        op = B
    elif c == 6:
        op = C
    A = A // 2**op
    return False


def bxl(c):
    global A
    global B
    global C
    B = B ^ c
    return False


def bst(c):
    global A
    global B
    global C
    if c <= 3:
        op = c
    elif c == 4:
        op = A
    elif c == 5:
        op = B
    elif c == 6:
        op = C
    B = op % 8
    return False


def jnz(c):
    global A
    global B
    global C
    if A == 0:
        return False
    return True


def bxc(c):
    global A
    global B
    global C
    B = B ^ C
    return False


def out(c):
    global A
    global B
    global C
    if c <= 3:
        op = c
    elif c == 4:
        op = A
    elif c == 5:
        op = B
    elif c == 6:
        op = C
    op = op % 8
    outs.append(op)
    return False


def bdv(c):
    global A
    global B
    global C
    if c <= 3:
        op = c
    elif c == 4:
        op = A
    elif c == 5:
        op = B
    elif c == 6:
        op = C
    B = A // 2**op
    return False


def cdv(c):
    global A
    global B
    global C
    if c <= 3:
        op = c
    elif c == 4:
        op = A
    elif c == 5:
        op = B
    elif c == 6:
        op = C
    C = A // 2**op
    return False


CODES = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

# pt 1
p = 0
outs = []
while p < len(reg):
    opcode = reg[p]
    combo = reg[p + 1]

    if CODES[opcode](combo):
        p = combo

    else:
        p += 2
print(",".join([str(x) for x in outs]))

# pt 2
res = outs
print(reg)

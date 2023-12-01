#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day16 2018
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data, prg = f.read().split("\n\n\n\n")


def parse(data):
    clusters = data.split("\n\n")
    container = []
    for c in clusters:
        reg_b, instr, reg_a = c.split("\n")
        _, reg_b = reg_b.split(": [")
        _, reg_a = reg_a.split(":  [")
        reg_b = reg_b[:-1].split(", ")
        instr = instr.split(" ")
        reg_a = reg_a[:-1].split(", ")

        reg_b = [int(x) for x in reg_b]
        instr = [int(x) for x in instr]
        reg_a = [int(x) for x in reg_a]

        container.append((reg_b, instr, reg_a))
    return container


def addr(a, b, c, reg):
    reg[c] = reg[a] + reg[b]
    return reg


def addi(a, b, c, reg):
    reg[c] = reg[a] + b
    return reg


def mulr(a, b, c, reg):
    reg[c] = reg[a] * reg[b]
    return reg


def muli(a, b, c, reg):
    reg[c] = reg[a] * b
    return reg


def banr(a, b, c, reg):
    reg[c] = reg[a] & reg[b]
    return reg


def bani(a, b, c, reg):
    reg[c] = reg[a] & b
    return reg


def borr(a, b, c, reg):
    reg[c] = reg[a] | reg[b]
    return reg


def bori(a, b, c, reg):
    reg[c] = reg[a] | b
    return reg


def setr(a, b, c, reg):
    reg[c] = reg[a]
    return reg


def seti(a, b, c, reg):
    reg[c] = a
    return reg


def gtir(a, b, c, reg):
    if a > reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg


def gtri(a, b, c, reg):
    if reg[a] > b:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg


def gtrr(a, b, c, reg):
    if reg[a] > reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg


def eqir(a, b, c, reg):
    if a == reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg


def eqri(a, b, c, reg):
    if reg[a] == b:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg


def eqrr(a, b, c, reg):
    if reg[a] == reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg


def check_codes(sample):
    _, code, reg_out = sample
    op_codes = [
        addr,
        addi,
        mulr,
        muli,
        banr,
        bani,
        borr,
        bori,
        setr,
        seti,
        gtir,
        gtri,
        gtrr,
        eqir,
        eqri,
        eqrr,
    ]
    count = 0

    for i in op_codes:
        reg_in = sample[0].copy()
        if reg_out == i(*code[1:], reg_in):
            count += 1
        else:
            continue

    return count


# pt 1
samples = parse(data)
print(len([check_codes(x) for x in samples if check_codes(x) >= 3]))


# pt 2
def solve(prg, codes):
    registers = [int(x) for x in "0000"]

    for i in prg.split("\n")[:-1]:
        i = [int(x) for x in i.split(" ")]
        kegisters = codes[i[0]](*i[1:], registers)

    return registers[0]


def resolve_codes(samples):
    codes = {}
    op_codes = [
        addr,
        addi,
        mulr,
        muli,
        banr,
        bani,
        borr,
        bori,
        setr,
        seti,
        gtir,
        gtri,
        gtrr,
        eqir,
        eqri,
        eqrr,
    ]

    while len(codes) < 15:
        for sample in samples:
            _, code, reg_out = sample
            executions = []

            for i in op_codes:
                reg_in = sample[0].copy()
                if reg_out == i(*code[1:], reg_in):
                    last_executed = code[0]
                    executions.append(i)

            if len(executions) == 1:
                codes[last_executed] = executions[0]
                op_codes.remove(executions[0])

    return codes


codes = resolve_codes(samples)
print(solve(prg, codes))

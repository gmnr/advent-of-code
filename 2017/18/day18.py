#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day18 2017
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import defaultdict as dd, deque


def parse_line(line):
    line = line.split()
    if len(line) == 3:
        instr, reg, val = line
        if val[-1].isdigit():
            return (instr, reg, int(val))
        else:
            return (instr, reg, val)
    else:
        instr, reg = line
        return (instr, reg)


def run(data):
    c = 0
    played = []
    registers = dd(int)

    while True:
        program = parse_line(data[c])
        instr, reg, val = program[0], program[1], program[-1]
        val = val if isinstance(val, int) else registers[val]

        if instr == "snd":
            played.append(registers[reg])
        elif instr == "set":
            registers[reg] = val
        elif instr == "add":
            registers[reg] += val
        elif instr == "mul":
            registers[reg] *= val
        elif instr == "mod":
            registers[reg] = registers[reg] % val
        elif instr == "rcv":
            if registers[reg] > 0:
                return played[-1]
        else:
            if registers[reg] > 0:
                c += val
                if c > len(data) or c < 0:
                    return played[-1]
                continue
        c += 1


class Program:
    def __init__(self, c, _id):
        self.status = "run"
        self.c = c
        self.registers = dd(int)
        self._id = _id
        self.registers["p"] = self._id
        self.counter = 0


def run_both(data):
    A = Program(0, 0)
    B = Program(0, 1)
    q = {0: deque([]), 1: deque([])}

    while A.status != "wait" or B.status != "wait":
        run_step(A, data, q)
        run_step(B, data, q)
    return B.counter


def run_step(prg, data, q):
    this = prg._id
    other = 1 - this

    program = parse_line(data[prg.c])
    instr, reg, val = program[0], program[1], program[-1]

    if type(val) == int or val.isdigit():
        val = val
    else:
        val = prg.registers[val]

    if instr == "snd":
        reg = int(reg) if reg in "0123456789" else prg.registers[reg]
        q[other].append(reg)
        prg.counter += 1
    elif instr == "set":
        prg.registers[reg] = val
    elif instr == "add":
        prg.registers[reg] += val
    elif instr == "mul":
        prg.registers[reg] *= val
    elif instr == "mod":
        prg.registers[reg] = prg.registers[reg] % val
    elif instr == "rcv":
        if not q[this]:
            prg.status = "wait"
            return
        else:
            prg.status = "run"
            val = q[this].popleft()
            prg.registers[reg] = val
    elif instr == "jgz":
        amount = int(reg) if reg.isdigit() else prg.registers[reg]
        if amount > 0:
            prg.c += val
            if prg.c > len(data) or prg.c < 0:
                print("should terminate")
            return
    prg.c += 1


# pt 1
print(run(data))
# pt 2
print(run_both(data))

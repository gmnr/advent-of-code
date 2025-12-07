#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 08 2020
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import defaultdict as dd


def solveStop(data, beforeloop=False):
    seen = dd(int)
    acc = 0
    cur = 0
    broken = False
    while cur < len(data):
        instruction = data[cur]
        if cur in list(seen.keys()):
            broken = True
            break
        seen[cur] += 1
        inst, value = instruction.split()
        if inst == "acc":
            acc += int(value)
            cur += 1
        elif inst == "jmp":
            cur += int(value)
        else:
            cur += 1
    if broken and not beforeloop:
        return "looped"
    return acc


def howMany(data):
    count = 0
    for inst in data:
        cmd, val = inst.split()
        if cmd in ["jmp", "nop"]:
            count += 1
    return count


def swap(inst):
    if inst == "jmp":
        return "nop"
    else:
        return "jmp"


def bruteForce(data):
    executions = howMany(data)
    seen = dd(int)
    idx = 0
    for i in range(executions):
        seen = dd(int)
        new_data = []
        new_data += data[:idx]
        for inst in data[idx:]:
            cmd, val = inst.split()
            if cmd == "acc":
                idx += 1
                new_data.append(inst)
            else:
                idx += 1
                cmd = swap(cmd)
                inst = " ".join([cmd, val])
                new_data.append(inst)
                new_data += data[idx:]
                val = solveStop(new_data)
                if val == "looped":
                    break
                else:
                    return val


# pt 1
print(solveStop(data, True))
# pt 2
print(bruteForce(data))

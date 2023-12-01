#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 14 2020
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import defaultdict as dd
from itertools import product


def build_instr(data):
    instr = dd(list)
    for el in data:
        if el[:4] == "mask":
            mask = el.split(" = ")[1]
        elif el[:3] == "mem":
            mem = el.split("] = ")[0].split("[")[1]
            val = el.split(" = ")[1]
            instr[mask] += [(int(mem), int(val))]
    return instr


def build_memory_v1(instr):
    memory = dd(int)
    for k, v in instr.items():
        mask = k
        for calc in v:
            mem, val = calc
            memory[mem] = compute_mask(val, mask)
    return memory


def compute_mask(val, mask):
    res = ""
    mask = "0b" + mask
    bin_val = format(val, f"#0{len(mask)}b")
    for i, _ in enumerate(mask):
        if mask[i] == "X":
            res += bin_val[i]
            continue
        else:
            res += mask[i]
            continue
    return int(res, 2)


def build_memory_v2(instr):
    memory = dd(int)
    for k, v in instr.items():
        mask = k
        for calc in v:
            mem, val = calc
            mem = mask_mem(mem, mask)
            for addr in mem:
                memory[addr] = val
    return memory


def mask_mem(mem, mask):
    addrs = []
    res = ""
    mask = "0b" + mask
    bin_val = format(mem, f"#0{len(mask)}b")
    for i, _ in enumerate(mask):
        if mask[i] == "X":
            res += "f"
            continue
        elif mask[i] in ["0", "b"]:
            res += bin_val[i]
            continue
        else:
            res += "1"
            continue
    return [x for x in scramble(res)]


def scramble(binary):
    res = []
    float_idx = [i for i, val in enumerate(binary) if val == "f"]
    prod_rules = {k: [0, 1] for k in float_idx}
    products = [dict(zip(prod_rules, v)) for v in product(*prod_rules.values())]
    for rule in products:
        target = list(binary)
        for k, v in rule.items():
            target[k] = str(v)
        res.append("".join(target))
    return [int(x, 2) for x in res]


set_instr = build_instr(data)
# pt1
mem1 = build_memory_v1(set_instr)
print(sum([x for x in mem1.values()]))
# pt2
mem2 = build_memory_v2(set_instr)
print(sum([x for x in mem2.values()]))

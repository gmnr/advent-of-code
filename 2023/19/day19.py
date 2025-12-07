#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day19 2023
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from math import prod

data, ratings = aoc.read_input(sep="\n\n")


def get_ratings(ratings):
    for line in ratings.splitlines():
        yield {
            x[0]: int(x[1]) for x in map(lambda i: i.split("="), line[1:-1].split(","))
        }


ratings = get_ratings(ratings)
workflows = {}
for d in data.splitlines():
    key, instr = d.split("{")
    rules = instr[:-1].split(",")
    rules, final = rules[:-1], rules[-1]
    rules = (r.split(":") for r in rules)
    rules = [(e[0], e[1], int(e[2:]), n) for e, n in rules]
    workflows[key] = (rules, final)


def run(workflows, ratings):
    c = "in"

    while c != "A" and c != "R":
        rules, final = workflows[c]

        for var, instr, value, succ in rules:
            var = ratings[var]
            if instr == "<" and var < value:
                c = succ
                break
            if instr == ">" and var > value:
                c = succ
                break
        else:
            c = final

    if c == "A":
        return sum(ratings.values())
    return 0


# pt 1
total = sum(run(workflows, r) for r in ratings)
print(total)


# pt 2
def accepted(workflows, ranges, c="in"):
    if c == "A":
        return prod(hi - lo + 1 for lo, hi in ranges.values())

    if c == "R":
        return 0

    rules, final = workflows[c]
    total = 0

    for var, instr, value, succ in rules:
        lo, hi = ranges[var]

        if instr == "<":
            if lo < value:
                total += accepted(workflows, ranges | {var: (lo, value - 1)}, succ)

            if hi >= value:
                ranges[var] = (value, hi)

        else:
            if hi > value:
                total += accepted(workflows, ranges | {var: (value + 1, hi)}, succ)

            if lo <= value:
                ranges[var] = (lo, value)

    total += accepted(workflows, ranges, final)
    return total


print(accepted(workflows, {v: (1, 4000) for v in "xmas"}))

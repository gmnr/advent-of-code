#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day07 2024
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from itertools import product, zip_longest, chain

test = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

data = aoc.read_input()

# pt 1
total = 0
failed = []
for e in data:
    res, operands = e.split(": ")
    operands = operands.split()
    res = int(res)

    for op in product("*+", repeat=len(operands) - 1):
        eq = zip_longest(operands, op)
        merged = list(chain(*eq))[:-1]

        subtotal = eval("".join(merged[:3]))
        if len(merged) > 3:
            tail = merged[3:]
            for i, c in enumerate(tail):
                if i % 2 == 0:
                    subtotal = eval("".join([str(subtotal), *tail[i : i + 2]]))
                    if subtotal > res:
                        break

        if res == subtotal:
            total += subtotal
            break
print(total)

# pt 2
failed_total = 0
for e in data:
    res, operands = e.split(": ")
    operands = operands.split()
    res = int(res)

    for op in product("*+|", repeat=len(operands) - 1):
        eq = zip_longest(operands, op)
        merged = list(chain(*eq))[:-1]

        subtotal = merged[:3]
        if "|" in subtotal:
            subtotal = int(subtotal[0] + subtotal[2])
        else:
            subtotal = eval("".join(merged[:3]))
        if len(merged) > 3:
            tail = merged[3:]
            for i, c in enumerate(tail):
                if i % 2 == 0:
                    new_tail = [tail[i : i + 2]]
                    if "|" in new_tail[0]:
                        concat = new_tail[0][-1]
                        subtotal = int(str(subtotal) + str(concat))
                    else:
                        subtotal = eval("".join([str(subtotal), *tail[i : i + 2]]))
                    if subtotal > res:
                        break

        if res == subtotal:
            failed_total += res
            break
print(failed_total)

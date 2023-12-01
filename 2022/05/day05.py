#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day05 2022
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from copy import deepcopy

data = aoc.read_input(sep="\n\n")
schema, instructions = data


def parse_schema(schema):
    stack = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

    for line in schema.split("\n"):
        c = 1
        for n, i in enumerate(line):
            if n in range(1, len(line), 4):
                stack[c].append(i)
                c += 1

    for k, v in stack.items():
        v = "".join(v[::-1]).strip()
        stack[k] = list(v[1:])

    return stack


stack = parse_schema(schema)
instructions = [aoc.ints(x) for x in instructions.split("\n")]


def move(stack, instr, new_model=False):
    stack = deepcopy(stack)
    for i in instr:
        n, fr, to = i
        if not new_model:
            for _ in range(n):
                stack[to].append(stack[fr].pop())
        else:
            stack[to].extend(stack[fr][-n:])
            del stack[fr][-n:]
    return stack


def print_top_crates(stack):
    print("".join(x[-1] for x in stack.values()))


# pt 1
new_stack = move(stack, instructions)
print_top_crates(new_stack)

# pt 2
new_stack_new_model = move(stack, instructions, new_model=True)
print_top_crates(new_stack_new_model)

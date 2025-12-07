#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 18 2020
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

import operator


def parse(expr):
    stack = [[]]
    for i in expr:
        current_node = stack[-1]
        if i == "(":
            new_node = []
            current_node.append(new_node)
            stack.append(new_node)
        elif i == ")":
            stack.pop()
        elif not i.isspace():
            current_node.append(i)
    return stack[0]


def solve(expr):
    expr = [int(x) if isinstance(x, str) and x not in ["+", "*"] else x for x in expr]
    acc = 0
    operations = {"+": operator.add, "*": operator.mul}
    op = operator.add
    for i in expr:
        if i in ["+", "*"]:
            op = operations[i]
        elif isinstance(i, list):
            acc = op(acc, solve(i))
        else:
            acc = op(acc, i)
    return acc


# pt 1
ops1 = [solve(parse(x)) for x in data]
print(sum(ops1))
# pt 2
doctored_data = [
    "(" + eq.replace("(", "((").replace(")", "))").replace("*", ")*(") + ")"
    for eq in data
]
ops2 = [solve(parse(x)) for x in doctored_data]
print(sum(ops2))

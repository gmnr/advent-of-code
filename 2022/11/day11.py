#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day11 2022
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


import helper.advent as aoc
from operator import add, mul
from math import lcm

data = aoc.read_input(sep='\n\n')

class Monkey:

    def __init__(self, name, items, op, val, test, if_true, if_false):
        self.name = name
        self.items = list(items)
        self.op = op
        self.val = val
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.counter = 0

def parse(data):
    monkeys = []
    for i in data:
        args = []
        for l in i.splitlines():
            if l.startswith('  Op'):
                op, val = l.split()[-2:]
                if val.isdigit():
                    val = int(val)
            else:
                f = aoc.ints(l)
                if len(f) == 1:
                    args.append(f[0])
                else:
                    args.append(f)
        args.insert(2, val)
        args.insert(2, op)

        if isinstance(args[1], int):
            args[1] = args[1],

        monkeys.append(Monkey(*args))
    return monkeys

def monkey_business(monkeys, rounds, not_worry=False):
    if not_worry:
        mod = lcm(*[m.test for m in monkeys])
    for _ in range(rounds):
        for m in monkeys:
            for i in m.items:
                if m.op[0] == '+':
                    oper = add
                else:
                    oper = mul

                if isinstance(m.val, str):
                    val = i
                else:
                    val = m.val

                item = oper(i, val)
                m.counter += 1

                if not_worry:
                    item = item % mod
                else:
                    item = item // 3

                if item % m.test == 0:
                    monkeys[m.if_true].items.append(item)
                else:
                    monkeys[m.if_false].items.append(item)
            m.items = []
    return mul(*sorted([m.counter for m in monkeys])[-2:])

# pt 1
monkeys = parse(data)
print(monkey_business(monkeys, 20))

# pt 2
# monkeys = parse(data)
print(monkey_business(monkeys, 10_000, True))

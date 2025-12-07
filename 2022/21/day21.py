#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day21 2022
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc

test = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""

data = aoc.read_input(test)


def parse(data):
    monkeys = {}
    values = {}
    for line in data:
        key, addend = line.split(": ")
        if addend.isdigit():
            values[key] = int(addend)
        monkeys[key] = addend.split()
    return values, monkeys


values, monkeys = parse(data)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day10 2022
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


from collections import defaultdict
import helper.advent as aoc

data = aoc.read_input()

def parse(data):
    cycles = defaultdict(int)
    reg = 1
    c = 0

    for l in data:

        if l.startswith('addx'):
            _, amt = l.split()
            for _ in range(2):
                c += 1
                cycles[c] = reg
            reg += int(amt)

        elif l.startswith('noop'):
                c += 1
                cycles[c] = reg

    return cycles

# pt 1
cycles = parse(data)
print(sum(x * cycles[x] for x in (20, 60, 100, 140, 180, 220)))

# pt 2
s = ''
for i in range(len(cycles)+1):
    if i % 40 == 0 and i != 0:
        print(s)
        s = ''

    pos = cycles[i+1]
    sprite = [pos-1, pos, pos+1]

    if i < 40:
        c = i
    else:
        c = i % 40

    if c in sprite:
        s += '#'
    else:
        s += '.'

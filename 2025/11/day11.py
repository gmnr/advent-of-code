#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day11 2025
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc

test = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

data = aoc.read_input(test)

# pt 1
paths = {}
for line in data:
    c, p = line.split(':')
    paths[c] = p.split()


stack = ['you']
target = 'out'
count = 0

while stack:
    node = stack.pop()
    next_nodes = paths[node]

    for n in next_nodes:

        if n == target:
            count += 1
            continue

        stack.append(n)
print(count)

# pt 2

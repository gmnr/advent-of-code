#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 13 2020
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

from collections import defaultdict as dd
from math import ceil, floor, gcd

timetable = dd(int)

depart = int(data[0])
buses = [int(x) for x in [y for y in data[1].split(',') if y != "x"]]

for bus in buses:
    div = depart / bus
    lower = floor(div)
    higher = ceil(div)
    timetable[lower * bus] = bus
    timetable[higher * bus] = bus

def lcm(x, y): return x * y // gcd(x, y)

def find_first(first, second, offset):
    x = 0
    y = 0

    while second * y - first * x != offset:
        if second * y > first * x: x += 1
        else: y += 1

    return lcm(first, second), first * x

# pt1
match = min([k for k in timetable.keys() if k > depart])
wait = match - depart
print(wait * timetable[match])
# pt2
times = [x for x in data[1].split(',')]
times = [int(x) if x != "x" else 0 for x in times]
table = [(i, val) for i, val in enumerate(times) if val != 0]
val1 = table[0][1]
off, val2 = table[1]
mult, coeff = find_first(val1, val2, off)
for dep in table[2:]:
    print(dep)
    i = 1
    while True:
        t = mult * i + coeff
        if (t + dep[0]) % dep[1] == 0:
            coeff = t
            mult *= dep[1]
            break
        i += 1
print(t)

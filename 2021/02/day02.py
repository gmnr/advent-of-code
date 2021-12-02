#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day02 2021
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

pos = 0
depth = 0
aim = 0
new_depth = 0

for cmd in data:
    inst, value = cmd.split(' ')
    value = int(value)
    
    if inst == 'forward':
        pos += value
        new_depth += aim * value
    elif inst == 'down':
        depth += value
        aim += value
    else:
        depth -= value
        aim -= value

# pt 1
print(pos * depth)

# pt 2
print(pos * new_depth)

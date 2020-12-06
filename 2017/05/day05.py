#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 05 2017
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().split('\n')[:-1]
    data = [int(x) for x in data]

def part1(data):
    steps = 0
    p = 0
    n = 0
    while True:
        try:
            n = data[p]
            data[p] += 1
            p += n
            steps += 1
        except IndexError:
            return steps

def part2(data):
    steps = 0
    p = 0
    n = 0
    while True:
        try:
            n = data[p]
            if data[p] >= 3:
                data[p] -= 1
            else:
                data[p] += 1
            p += n
            steps += 1
        except IndexError:
            return steps

# pt 1
print(part1(data))
# pt 2
print(part2(data))

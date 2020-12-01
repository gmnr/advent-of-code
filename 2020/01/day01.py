#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 01
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().split('\n')[:-1]

numbs = [int(x) for x in data]
numbs = sorted(numbs)

def find2020_part1():
    for i in range(len(numbs)):
        for j in reversed(range(len(numbs))):
            if numbs[i] + numbs[j] > 2500:
                continue
            else:
                if numbs[i] + numbs[j] == 2500:
                    return numbs[i] * numbs[j]

def find2020_part2():
    for i in range(len(numbs)):
        for j in range(len(numbs)):
            for k in range(len(numbs)):
                if numbs[i] + numbs[j] + numbs[k] == 2020:
                    return numbs[i] * numbs[j] * numbs[k]

# part 1
print(find2020_part1())
print(find2020_part2())




#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day18 2021
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

from functools import reduce
from itertools import permutations

def parse(data):
    flatlist = []
    for line in data:
        flatline, depth = [], 0
        for c in line:
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            elif c.isdigit():
                flatline.append([int(c), depth])
        flatlist.append(flatline)
    return flatlist

def split(pair):
    for i, (num, depth) in enumerate(pair):
        if num < 10:
            continue
        down = num // 2
        up = num - down
        return True, pair[:i] + [[down, depth+1],[up, depth+1]] + pair[i+1:]
    return False, pair

def explode(pair):
    for i, ((num1, depth1), (num2, depth2)) in enumerate(zip(pair, pair[1:])):
        if depth1 < 5 or depth1 != depth2:
            continue
        if i > 0:
            pair[i - 1][0] += num1
        if i < len(pair) - 2:
            pair[i + 2][0] += num2
        return True, pair[:i] + [[0, depth1 - 1]] + pair[i + 2:] 
    return False, pair

def add(a, b):
    pair = [[num, depth+1] for num,depth in a + b]
    while True:
        change, pair = explode(pair)
        if change:
            continue
        change,pair = split(pair)
        if not change:
            break
    return pair

def magnitude(pair):
    while len(pair) > 1:
        for i, ((num1, depth1), (num2, depth2)) in enumerate(zip(pair, pair[1:])):
            if depth1 != depth2:
                continue
            val = num1 * 3 + num2 * 2
            pair = pair[:i]+[[val, depth1-1]]+pair[i+2:]
            break
    return pair[0][0]

flatlist = parse(data)
# pt 1
print(magnitude(reduce(add, flatlist)))
# pt 2
print(max(magnitude(add(a, b)) for a, b in permutations(flatlist, 2)))

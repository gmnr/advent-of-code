#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Soluton for day17 2015
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

from itertools import combinations
from collections import defaultdict as dd

eggnog = 150
containers = [int(x) for x in data]

def solve(containers, lim):
    sol = dd(int)

    for i in range(2, len(containers)):
        comb = combinations(containers, i)
        summed = [sum(x) for x in comb]
        for x in summed:
            if x == lim:
                sol[i] += 1
    return sol

# pt 1
sol = solve(containers, eggnog)
print(sum(sol.values()))
# pt 2
least = min(sol.keys())
print(sol[least])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 02 2015
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

from itertools import combinations
from operator import mul
from functools import reduce

def wrapping(lst):
    lst = [int(x) for x in lst]
    p = combinations(lst, 2)
    m = [mul(*x) for x in p]
    return sum(m) * 2 + min(m)

def ribbon(lst):
    lst = sorted([int(x) for x in lst])
    c = reduce(mul, lst)
    m1, m2, _ = lst
    return c + 2 * (m1 + m2)

measures = [x.split('x') for x in data]
wrapping = [wrapping(x) for x in measures]
ribbon = [ribbon(x) for x in measures]
print(sum(wrapping))
print(sum(ribbon))

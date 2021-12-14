#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day14 2021
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    template, recipe = f.read().split('\n\n')

from collections import Counter

elements = Counter(template)
pairs = Counter([a+b for a,b in zip(template, template[1:])])
recipe = dict(l.split(' -> ') for l in recipe.splitlines())

for _ in range(40):
    old = pairs.copy()
    for (a, b), c in recipe.items():
        count = old[a+b]
        pairs[a+b] -= count
        pairs[a+c] += count
        pairs[c+b] += count
        elements[c] += count
    # pt 1
    if _ == 9:
        print(elements.most_common()[0][1] - elements.most_common()[-1][1])

# pt 2
print(elements.most_common()[0][1] - elements.most_common()[-1][1])

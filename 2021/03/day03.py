#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day03 2021
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

from collections import Counter

def transpose(data):
    return list(map(list, zip(*data)))

def find_life_support_ratings(data, kind):
    if kind == 'oxygen':
        m = max
    else:
        m = min
    rating = ''
    idx = 0
    while len(data) > 1:
        transposed = transpose(data)
        t = transposed[idx]
        vals = Counter(t)
        if len(vals) == 1:
            rating += list(vals.keys())[0]
        elif len(set(vals.values())) == 1 and kind == 'oxygen':
            rating += '1'
        elif len(set(vals.values())) == 1 and kind != 'oxygen':
            rating += '0'
        else:
            rating += m(vals, key=vals.get)
        idx += 1
        data = [x for x in data if x.startswith(rating)]
    return data[0]

# pt 1
gamma = ''
for t in transpose(data):
    vals = Counter(t)
    gamma += max(vals, key=vals.get)
epsilon = ''.join(['1' if x == '0' else '0' for x in gamma])
gamma, epsilon = int(gamma, 2), int(epsilon, 2)
print(gamma * epsilon)

# pt 2
oxygen_gen = find_life_support_ratings(data, 'oxygen')
co2_scrubber = find_life_support_ratings(data, 'co2_scrubber')
oxygen_gen, co2_scrubber = int(oxygen_gen, 2), int(co2_scrubber, 2)
print(oxygen_gen * co2_scrubber)

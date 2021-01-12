#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day21 2017
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

from itertools import chain, combinations
from math import sqrt

def parse_rules(data):
    rules = {}
    for rule in data:
        key, value = rule.split(' => ')
        value = tuple(list(x) for x in value.split('/'))
        rules[key] = value
    return rules

def stringify(pattern):
    return '/'.join([''.join(x) for x in pattern])

def rotate90(pattern):
    return list(zip(*pattern[::-1]))

def rotations(pattern):
    yield pattern
    for _ in range(3):
        pattern = rotate90(pattern)
        yield pattern

def orientations(pattern):
    yield from rotations(pattern)
    yield from rotations(pattern[::-1])

def decompose(pattern):
    if len(pattern[0]) in [2, 3]: return pattern

    elif len(pattern) %  2 == 0:
        stripes = [[v, pattern[i+1]] for i, v in enumerate(pattern) if i % 2 == 0]

        pattern = []
        for stripe in stripes:
            unord_stripe = list(zip(*stripe))
            unord_stripe = [[v, unord_stripe[i+1]] for i, v in enumerate(unord_stripe) if i % 2 == 0]
            for couple in unord_stripe:
                pattern.append([[i, j] for i, j in zip(*couple)])

    elif len(pattern) % 3 == 0:
        stripes = [[v, pattern[i+1], pattern[i+2]] for i, v in enumerate(pattern) if i % 3 == 0]
        pattern = []
        for stripe in stripes:
            unord_stripe = list(zip(*stripe))
            unord_stripe = [[v, unord_stripe[i+1], unord_stripe[i+2]] for i, v in enumerate(unord_stripe) if i % 3 == 0]
            for couple in unord_stripe:
                pattern.append([[i, j, k] for i, j, k in zip(*couple)])

    return pattern

def compose(quads):

    item_len = len(quads[0][0])
    size = int(sqrt(len(quads)))
    pattern = []
    stripes = [quads[x:x+size] for x in range(0, len(quads), size)]

    for s in stripes:
        pattern.append([[x] for x in zip(*s)])

    res = []
    for ext in pattern:
        for el in ext:
            el = [list(chain.from_iterable(i)) for i in el]
            res.append(el)

    return [item for sublist in res for item in sublist]

def count_pixels(pattern):
    return sum(1 for x in [i for sub in pattern for i in sub] if x == '#')

def step(pattern, iterations):
    for _ in range(iterations):
        if len(pattern) % 2 == 0 or len(pattern) % 3 == 0:
            perm = decompose(pattern)
            if len(perm) in [2, 3]:
                for rot in orientations(perm):
                    if stringify(rot) in rules.keys():
                        pattern = list(rules[stringify(rot)])
                        break
            else:
                quads = []
                for quad in perm:
                    for rot in orientations(quad):
                        if stringify(rot) in rules.keys():
                            quads.append(rules[stringify(rot)])
                            break
                pattern = compose(quads)
    return pattern

pattern = """.#.
..#
###"""

rules = parse_rules(data)
pattern = [list(x) for x in pattern.splitlines()]
# pt 1
res1 = step(pattern, 5)
print(count_pixels(res1))
# pt 2
res2 = step(pattern, 18)
print(count_pixels(res2))

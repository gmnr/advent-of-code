#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day08 2021
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

def parse(data):
    res = []
    for l in data:
        pattern, output = l.split(' | ')
        pattern = pattern.split()
        output = output.split()
        res.append((pattern, output))
    return res

def compose_pattern(p):
    mapped = {}

    len_to_num = {
            2: 1,
            3: 7,
            4: 4,
            5: [2, 3, 5],
            6: [0, 6, 9],
            7: 8
    }

    for v in p:
        if len(v) in [2, 3, 4, 7]:
            mapped[v] = len_to_num[len(v)]
            if len(v) == 3:
                curr = v
    p = list(set(p) - set(mapped.keys()))

    for v in p:
        if len(set(v) - set(curr)) ==  2:
            mapped[v] = 3
        elif len(set(v) - set(curr)) ==  4:
            mapped[v] = 6
    p = list(set(p) - set(mapped.keys()))
    curr = {v:k for k, v in mapped.items()}.get(3)

    for v in p:
        if len(set(v) - set(curr)) ==  2:
            mapped[v] = 0
    p = list(set(p) - set(mapped.keys()))
    curr = {v:k for k, v in mapped.items()}.get(6)

    for v in p:
        if len(set(v) - set(curr)) ==  0:
            mapped[v] = 5
    p = list(set(p) - set(mapped.keys()))
    curr = {v:k for k, v in mapped.items()}.get(5)

    for v in p:
        if len(set(v) - set(curr)) ==  2:
            mapped[v] = 2
        else:
            mapped[v] = 9
    return mapped

def clock_to_num(output, k):
    output = [''.join(sorted(x)) for x in output]
    k = {''.join(sorted(key)): value for key, value in k.items()}
    s = ''
    for v in output:
        s += str(k[v])
    return int(''.join(s))

data = parse(data)

# # pt 1
count = 0
for l in data:
    out = l[1]
    for c in out:
        if len(c) in [2, 3, 4, 7]:
            count += 1
print(count)

# # pt 2
res = 0
for l in data:
    p, o = l[0], l[1]
    k = compose_pattern(p)
    res += clock_to_num(o, k)
print(res)

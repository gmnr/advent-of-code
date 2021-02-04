#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day07 2018
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

import re
from collections import defaultdict as dd

def parse(data):
    rules = dd(list)
    regex = r' ([A-Z]) '
    return [re.findall(regex, line) for line in data]

def prerequisite(rules):
    r = dd(list)
    for c in rules:
        p, n = c
        r[n] += p
    return r

def compose(rules):
    remaining = {x for pairs in rules for x in pairs}
    prereq = prerequisite(rules)
    def possible(c): return all(pre not in remaining for pre in prereq[c])
    while remaining:
        c = min(filter(possible, remaining))
        remaining.remove(c)
        yield c

def time(c):
    return 60 + ord(c) - ord('A')

def next_step(steps, l):
    return [s for s in steps if all(b != s for (_, b) in l)]

def schedule(rules, ws=5):
    steps = set([s[0] for s in rules] + [s[1] for s in rules])
    t = 0
    workers = [0 for _ in range(ws)]
    work = [None for _ in range(ws)]
    while steps or any(w > 0 for w in workers):
        cand = list(next_step(steps, rules))
        cand.sort()
        cand = cand[::-1]
        for i in range(ws):
            workers[i] = max(workers[i] - 1, 0)
            if workers[i] == 0:
                if work[i] is not None:
                    rules = [(a, b) for (a, b) in rules if a != work[i]]
                if cand:
                    n = cand.pop()
                    workers[i] = time(n)
                    work[i] = n
                    steps.remove(n)
        t += 1
    return t

# pt 1
rules = parse(data)
print(''.join(compose(rules)))
# pt 2
print(schedule(rules))

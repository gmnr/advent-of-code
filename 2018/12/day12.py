#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day12 2018
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'

with open('input.txt', 'r') as f:
    data = f.read()

def parse(data):
    state, rules = data.split('\n\n')
    _, state = state.split(': ')
    rules = rules.splitlines()
    ruleset = {}
    for rule in rules:
        note, out = rule.split(' => ')
        ruleset[note] = out
    return state, ruleset

init_state, rules = parse(data)

def sum_plants(curr):
    diff = (len(curr) - 100) // 2
    total = 0
    for i, c in enumerate(curr):
        if c == '#':
            total += (i - diff)
    return total

curr = init_state
prev_sum = sum_plants(init_state)
diffs = []
num_iters = 1000
for i in range(num_iters):
    if(i == 20):
        print(sum_plants(curr))
    curr = "...." + curr + "...."
    nx = ""
    for x in range(2, len(curr) - 2):
        sub = curr[x-2:x+3]
        nx += rules[sub]
    curr = nx
    currsum = sum_plants(curr)
    diff = currsum - prev_sum
    diffs.append(diff)
    if(len(diffs) > 100): diffs.pop(0)
    prev_sum = currsum

last100diff = sum(diffs) // len(diffs)
total = (50000000000 - num_iters) * last100diff + sum_plants(curr)
print(total)

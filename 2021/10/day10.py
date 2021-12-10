#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day10 2021
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

score  = {')': 3, ']': 57, '}': 1197, '>': 25137}
closer = {')': '(', ']': '[', '}': '{', '>': '<'}
opener = {'(': ')', '[': ']', '{': '}', '<': '>'}

illegals = []
suspended = []
for line in data:
    opens = []
    for c in line:
        if c in closer.values():
            opens.append(c)
        else:
            if closer[c] == opens[-1]:
                opens.pop()
            else:
                illegals.append(c)
                opens = []
                break
    if opens:
        suspended.append(opens)

def get_score(lst):
    score = 0
    for x in lst:
        score = (score * 5) + x
    return score

# pt 1
print(sum(score[x] for x in illegals))

# pt 2
new_score = {')': 1, ']': 2, '}': 3, '>': 4}
rev_suspended = []
for el in suspended:
    el.reverse()
    rev = [opener[x] for x in el]
    rev_suspended.append(rev)

scores = []
for el in rev_suspended:
    score = get_score([new_score[x] for x in el])
    scores.append(score)

median = len(scores) // 2
print(sorted(scores)[median])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 22 2020
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'

with open('input.txt', 'r') as f:
    data = f.read()

def score(cards):
    return sum(x * i for i,x in enumerate(cards[::-1], 1))

def play(p1, p2):
    while p1 and p2:
        check = list(zip(p1, p2))
        match = check[0]
        v1, v2 = match
        if v1 > v2:
            p1.extend([v1, v2])
            p1.pop(0)
            p2.pop(0)
        else:
            p2.extend([v2, v1])
            p1.pop(0)
            p2.pop(0)
    return p1 if p1 else p2

def recursive_play(p1, p2):
    seen = []
    while p1 and p2:
        if (tuple(p1), tuple(p2)) in seen:
            return 1, p1

        seen.append((tuple(p1), tuple(p2)))
        check = list(zip(p1, p2))
        match = check[0]
        v1, v2 = match
        if len(p1) - 1 >= v1 and len(p2) - 1 >= v2:
            pl, winner = recursive_play(p1.copy()[1:v1+1], p2.copy()[1:v2+1])
            if pl == 1:
                p1.extend([v1, v2])
                p1.pop(0)
                p2.pop(0)
            else:
                p2.extend([v2, v1])
                p1.pop(0)
                p2.pop(0)
        else:
            if v1  > v2:
                p1.extend([v1, v2])
                p1.pop(0)
                p2.pop(0)
            else:
                p2.extend([v2, v1])
                p1.pop(0)
                p2.pop(0)
    return (1, p1) if p1 else (2, p2)

# pt 1
p1, p2 = map(str.splitlines, data.split('\n\n'))
p1, p2 = list(map(int, p1[1:])), list(map(int, p2[1:]))
winner_normal = play(p1.copy(), p2.copy())
print(score(winner_normal))
# pt 2
pl, winner_recursive = recursive_play(p1.copy(), p2.copy())
print(score(winner_recursive))

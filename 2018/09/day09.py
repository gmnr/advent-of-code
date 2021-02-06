#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day09 2018
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read()

import re
from collections import deque, defaultdict as dd

pls, turns = [int(x) for x in re.findall(r'(\d+)', data)]

def game(players, turns):
    scores = dd(int)
    marbles = deque([0])

    for marble in range(1, turns + 1):
        if marble % 23 == 0:
            marbles.rotate(7)
            scores[marble % players] += marble + marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(marble)

    return max(scores.values())

# pt1
print(game(pls, turns))
# pt2
print(game(pls, turns * 100))

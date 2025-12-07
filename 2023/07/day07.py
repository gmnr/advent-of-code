#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day07 2023
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from collections import Counter
from functools import cmp_to_key
import re

data = aoc.read_input()


def five(s):
    return len(set(s)) == 1


def four(s):
    return 4 in Counter(s).values()


def full(s):
    c = list(Counter(s).values())
    return c == [2, 3] or c == [3, 2]


def three(s):
    c = list(Counter(s).values())
    return c == [3, 1, 1] or c == [1, 3, 1] or c == [1, 1, 3]


def two(s):
    c = list(Counter(s).values())
    return c == [2, 2, 1] or c == [2, 1, 2] or c == [1, 2, 2]


def one(s):
    return len(set(s)) == 4


def high(s):
    return len(set(s)) == 5


def sort_hands(h1, h2):
    labels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    kind = [five, four, full, three, two, one, high]
    p1, p2 = [x(h1) for x in kind], [x(h2) for x in kind]

    v1, v2 = p1.index(True), p2.index(True)

    if v1 > v2:
        return 1
    elif v1 < v2:
        return -1
    else:
        comparison = zip(h1, h2)
        for c in comparison:
            v1, v2 = labels.index(c[0]), labels.index(c[1])
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1


def sort_hands_pt2(h1, h2):
    labels = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    kind = [five, four, full, three, two, one, high]

    hands = []
    for h in [h1, h2]:
        if "J" in h:
            score = 999
            new_h = None
            for l in labels:
                cmp_h = re.sub("J", l, h)
                new_score = [x(cmp_h) for x in kind].index(True)
                if new_score < score:
                    score = new_score
                    new_h = cmp_h
            hands.append(new_h)

        else:
            hands.append(h)

    hj1, hj2 = hands

    p1, p2 = [x(hj1) for x in kind], [x(hj2) for x in kind]

    v1, v2 = p1.index(True), p2.index(True)

    if v1 > v2:
        return 1
    elif v1 < v2:
        return -1
    else:
        comparison = zip(h1, h2)
        for c in comparison:
            v1, v2 = labels.index(c[0]), labels.index(c[1])
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1


bids = {}
games = []
for d in data:
    hand, bid = d.split()
    bids[hand] = int(bid)
    games.append(hand)

# pt 1
score = 0
for rank, h in enumerate(sorted(games, key=cmp_to_key(sort_hands), reverse=True), 1):
    score += rank * bids[h]
print(score)

# pt 2
score = 0
for rank, h in enumerate(
    sorted(games, key=cmp_to_key(sort_hands_pt2), reverse=True), 1
):
    score += rank * bids[h]
print(score)

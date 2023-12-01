#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day13 2015
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import defaultdict as dd, deque
from itertools import permutations


def parse(data):
    mood = dd(list)

    for line in data:
        seated, rest = line.split(" would ")
        d, amount, *_, neighboor = rest.split()
        neighboor = neighboor[:-1]

        if d == "gain":
            amount = int(amount)
        else:
            amount = int(amount) * -1

        mood[seated].append((neighboor, amount))
    return mood


def score_configuration(conf, guests):
    score = 0
    for i in range(len(conf)):
        c = conf[i]
        conf.rotate(1)
        p = conf[i]
        conf.rotate(-2)
        n = conf[i]
        conf.rotate(1)

        mood = guests[c]
        mood = [x for x in mood if x[0] in [p, n]]
        score += sum(x[1] for x in mood)
    return score


# pt 1
guests = parse(data)
combs = [deque(x) for x in permutations(guests.keys())]
scores = [score_configuration(x, guests) for x in combs]
print(max(scores))
# pt 2
guest_list = guests.keys()
guests["Guido"] = []
for k in guest_list:
    guests[k].append(("Guido", 0))
    guests["Guido"].append((k, 0))
combs = [deque(x) for x in permutations(guests.keys())]
scores = [score_configuration(x, guests) for x in combs]
print(max(scores))

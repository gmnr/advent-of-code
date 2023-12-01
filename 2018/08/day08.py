#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day08 2018
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = [int(x) for x in f.read().split()]


def build_nodes(data):
    children, metas = data[:2]
    data = data[2:]
    scores = []
    totals = 0

    for i in range(children):
        total, score, data = build_nodes(data)
        totals += total
        scores.append(score)
    totals += sum(data[:metas])

    if children == 0:
        return (totals, sum(data[:metas]), data[metas:])
    else:
        return (
            totals,
            sum(scores[k - 1] for k in data[:metas] if k > 0 and k <= len(scores)),
            data[metas:],
        )


total, value, remaining = build_nodes(data)
# pt1
print(total)
# pt2
print(value)

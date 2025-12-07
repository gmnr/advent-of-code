#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Soluton for day24 2017
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import defaultdict as dd


def parse_components(data):
    components = dd(set)
    for pin in data:
        i, o = map(int, pin.split("/"))
        components[i].add(o)
        components[o].add(i)
    return components


def score_bridge(bridge):
    return sum(sum(x) for x in bridge)


def generate_bridges(comps, bridge):
    bridge = bridge or [(0, 0)]
    c = bridge[-1][1]
    for pin in comps[c]:
        if not ((c, pin) in bridge or (pin, c) in bridge):
            next_bridge = bridge + [(c, pin)]
            yield next_bridge
            yield from generate_bridges(comps, next_bridge)


components = parse_components(data)
bridges = []

for bridge in generate_bridges(components, None):
    bridges.append(bridge)
scores = [(len(x), score_bridge(x)) for x in bridges]

# pt 1
print(max(scores, key=lambda x: x[1])[1])
# pt2
length = max(scores, key=lambda x: x[0])[0]
longest = [x for x in scores if x[0] == length]
print(max(longest, key=lambda x: x[1])[1])

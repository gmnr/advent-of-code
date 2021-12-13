#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day25 2018
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

from collections import defaultdict

def parse(data):
    return [tuple(map(int, l.split(','))) for l in data]

def manhattan(a, b):
    return sum(abs(p1-p2) for p1, p2 in zip(a, b))

def build(coords):
    relations = defaultdict(list)
    for c1 in coords:
        for c2 in coords:
            if c1 == c2:
                continue
            elif manhattan(c1, c2) <= 3:
                relations[c1].append(c2)
        if c1 not in relations.keys():
            relations[c1] = []
    return relations

def link(nodes):
    constellations = []

    while nodes:
        first = next(iter(nodes))
        visited = [first]
        queue = [first]

        while queue:
            coord = queue.pop()

            for c in nodes[coord]:
                if c not in visited:
                    visited.append(c)
                    queue.append(c)

        constellations.append(visited)
        for i in visited:
            del nodes[i]

    return len(constellations)

# pt 1
nodes = build(parse(data))
print(link(nodes))

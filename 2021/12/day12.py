#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day12 2021
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

from collections import defaultdict, deque

def build_notes(data):
    nodes = defaultdict(list)
    for line in data:
        node1, node2 = line.split('-')
        if node2 != 'start':
            nodes[node1].append(node2)
        if node1 != 'start':
            nodes[node2].append(node1)
    return nodes

def find_paths(nodes, start, end):
    paths = deque([(start, set())])
    total = 0

    while paths:
        node, visited = paths.pop()

        if node == end:
            total += 1
            continue

        for n in nodes[node]:
            if n in visited and n.islower():
                continue

            paths.append((n, visited | {n}))

    return total

def find_paths2(nodes, start, end):
    paths = deque([(start, set(), False)])
    total = 0

    while paths:
        node, visited, twice_small = paths.pop()

        if node == end:
            total += 1
            continue

        for n in nodes[node]:
            if n not in visited or n.isupper():
                paths.append((n, visited | {n}, twice_small))
                continue

            if twice_small:
                continue

            paths.append((n, visited, True))

    return total

nodes = build_notes(data)
# pt 1
print(find_paths(nodes, 'start', 'end'))
# pt 2
print(find_paths2(nodes, 'start', 'end'))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day23 2024
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
import networkx as nx
from collections import defaultdict
from itertools import combinations

data = aoc.read_input()
graph = nx.Graph()

conn = defaultdict(set)
for l in data:
    c1, c2 = l.split("-")
    graph.add_edge(c1, c2)
    conn[c1].add(c2)
    conn[c2].add(c1)

# pt 1
res = 0
for a, b, c in combinations(conn.keys(), 3):
    if a.startswith("t") or b.startswith("t") or c.startswith("t"):
        if a in conn[b] and a in conn[c] and b in conn[c]:
            res += 1
print(res)

# pt 2
largest_subgraph = max(list(nx.find_cliques(graph)), key=len)
print(",".join(sorted(largest_subgraph)))

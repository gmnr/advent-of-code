#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day25 2023
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from itertools import combinations
import networkx as nx

data = aoc.read_input()

graph = nx.Graph()

for line in data:
    parent, children = line.split(": ")
    children = children.split()
    for c in children:
        graph.add_edge(parent, c, capacity=1)

for vert1, vert2 in combinations(list(graph.nodes), 2):
    nodes_removed, resulting_graphs = nx.minimum_cut(graph, vert1, vert2)
    if nodes_removed == 3:
        graph1, graph2 = resulting_graphs[0], resulting_graphs[1]
        print(len(graph1) * len(graph2))
        break

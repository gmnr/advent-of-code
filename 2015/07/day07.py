#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day07 2015
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import defaultdict as dd
import operator as o


def value(val, wires):
    return int(val) if val.isdigit() else wires[val]


def execute(key, comps, wires):
    cmds = {
        "NOT": o.not_,
        "AND": o.and_,
        "OR": o.or_,
        "LSHIFT": o.lshift,
        "RSHIFT": o.rshift,
    }
    if len(comps) == 1:
        wires[key] = value(comps[0], wires)
    elif len(comps) == 2:
        op, val = comps
        wires[key] = 65536 + ~(value(val, wires))
    else:
        val1, op, val2 = comps
        wires[key] = cmds[op](value(val1, wires), value(val2, wires))
    return wires


def build_graph(data):
    graph = {}
    for line in data:
        val, key = line.split(" -> ")
        graph[key] = val.split()
    return graph


def calculable(line, wires):
    keywords = ["NOT", "AND", "OR", "LSHIFT", "RSHIFT"]
    line = [x for x in line if x not in keywords]
    if all([x.isdigit() for x in line]):
        return True
    else:
        line = [x for x in line if not x.isdigit()]
        return all([x in wires.keys() for x in line])


graph = build_graph(data)


def solve(graph, wires, pt2=False):
    instr = [calculable(x, wires) for x in graph.values()]
    while not all(instr):
        for key in graph.keys():
            if pt2:
                if key == "b":
                    continue
            if calculable(graph[key], wires):
                wires = execute(key, graph[key], wires)
                instr = [calculable(x, wires) for x in graph.values()]
    for key in graph.keys():
        wires = execute(key, graph[key], wires)
    return wires


wires = dd(int)
wires = solve(graph, wires)
# pt 1
res1 = wires["a"]
print(res1)
# pt 2
wires = dd(int)
wires["b"] = res1
wires = solve(graph, wires, True)
res2 = wires["a"]
print(res2)

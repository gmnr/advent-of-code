#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day16 2022
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
import re

test = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""

data = aoc.read_input(test)


def parse(data):
    graph, rates = {}, {}
    regex = r"\d+|[A-Z]{2}"

    for line in data:
        node, val, *path = re.findall(regex, line)
        graph[node] = path
        rates[node] = val

    return graph, rates


def score(rates, opened_valves):
    res = 0
    for valve, time in opened_valves.items():
        res += rates[valve] * time
    return res


# pt1
graph, rates = parse(data)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day20 2023
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from collections import deque
from itertools import count
from math import lcm

data = aoc.read_input()

FF = {}
CJ = {}
graph = {}

for line in data:
    source, dest = line.split("->")
    source = source.strip()
    dest = dest.strip().split(", ")

    if source[0] == "%":
        source = source[1:]
        FF[source] = False
    elif source[0] == "&":
        source = source[1:]
        CJ[source] = {}

    graph[source] = dest

for source, dests in graph.items():
    for dest in dests:
        if dest in CJ:
            CJ[dest][source] = False


def traverse(graph, FF, CJ):
    q = deque([("button", "broadcaster", False)])
    hi = 0
    lo = 0

    while q:
        sender, receiver, pulse = q.popleft()

        if pulse:
            hi += 1
        else:
            lo += 1

        if receiver in FF:
            if pulse:
                continue
            next_pulse = FF[receiver] = not FF[receiver]

        elif receiver in CJ:
            CJ[receiver][sender] = pulse
            next_pulse = not all(CJ[receiver].values())

        elif receiver in graph:
            next_pulse = pulse

        else:
            continue

        for new_receiver in graph[receiver]:
            q.append((receiver, new_receiver, next_pulse))

    return hi, lo


def gen_pulses(graph, FF, CJ, sender, receiver, pulse):
    if receiver in FF:
        if pulse:
            return
        next_pulse = FF[receiver] = not FF[receiver]
    elif receiver in CJ:
        CJ[receiver][sender] = pulse
        next_pulse = not all(CJ[receiver].values())
    elif receiver in graph:
        next_pulse = pulse
    else:
        return

    for new_receiver in graph[receiver]:
        yield receiver, new_receiver, next_pulse


def find_period(graph, FF, CJ):
    periodic = set()

    for rx_src, d in graph.items():
        if d == ["rx"]:
            break

    for s, d in graph.items():
        if rx_src in d:
            periodic.add(s)

    for iteration in count(1):
        q = deque([("button", "broadcaster", False)])

        while q:
            sender, receiver, pulse = q.popleft()

            if not pulse:
                if receiver in periodic:
                    yield iteration

                    periodic.discard(receiver)
                    if not periodic:
                        return

            q.extend(gen_pulses(graph, FF, CJ, sender, receiver, pulse))


# pt 1
cnt_hi = cnt_lo = 0
for _ in range(1000):
    hi, lo = traverse(graph, FF, CJ)
    cnt_hi += hi
    cnt_lo += lo
print(cnt_hi * cnt_lo)

# pt 2
for f in FF:
    FF[f] = False
for inputs in CJ.values():
    for i in inputs:
        inputs[i] = False
print(lcm(*find_period(graph, FF, CJ)))

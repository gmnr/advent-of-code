#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day04 2018
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

import re
from datetime import datetime as dt
from collections import defaultdict as dd, Counter
from functools import reduce


def get_timestamp(line):
    regex = r"\[(.+)\]"
    return dt.fromisoformat(re.search(regex, line).group(1))


def turnize(data):
    turns = []
    turn = []
    for r in data:
        if "begins" in r:
            turns.append(turn)
            turn = [r]
        else:
            turn.append(r)
    turns.append(turn)
    return turns[1:]


# pt 1
data = sorted(data, key=lambda x: get_timestamp(x))
turns = turnize(data)
guards = dd(list)
for turn in turns:
    id_ = int(re.search(r"#(\d+)", turn[0]).group(1))
    for t in turn:
        if "asleep" in t:
            s = get_timestamp(t).minute
        elif "wakes" in t:
            e = get_timestamp(t).minute
            guards[id_] += list(range(s, e))

selected_guard = max(guards.keys(), key=lambda x: len(guards[x]))
minutes = Counter(guards[selected_guard])
minute = max(minutes.keys(), key=lambda x: minutes[x])
print(selected_guard * minute)
# pt 2
selected_guard = {"id_": 0, "t": 0, "m": 0}
for guard in guards:
    minutes = Counter(guards[guard])
    times = max(minutes.values())
    minute = max(minutes.keys(), key=lambda x: minutes[x])
    if times > selected_guard["t"]:
        selected_guard["id_"] = guard
        selected_guard["m"] = minute
        selected_guard["t"] = times
print(reduce(lambda x, y: x * y, [v for k, v in selected_guard.items() if k != "t"]))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 13 2017
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import defaultdict as dd


def scan_frq(i, width):
    return i % ((width * 2) - 2) == 0


def build_firewall(data):
    firewall = dd(int)
    for l in data:
        depth, width = [int(x) for x in l.split(": ")]
        firewall[depth] = width
    return firewall


def run_simul(data, offset=0):
    firewall = build_firewall(data)
    m_len = int(data[-1].split(": ")[0])
    res = []
    for i in range(m_len + 1):
        if firewall[i] == 0:
            continue
        else:
            if scan_frq(i + offset, firewall[i]):
                res.append((i, firewall[i]))
    return res


# pt 1
res = run_simul(data)
print(sum(map(lambda x: x[0] * x[1], res)))
# pt 2
off = 0
while True:
    if run_simul(data, off) == []:
        print(off)
        break
    off += 1

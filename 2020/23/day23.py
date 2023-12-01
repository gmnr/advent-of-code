#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day23 2020
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()[0]

from collections import deque
from itertools import islice, chain

cups = [int(x) for x in data]


def play(cups, turns):
    cups = deque(cups)
    low, high = min(cups), max(cups)
    p = 0

    for _ in range(turns):
        cups.rotate(-p)
        picks = list(islice(cups, 1, 4))
        cups = deque([x for x in cups if x not in picks])
        des = cups[0] - 1
        while des in picks + [0]:
            des -= 1
            if des < low:
                des = high
        d_p = cups.index(des) + 1
        for el in picks:
            cups.insert(d_p, el)
            d_p += 1
        p = 1

    one = cups.index(1)
    cups.rotate(-one)
    cups.popleft()
    return "".join(map(str, cups))


class Cup:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


def build_list(start):
    values = chain(start, range(10, 1_000_000 + 1))
    cups = [None] * (1_000_000 + 1)

    first_val = next(values)
    cups[first_val] = Cup(first_val)
    first = cups[first_val]
    prev = first

    for value in values:
        cur = cups[value] = Cup(value)
        cur.prev = prev
        prev.next = cur
        prev = cur

    cur.next = first
    return first, cups


def play_class(cur, cups, moves):
    high = len(cups) - 1

    for _ in range(moves):
        first = cur.next
        mid = first.next
        last = mid.next
        pick = (first.value, mid.value, last.value)
        cur.next = last.next

        if cur.value == 1:
            d = high
        else:
            d = cur.value - 1

        while d in pick:
            if d == 1:
                d = high
            else:
                d -= 1

        d = cups[d]
        first.prev = d
        last.next = d.next
        d.next = first
        cur = cur.next

    return cups[1].next.value * cups[1].next.next.value


# pt 1
print(play(cups, 100))
# pt 2
first, cups = build_list(cups)
print(play_class(first, cups, 10_000_000))

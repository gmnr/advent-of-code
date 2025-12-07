#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 15 2017
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

import re

regex = r"\d+"
v_A, v_B = [int(re.findall(regex, i)[0]) for i in data]


def gen(prev, factor, m=2147483647):
    while prev:
        prev = (prev * factor) % m
        yield prev


def to_bin(num):
    return bin(num)[-16:]


def compare(A, B, N):
    return sum([to_bin(a) == to_bin(b) for (a, b, _) in zip(A, B, range(N))])


def A(v):
    return gen(v, 16807)


def B(v):
    return gen(v, 48271)


def criteria(val, iterable):
    return (n for n in iterable if n % val == 0)


print(compare(A(v_A), B(v_B), 40_000_000))
print(compare(criteria(4, A(v_A)), criteria(8, B(v_B)), 5_000_000))

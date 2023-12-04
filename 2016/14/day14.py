#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day14 2016
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


from helper import advent as aoc
from functools import lru_cache
from hashlib import md5
import re

salt = aoc.read_input()[0].encode()


@lru_cache(1001)
def get_hash(i):
    return md5(salt + str(i).encode()).hexdigest()


def is_key(i, fn):
    three = re.search(r"(.)\1\1", fn(i))
    if three:
        five = three.group(1) * 5
        for x in range(i + 1, i + 1000):
            if re.search(five, fn(x)):
                return True


# pt 1
keys = cnt = 0
while keys < 64:
    if is_key(cnt, get_hash):
        keys += 1
    cnt += 1
print(cnt - 1)


# pt 2
@lru_cache(1001)
def stretch_hash(i):
    hash = md5(salt + str(i).encode()).hexdigest()
    for _ in range(2016):
        hash = md5(hash.encode()).hexdigest()
    return hash


keys = cnt = 0
while keys < 64:
    if is_key(cnt, stretch_hash):
        keys += 1
    cnt += 1
print(cnt - 1)

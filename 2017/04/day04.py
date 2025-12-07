#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
solution for day 4 2017
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]

import sys
from collections import Counter


def anagrams(words):
    for w in range(len(words)):
        n_list = list(words)
        n_list = n_list[w + 1 :]
        for s in n_list:
            if Counter(words[w]) == Counter(s):
                return True
    return False


counter1 = 0
counter2 = 0
for passph in data:
    words = passph.split()
    if len(set(words)) == len(words):
        counter1 += 1
        if not anagrams(words):
            counter2 += 1

# pt 1
print(counter1)
# pt 2
print(counter2)

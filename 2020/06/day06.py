#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 06 2020
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read()

import re

groups = re.split('\n\n', data)

def countAll(groups):
    counter = {}
    for i in range(len(groups)):
        counter[i] = 0
        group = groups[i]
        ans = set()
        people = group.split('\n')
        for person in people:
            for char in person:
                ans.add(char)
        counter[i] = len(ans)
    return sum(counter.values())

def countExclusive(groups):
    counter = {}
    for i in range(len(groups)):
        counter[i] = 0
        group = groups[i]
        ans = 0
        people = group.split('\n')
        seen = {}
        for person in people:
            for char in person:
                seen[char] = seen.get(char, 0) + 1
            for ch in seen.values():
                if ch == len(people):
                    ans += 1
        counter[i] = ans
    return sum(counter.values())

print(countAll(groups))
print(countExclusive(groups))

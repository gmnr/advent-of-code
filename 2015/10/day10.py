#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day10 2015
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().rstrip()

def find_adj(s):
    res = []
    wip = ''
    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            if i == 0:
                res.append(s[i])
            else:
                wip += s[i]
                res.append(wip)
                wip = ''
        else:
            wip += s[i]
    wip += s[-1]
    res.append(wip)
    return res

def look_say(comp):
    res = ''
    for el in comp:
        res += str(len(el)) + el[0]
    return res

data1 = data
data2 = data

# pt 1
for _ in range(40):
    data1 = find_adj(data1)
    data1 = look_say(data1)
print(len(data1))
# pt 2
for _ in range(50):
    data2 = find_adj(data2)
    data2 = look_say(data2)
print(len(data2))

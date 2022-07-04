#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day09 2016
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


from helper import advent as aoc

data = aoc.read_input()[0]

def expand(str):
    cnt = 0
    i = 0

    while i < len(str): 
        c = str[i]

        if c == '(':
            upper = str[i:].find(')') + i
            expansion = str[i+1:upper]
            seg, times = expansion.split('x')
            cnt += int(seg) * int(times)

            i = int(seg) + upper + 1
            continue

        # tidy up
        i += 1
        cnt += 1

    return cnt

def expand_recur(str):
    cnt = 0
    i = 0

    while i < len(str): 
        c = str[i]

        if c == '(':
            upper = str[i:].find(')') + i
            expansion = str[i+1:upper]
            seg, times = expansion.split('x')

            new_seg = str[upper+1:upper+int(seg)+1]

            cnt += int(times) * expand_recur(new_seg)

            i = int(seg) + upper + 1
            continue

        # tidy up
        i += 1
        cnt += 1

    return cnt

# pt 1
# print(expand(data))

# pt 2
print(expand_recur(data))

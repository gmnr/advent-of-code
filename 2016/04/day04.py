#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day04 2016
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


from helper import advent as aoc
from collections import Counter
from string import ascii_lowercase as ascii
import re

data = aoc.read_input()

def validate(str):
    regex = r'(.+?)(\d+)\[(\w+)\]'
    s, id, checksum = re.findall(regex, str)[0]
    cnt = Counter(s.replace('-', ''))

    most_common = cnt.most_common()

    check = sorted(most_common, key=lambda x: (-x[1], x[0]))
    check = ''.join([x[0] for x in check])[:5]

    if check == checksum:
        return int(id)
    return 0

def decypher(str):
    regex = r'(.+?)(\d+)\[(\w+)\]'
    s, id, _ = re.findall(regex, str)[0]
    offset = int(id) % len(ascii)

    new_message = ''
    for c in s:
        if c == '-':
            new_message += ' '
            continue
        start = ascii.index(c)
        if (start + offset) >= len(ascii):
            new_message += ascii[(start + offset) % len(ascii)]
        else:
            new_message += ascii[start + offset]
    return new_message[:-1], int(id)

# pt 1
sum = 0
real = []
for s in data:
    if val := validate(s):
        sum += val
        real.append(s)
print(sum)

# pt 2
for s in real:
    location, id = decypher(s)
    if location == 'northpole object storage':
        print(id)
        break

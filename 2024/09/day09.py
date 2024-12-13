#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day09 2024
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from collections import deque

data = aoc.read_input()[0]

files = {}
gaps = deque()
cnt = 0
for i, c in enumerate(data):
    if i % 2 == 0:
        files[cnt] = int(c)
        cnt += 1
    else:
        gaps.append(int(c))

frag = dict(files)
gap = deque(gaps)

# # pt 1
c = 0
i = 0
id_to_fill = deque(files.keys())
last = id_to_fill.pop()
checksum = 0
ls = []
max = sum(files.values())
while i < max:

    if files[c] == 0:

        if files[last] == 0:
            last = id_to_fill.pop()
        if gaps:
            g = gaps.popleft()
            for _ in range(g):
                checksum += i * int(last)
                ls.append(str(last))
                files[last] -= 1
                if files[last] == 0:
                    last = id_to_fill.pop()
                i += 1
                if i == max:
                    break

        c += 1

    else:
        for _ in range(files[c]):
            checksum += i * c
            ls.append(str(c))
            i += 1
        files[c] = 0
print(checksum)


# pt2
def compress(alloc, to_move):
    while to_move:
        check = to_move.pop()
        v = check[1]
        passed = set()
        for i, c in enumerate(alloc):
            if check in passed:
                break
            passed.add(c)
            if isinstance(c, int):
                if c >= v:
                    if c - v == 0:
                        payload = [check]
                    else:
                        payload = [check, c - v]
                    alloc = (
                        alloc[:i]
                        + payload
                        + [v if x == check else x for x in alloc[i + 1 :]]
                    )
                    new_alloc = []
                    nums = []
                    for x in alloc:
                        if isinstance(x, int):
                            nums.append(x)
                        else:
                            if nums == []:
                                new_alloc.append(x)
                                continue
                            else:
                                new_alloc.append(sum(nums))
                                nums = []
                            new_alloc.append(x)

                    alloc = new_alloc
                    break
    return alloc


alloc = []
to_move = deque()
for k, v in frag.items():
    to_move.append((k, v))
    alloc.append((k, v))
    if gap:
        alloc.append(gap.popleft())

res = compress(alloc, to_move)
i = 0
checksum = 0
for c in res:
    if isinstance(c, tuple):
        v, t = c
        for _ in range(t):
            checksum += v * i
            i += 1
    else:
        i += c
print(checksum)

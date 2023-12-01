#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day21 2018
"""

__author__ = "Guido Minieri"
__license__ = "GPL"

with open("input.txt", "r") as f:
    data = f.read().splitlines()


def run(num, pt1):
    seen = set()
    c = 0
    last_unique_c = -1

    while True:
        a = c | 65536
        c = num

        while True:
            c = (((c + (a & 255)) & 16777215) * 65899) & 16777215

            if 256 > a:
                if pt1:
                    return c
                else:
                    if c not in seen:
                        seen.add(c)
                        last_unique_c = c
                        break
                    else:
                        return last_unique_c
            else:
                a //= 256


num = int(data[8].split()[1])
# pt 1
print(run(num, True))
# pt 2
print(run(num, False))

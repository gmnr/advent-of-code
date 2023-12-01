#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day05 2016
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


from helper import advent as aoc
import hashlib

data = aoc.read_input()[0]


def find_password(door):
    password = ""
    for i in range(10**999):
        x = hashlib.md5(bytes(door + str(i), "utf-8")).hexdigest()
        if x.startswith("00000"):
            password += x[5]
            if len(password) == 8:
                return password


def find_password_v2(door):
    discovered = []
    password = [False] * 8
    for i in range(10**999):
        x = hashlib.md5(bytes(door + str(i), "utf-8")).hexdigest()
        if x.startswith("00000"):
            pos = x[5]
            if pos in "1234567890" and int(pos) < 8 and pos not in discovered:
                val = x[6]
                password[int(pos)] = val
                discovered.append(pos)
            if all(password):
                return "".join(password)


# pt 1
# pwd = find_password(data)
# print(pwd)

# pt 2
pwd = find_password_v2(data)
print(pwd)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 04 2015
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()[0]

from hashlib import md5


def hash_true(word, l):
    h = md5(word.encode()).hexdigest()
    return h[:l] == "0" * l


counter5 = 1
while not hash_true(data + str(counter5), 5):
    counter5 += 1
print(counter5)

counter6 = 1
while not hash_true(data + str(counter6), 6):
    counter6 += 1
print(counter6)

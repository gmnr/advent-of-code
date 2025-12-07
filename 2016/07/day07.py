#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day07 2016
"""

__author__ = "gmnr"
__license__ = "GPL"


from helper import advent as aoc
from itertools import chain
import re


data = aoc.read_input()


def is_palindrome(s, n, pt2=False):
    founds = []
    for i in range(len(s) - n + 1):
        chunk = s[i : i + n]

        if not pt2:
            if chunk == chunk[::-1]:
                if chunk != s[i] * n:
                    return True

        else:
            if chunk == chunk[::-1]:
                if chunk != s[i] * n:
                    founds.append(chunk)
    if founds:
        return founds


def tsl(data):
    cnt = 0
    for l in data:
        regex = r"\[(.+?)\]"
        inside = re.findall(regex, l)

        for i in inside:
            l = l.replace("[" + i + "]", " ")

        outside = l.split()
        inside_condition = any([is_palindrome(x, 4) for x in inside])
        outside_condition = any([is_palindrome(x, 4) for x in outside])
        if not inside_condition and outside_condition:
            cnt += 1
    return cnt


def ssl(data):
    cnt = 0
    for l in data:
        regex = r"\[(.+?)\]"
        inside = re.findall(regex, l)

        for i in inside:
            l = l.replace("[" + i + "]", " ")

        outside = l.split()

        insides = list(
            chain.from_iterable(
                [
                    is_palindrome(x, 3, True)
                    for x in inside
                    if is_palindrome(x, 3, True) is not None
                ]
            )
        )
        outsides = list(
            chain.from_iterable(
                [
                    is_palindrome(x, 3, True)
                    for x in outside
                    if is_palindrome(x, 3, True) is not None
                ]
            )
        )
        opp_outsides = [x[1:] + x[1] for x in outsides]

        for i in insides:
            if i in opp_outsides:
                cnt += 1
                break
    return cnt


# pt 1
print(tsl(data))

# pt 2
print(ssl(data))

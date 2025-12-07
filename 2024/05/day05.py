#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day05 2024
"""

__author__ = "gmnr"
__license__ = "GPL"


from collections import defaultdict
import math
import helper.advent as aoc


rules, updates = aoc.read_input(sep="\n\n")
updates = [aoc.ints(x) for x in updates.splitlines()]

rule_book = defaultdict(list)
for l in rules.splitlines():
    k, v = aoc.ints(l)
    rule_book[k].append(v)


def is_correct(upd, rule_book):
    for i, u in enumerate(upd):
        rules = rule_book[u]
        for r in rules:
            if r in upd:
                rj = upd.index(r)
                if rj < i:
                    return False
            else:
                continue
    return True


def fix_page(upd, rule_book):
    new_upd = list(upd)
    while not is_correct(new_upd, rule_book):
        again = False
        for i, u in enumerate(upd):
            rules = rule_book[u]
            for r in rules:
                if r in upd:
                    rj = upd.index(r)
                    if rj < i:
                        new_upd[rj] = u
                        new_upd[i] = r
                        again = True
                        break
            if again:
                upd = new_upd
                break
    return new_upd


# pt 1
cnt = 0
incorrect_pages = []
for u in updates:
    if is_correct(u, rule_book):
        cnt += u[math.ceil(len(u) // 2)]
    else:
        incorrect_pages.append(u)
print(cnt)

# pt 2
fixed_pages = []
for upd in incorrect_pages:
    fixed_pages.append(fix_page(upd, rule_book))
print(sum(u[math.ceil(len(u) // 2)] for u in fixed_pages))

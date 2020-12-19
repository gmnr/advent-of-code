#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 19 2020
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read()

import re

rules, msg = [x.splitlines() for x in data.split('\n\n')]

def build_rules(rules, part2=False):
    rule_book = {}
    rules = rules.copy()
    if part2: rules = update_rules(rules)
    while len(rules) != 0:
        for r in rules:
            cod, rule = r.split(": ")
            if rule.startswith('"'):
                rule_book[int(cod)] = rule.split('"')[1]
                rules.remove(r)
                continue
            cods = set([int(x) for x in rule.split() if x.isdigit()])
            if cods & set(rule_book.keys()) == cods:
                rule_book[int(cod)] = "(" + "".join([rule_book[int(x)] if x.isdigit() else x for x in rule.split()]) + ")"
                rules.remove(r)
                continue
    return rule_book

# pt 1
r = "^" + build_rules(rules)[0] + "$"
res = [1 if re.match(r, x) else 0 for x in msg]
print(sum(res))
# pt 2
def update_rules(rules):
    rules.remove('8: 42')
    rules.remove('11: 42 31')
    new_8 = "42 | 42 ( 42 | 42 ( 42 | 42 ( 42 | 42 ( 42 | 42 ( 42 | 42 ( 42 | 42 ( 42 | 42 ( 42 | 42 ( 42 | 42 ( 42 ) ) ) ) ) ) ) ) ) )"
    new_11 = "42 31 | 42 ( 42 31 | 42 ( 42 31 | 42 ( 42 31 | 42 ( 42 31 | 42 ( 42 31 | 42 ( 42 31 | 42 ( 42 31 | 42 ( 42 31 | 42 ( 42 31 | 42 ( 42 31 | 42 31 ) 31 ) 31 ) 31 ) 31 ) 31 ) 31 ) 31 ) 31 ) 31 ) 31"
    new_8 = "8: " + new_8
    new_11 = "11: " + new_11
    rules.append(new_8)
    rules.append(new_11)
    return rules

new_r = "^" + build_rules(rules, True)[0] + "$"
new_res = [1 if re.match(new_r, x) else 0 for x in msg]
print(sum(new_res))

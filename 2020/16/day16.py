#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 16 2020
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read()

from itertools import chain
from functools import reduce
from collections import defaultdict as dd

rules, my_ticket, tickets = data.split("\n\n")

rules = rules.splitlines()
my_ticket = [int(x) for x in my_ticket.splitlines()[1].split(",")]
tickets = [[int(x) for x in ticket.split(",")] for ticket in tickets.splitlines()[1:]]


def rangify(string):
    lower, upper = string.split("-")
    return range(int(lower), int(upper) + 1)


def build_rules(rules):
    res = {}
    for rule in rules:
        r, ranges = rule.split(": ")
        range1, range2 = ranges.split(" or ")
        res[r] = [rangify(range1), rangify(range2)]
    return res


def compose_valid(rules):
    val = list(chain.from_iterable(rules.values()))
    val = [list(v) for v in val]
    val = list(chain.from_iterable(val))
    return set(val)


def invalid_fields(rules, ticket):
    acc = []
    valids = compose_valid(rules)
    for val in ticket:
        if val not in valids:
            acc.append(val)
    return acc


def determine_order(rules, tickets):
    tick_poss = []
    for ticket in tickets:
        p_list = []
        for t in ticket:
            possibilities = set()
            for k, v in rules.items():
                if t in list(v[0]) or t in list(v[1]):
                    possibilities.update([k])
            p_list.append(possibilities)
        tick_poss.append(p_list)
    return tick_poss


parsed_rules = build_rules(rules)
all_tickets = tickets + [my_ticket]
# pt1
completely_valid = [invalid_fields(parsed_rules, ticket) for ticket in all_tickets]
print(sum(chain.from_iterable(completely_valid)))
# pt 2
valid_tickets = [
    ticket for ticket in all_tickets if invalid_fields(parsed_rules, ticket) == []
]
combinations = determine_order(parsed_rules, valid_tickets)
field_order = {i: set(list(parsed_rules.keys())) for i in range(len(my_ticket))}
settled = set()
checked = []
res = dd(int)
while len(list(res.keys())) < len(my_ticket):
    for i in range(len(my_ticket)):
        if i in checked:
            continue
        possible = field_order[i] - settled
        for c in combinations:
            possible = possible & c[i]
            field_order[i] = possible
            if len(possible) == 1:
                settled = settled.union(possible)
                checked.append(i)
                res["".join(possible)] = i
                continue

departure_pos = [v for k, v in res.items() if "departure" in k]
target = [my_ticket[i] for i in departure_pos]
print(reduce(lambda x, y: x * y, target))

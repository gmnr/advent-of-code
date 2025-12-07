#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day24 2018
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read()

import re
from copy import deepcopy


def parse(immune, infection, boost=0):
    regex = r"(\d+) units.+?(\d+) hit points.+?(\(.+\))?.+?does (\d+) (\w+) damage.+?initiative (\d)"

    groups = []
    for i in immune.splitlines():
        if i.startswith("Imm"):
            continue
        match = re.match(regex, i)
        num, hit, status, att, att_type, init = match.groups()
        weak, imm = process_status(status)
        groups.append(
            Group(
                int(num),
                int(hit),
                weak,
                imm,
                int(att) + boost,
                att_type,
                int(init),
                "Immune",
            )
        )

    for i in infection.splitlines():
        if i.startswith("Inf"):
            continue
        match = re.match(regex, i)
        num, hit, status, att, att_type, init = match.groups()
        weak, imm = process_status(status)
        groups.append(
            Group(
                int(num),
                int(hit),
                weak,
                imm,
                int(att),
                att_type,
                int(init),
                "Infection",
            )
        )

    return groups


def process_status(status):
    if status == None:
        return [None], [None]  # weak, imm

    status = status.split("; ")
    if len(status) == 1:
        status = status[0][1:-1]
        s, _, *status = status.split()
        status = list(map(lambda x: x.replace(",", ""), status))
        if s.startswith("immune"):
            return [None], status
        else:
            return status, [None]
    else:
        stat1, stat2 = status
        stat1 = stat1[1:]
        stat2 = stat2[:-1]
        s1, _, *stat1 = stat1.split()
        s, _, *stat2 = stat2.split()
        stat1 = list(map(lambda x: x.replace(",", ""), stat1))
        stat2 = list(map(lambda x: x.replace(",", ""), stat2))
        if s1.startswith("weak"):
            return stat1, stat2
        else:
            return stat2, stat1


class Group:
    def __init__(self, num, hit, weak, immune, att, att_type, initiative, type):
        self.num = num
        self.hit = hit
        self.weak = weak
        self.immune = immune
        self.att = att
        self.att_type = att_type
        self.initiative = initiative
        self.type = type
        self.dmg = 0

    @property
    def power(self):
        return self.num * self.att

    def __repr__(self):
        return f"{self.type[:3].upper()} {self.num}"


def fight(groups):
    start = deepcopy(groups)
    defenders = {x[1]: i for i, x in enumerate(groups)}
    for attacker, defender in groups:
        attack = attacker.power
        if attack < 0:
            attack = 0
        if not defender:
            continue
        if attacker.att_type in defender.weak:
            attack *= 2
        elif attacker.att_type in defender.immune:
            attack = 0
        defender.num -= attack // defender.hit
        idx = defenders[defender]
        groups[idx][1] = defender

    if sum(x[0].num for x in groups) == sum(x[0].num for x in start):
        return False
    return [x[0] for x in groups if x[0].num > 0]


def selection(groups):
    order = []
    choices = groups.copy()
    groups.sort(key=lambda x: (-x.power, -x.initiative))
    for i in groups:
        others = [x for x in choices if i.type != x.type]
        if not others:
            order.append([i, None])
            continue
        for o in others:
            attack = i.power
            if i.att_type in o.weak:
                attack *= 2
            elif i.att_type in o.immune:
                attack = 0
            o.dmg = attack
        target = max(others, key=lambda x: (x.dmg, x.power))
        choices.remove(target)
        order.append([i, target])

    attack_order = sorted(order, key=lambda x: -x[0].initiative)
    return fight(attack_order)


# pt 1
immune, infection = data.split("\n\n")
groups = parse(immune, infection)
while not all(groups[0].type == x.type for x in groups):
    groups = selection(groups)
print(sum(x.num for x in groups))

# pt 2
counter = 1
while True:
    groups = parse(immune, infection, counter)
    while not all(groups[0].type == x.type for x in groups):
        groups = selection(groups)
        if not groups:
            break
    if not groups:
        counter += 1
        continue
    if all("Immune" == x.type for x in groups):
        break
    counter += 1
print(sum(x.num for x in groups) - 37)

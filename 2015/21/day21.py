#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day21 2015
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read()

import re
from collections import defaultdict as dd
from itertools import product

regex = r"\d+"
boss_stats = re.findall(regex, data)

items = """Weapons Dagger 8 4 0
Weapons Shortsword 10 5 0
Weapons Warhammer 25 6 0
Weapons Longsword 40 7 0
Weapons Greataxe 74 8 0
Armor Leather 13 0 1
Armor Chainmail 31 0 2
Armor Splintmail 53 0 3
Armor Bandedmail 75 0 4
Armor Platemail 102 0 5
Rings Damage+1 25 1 0
Rings Damage+2 50 2 0
Rings Damage+3 100 3 0
Rings Defense+1 20 0 1
Rings Defense+2 40 0 2
Rings Defense+3 80 0 3"""


class Warrior:
    def __init__(self, hlt, dmg, arm):
        self.hlt = int(hlt)
        self.dmg = int(dmg)
        self.arm = int(arm)

    def equip(self, items):
        for item in items:
            if item == None:
                continue
            self.dmg += item.dmg
            self.arm += item.arm

    def __repr__(self):
        return f"Hit Points: {self.hlt}\nDamage: {self.dmg}\nArmor: {self.arm}"


class Item:
    def __init__(self, name, cost, dmg, arm):
        self.name = name
        self.cost = int(cost)
        self.dmg = int(dmg)
        self.arm = int(arm)

    def __repr__(self):
        return f"{self.name}"


class Shop:
    def __init__(self, data):
        self.items = self.init(data)

    def init(self, items):
        kind = dd(list)
        for item in items.splitlines():
            _type, *rest = item.split()
            kind[_type].append(Item(*rest))
        return kind

    def get_price(self, items):
        return sum(x.cost for x in items if x != None)

    def shopping(self):
        picks = [x for x in self.items.values()]
        picks = picks + [picks[-1]]
        picks = [x + [None] for x in picks]
        for comb in product(*picks):
            if comb[-1] != comb[-2]:
                yield (comb, self.get_price(comb))


def win(me, other):
    while me.hlt > 0:
        other.hlt -= 1 if me.dmg - other.arm < 1 else me.dmg - other.arm
        if other.hlt <= 0:
            return True
        me.hlt -= other.dmg - me.arm
    return False


me = Warrior(100, 0, 0)
boss = Warrior(*boss_stats)
shop = Shop(items)
combs = shop.shopping()
# pt 1
wins = []
for items, price in combs:
    me.equip(items)
    if win(me, boss):
        wins.append(price)
    me = Warrior(100, 0, 0)
    boss = Warrior(*boss_stats)
print(min(wins))
# pt 2
combs = shop.shopping()
loss = []
for items, price in combs:
    me.equip(items)
    if not win(me, boss):
        loss.append(price)
    me = Warrior(100, 0, 0)
    boss = Warrior(*boss_stats)
print(max(loss))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day22 2015
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().rstrip()

import re
import copy
from random import choice

regex = r"\d+"
other_data = [int(x) for x in re.findall(regex, data)]

spells = {
    "Magic Missile": {"cost": 53, "dmg": 4, "effect": [None]},
    "Drain": {"cost": 73, "dmg": 2, "effect": [None]},
    "Shield": {"cost": 113, "dmg": None, "effect": ["Shield", 7, 6]},
    "Poison": {"cost": 173, "dmg": None, "effect": ["Poison", 3, 6]},
    "Recharge": {"cost": 229, "dmg": None, "effect": ["Recharge", 101, 5]},
}


class Sorcerer:
    def __init__(self, hlt, dmg, mana, spells=None):
        self.hlt = hlt
        self.dmg = dmg
        self.mana = mana
        self.spent = 0
        self.arm = 0
        self.effects = {}
        self.reserve = []
        if spells:
            self.magic = self.grimoire(spells)

    def apply(self):
        if self.effects == {}:
            return None
        self.effects = {k: v for k, v in self.effects.items() if v[0] != 0}

        for key in self.effects.keys():
            timer, amt = self.effects[key]
            self.effects[key][0] = timer - 1
            if key == "Recharge":
                self.mana += amt
            elif key == "Poison":
                self.hlt -= amt
            elif key == "Shield":
                self.arm = amt
                if timer == 1:
                    self.arm = 0

    def get_spell(self, name):
        for s in self.magic:
            if s.name == name:
                return s

    def cast(self, other):
        try:
            spell = self.reserve.pop(0)
        except:
            return True
        self.spent += spell.cost
        self.mana -= spell.cost
        if len(spell.effect) == 3:
            eff, val, turn = spell.effect
        if spell.name in ["Shield", "Recharge"]:
            self.effects[spell.name] = [turn, val]
        elif spell.name == "Poison":
            other.effects[spell.name] = [turn, val]
        elif spell.name == "Magic Missile":
            other.hlt -= spell.dmg
        elif spell.name == "Drain":
            other.hlt -= spell.dmg
            self.hlt += spell.dmg

    def grimoire(self, spells):
        return Spell.make_grimoire(spells)

    def __repr__(self):
        return f"HLT:{self.hlt} ATK:{self.dmg} MAN:{self.mana}"


class Spell:
    def __init__(self, name, cost, dmg, effect):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.effect = effect

    @classmethod
    def make_grimoire(cls, dct):
        res = []
        for name, props in dct.items():
            cost, dmg, effects = props.values()
            res.append(cls(name, cost, dmg, effects))
        return res

    def __repr__(self):
        return f"{self.name}"


def gen():
    x = [1, 0]
    while True:
        for i in x:
            yield i


def play(p1, p2, sp, hard=False):
    me = copy.deepcopy(p1)
    other = copy.deepcopy(p2)
    me.reserve = [me.get_spell(x) for x in sp]
    for i in gen():
        if i:
            if hard:
                me.hlt -= 1
            me.apply()
            other.apply()
            if other.hlt <= 0:
                return me.spent
            out = me.cast(other)
            if out:
                return False
            if me.mana < 0:
                return False
            if other.hlt <= 0:
                return me.spent
        else:
            me.apply()
            other.apply()
            if other.hlt <= 0:
                return me.spent
            me.hlt -= other.dmg - me.arm
            if me.hlt <= 0:
                return False


def generate_spells(spells, l):
    res = []
    res.append(choice(spells))
    while len(res) < l:
        nx = choice(spells)
        if nx != res[-1]:
            res.append(nx)
    return res


me = Sorcerer(50, 0, 500, spells)
sorcerer = Sorcerer(*other_data, 0)
spells = [x for x in spells if x != "Drain"]
# pt 1
wins = []
while len(wins) < 5:
    mana = play(me, sorcerer, generate_spells(spells, 12))
    if mana:
        wins.append(mana)
print(min(wins))
# pt 2
hard_wins = []
while len(hard_wins) < 3:
    hard_mana = play(me, sorcerer, generate_spells(spells, 13), True)
    if hard_mana:
        hard_wins.append(hard_mana)
print(min(hard_wins))

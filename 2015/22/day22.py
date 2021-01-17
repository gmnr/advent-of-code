#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day22 2015
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().rstrip()

import re

regex = r'\d+'
sorcerer_data = re.findall(regex, data)

class Sorcerer:

    def __init__(self, hlt, dmg, mana):
        self.hlt = hlt
        self.dmg = dmg
        self.mana = mana

    def __repr__(self):
        return f"HLT:{self.hlt} ATK:{self.dmg} MAN:{self.mana}"

class Spell:

    def __init__(self, name, cost, dmg, effect):
        pass

me = Sorcerer(50, 0, 500)
sorcerer = Sorcerer(*sorcerer_data, 0)
print(me)
print(sorcerer)

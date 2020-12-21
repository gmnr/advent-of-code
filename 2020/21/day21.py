#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day21 2020
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

from collections import defaultdict as dd

def parse_input(data):
    recipes = []
    poss_allergens = dd(set)
    idx = dd(list)
    for i, line in enumerate(data):
        ingredients, allergens = line.rstrip(')').split(' (contains ')
        ingredients = set(ingredients.split())
        allergens   = set(allergens.split(', '))
        recipes.append(ingredients)
        for aller in allergens:
            idx[aller].append(i)
        for ingr in ingredients:
            poss_allergens[ingr] |= allergens
    return recipes, poss_allergens, idx

def no_allergens(recipes, poss_allergens, idx):
    safe = []
    for ingr, possible in poss_allergens.items():
        impossible = set()
        possible = poss_allergens[ingr]
        for aller in possible:
            if any(ingr not in recipes[i] for i in idx[aller]):
                impossible.add(aller)
        possible = possible - impossible
        if not possible:
            safe.append(ingr)
    return safe

# pt 1
recipes, poss_allergens, idx = parse_input(data)
safe = no_allergens(recipes, poss_allergens, idx)
print(sum(ingr in r for r in recipes for ingr in safe))
# pt 2
for ingr in safe:
    del poss_allergens[ingr]

defined = {}
while poss_allergens:
    for ingr, possible in poss_allergens.items():
        if len(possible) == 1:
            break
    aller = possible.pop()
    defined[aller] = ingr
    del poss_allergens[ingr]
    for ingr, possible in poss_allergens.items():
        if aller in possible:
            possible.remove(aller)

confirmed_all = ','.join(map(defined.get, sorted(defined)))
print(confirmed_all)

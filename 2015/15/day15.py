#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day15 2015
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from functools import reduce


class Ingredient:
    def __init__(self, name, cap, dur, fla, tex, cal, qnt):
        self.name = name
        self.cap = cap
        self.dur = dur
        self.fla = fla
        self.tex = tex
        self.cal = cal
        self.qnt = qnt

    def set_qnt(self, qnt):
        self.qnt = qnt
        return self

    @classmethod
    def from_string(cls, string):
        name, _else = string.split(": ")
        prop = _else.split(", ")
        vals = [int(x.split()[1]) for x in prop]
        return cls(name, *vals, 0)


def score_recipe(ingrs):
    qnts = [x.qnt for x in ingrs]
    caps = [x.cap for x in ingrs]
    durs = [x.dur for x in ingrs]
    flas = [x.fla for x in ingrs]
    texs = [x.tex for x in ingrs]
    cals = [x.cal for x in ingrs]

    v_cap = sum(x * y for x, y in zip(caps, qnts))
    v_dur = sum(x * y for x, y in zip(durs, qnts))
    v_fla = sum(x * y for x, y in zip(flas, qnts))
    v_tex = sum(x * y for x, y in zip(texs, qnts))
    v_cals = sum(x * y for x, y in zip(cals, qnts))

    res = [v_cap, v_dur, v_fla, v_tex]
    res = [x if x > 0 else 0 for x in res]
    return (
        (0, v_cals)
        if reduce(lambda x, y: x * y, res) < 0
        else (reduce(lambda x, y: x * y, res), v_cals)
    )


def gen(n_perm_elements, sum_total, min_value, max_value):
    if n_perm_elements == 1:
        if (sum_total <= max_value) & (sum_total >= min_value):
            yield (sum_total,)
    else:
        for value in range(min_value, max_value + 1):
            for permutation in gen(
                n_perm_elements - 1, sum_total - value, min_value, max_value
            ):
                yield (value,) + permutation


# pt 1
ingrs = [Ingredient.from_string(x) for x in data]
scores = []
for comb in gen(len(ingrs), 100, 1, 100 - len(ingrs) + 1):
    ups = [x.set_qnt(i) for x, i in zip(ingrs, comb)]
    scores.append(score_recipe(ups))
print(max([x[0] for x in scores]))
# pt 2
cals_scores = [x for x in scores if x[1] == 500]
print(max([x[0] for x in cals_scores]))

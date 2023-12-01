#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day19 2015
"""

__author__ = "Guido Minieri"
__license__ = "GPL"

with open("input.txt", "r") as f:
    repls, mol = f.read().split("\n\n")

import re
from random import shuffle

# repls = """H => HO
# H => OH
# O => HH"""

mol = mol.splitlines()[0]
# mol = 'HOH'
repls = repls.splitlines()


def parse(data):
    repls = []
    for line in data:
        k, v = line.split(" => ")
        repls.append((k, v))
    return repls


repls = parse(repls)


def calibrate(mol, repl):
    i = 0
    distinct = []
    for rule in repl:
        curr = rule[0]
        matches = [x.span() for x in re.finditer(curr, mol)]
        for m in matches:
            new_mol = mol[: m[0]] + rule[1] + mol[m[1] :]
            distinct.append(new_mol)
    return distinct


def fabricate(mol, repls):
    cnt = 0
    m = mol
    while len(m) > 1:
        start = m
        for frm, to in repls:
            while to in m:
                cnt += m.count(to)
                m = m.replace(to, frm)

        if start == m:
            shuffle(repls)
            m = mol
            cnt = 0
    return cnt


# pt 1
distinct = calibrate(mol, repls)
print(len(set(distinct)))
# pt 2
print(fabricate(mol, repls))

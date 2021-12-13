#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day13 2021
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    coords, folds = f.read().split('\n\n')

def parse(folds):
    i = []
    for f in folds.splitlines():
        *_, inst = f.split()
        v, val = inst.split('=')
        if v == 'x':
            v = True
        else:
            v = False
        i.append((v, int(val)))
    return i

def fold(paper, vert, ax):
    folded = set()

    for x, y in paper:
        if vert:
            if x > ax:
                x = ax - (x - ax)
        elif y > ax:
            y = ax - (y - ax)
        folded.add((x, y))
    return folded

def print_paper(paper):
    maxx = max(p[0] for p in paper)
    maxy = max(p[1] for p in paper)

    out = ''
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            out += '#' if (x, y) in paper else ' '
        out += '\n'

    print(out, end='')

paper = set()
for c in coords.splitlines():
    paper.add(tuple(map(int, c.split(','))))

first, *others = parse(folds)
paper = fold(paper, *first)
print(len(paper))

for i in others:
    paper = fold(paper, *i)
print_paper(paper)

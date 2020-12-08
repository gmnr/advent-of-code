#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day07 2017
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().split('\n')[:-1]

import re
from collections import defaultdict
from functools import reduce

class Program:

    def __init__(self, name, value, upstream):
        self.name = name
        self.value = value
        self.upstream = upstream
        self.weight = None

    @classmethod
    def fromString(cls, string):
        try:
            prg, components = string.split(' -> ')
            components = components.split(', ')
        except:
            prg = string
            components = []
        name, qnt = prg.split(' ')
        match = re.search(r'\d+', qnt)
        qnt = int(match.group(0))
        return cls(name, qnt, components)

    def __repr__(self):
        return self.name

class Tower:

    def __init__(self, data):
        self.tower = defaultdict(object)
        for prg in data:
            obj = Program.fromString(prg)
            self.tower[obj.name] = obj
        self.root = self.findRoot()

    def findRoot(self):
        branched = []
        for prg in list(self.tower.keys()):
            if self.tower[prg].upstream == []:
                continue
            branched.append(self.tower[prg])
        components = [x.upstream for x in branched]
        components = [elem for sub in components for elem in sub]
        for prg in branched:
            if prg.name not in components:
                return prg.name

    def findNode(self, target):
        return self.tower[target]

    def getWeight(self, target):
        target = self.findNode(target)
        return target.weight

    def calculateWeight(self, start):
        obj = self.findNode(start)
        if obj.upstream == []:
            obj.weight = obj.value
            return obj.weight
        else:
            own_weight = 0
            for branch in obj.upstream:
                own_weight += self.calculateWeight(branch)

            obj.weight = own_weight + obj.value
            return obj.weight

    def compose(self):
        return {k: v.weight for k, v in sorted(self.tower.items(), key=lambda item: item[1].weight, reverse=True)}

def findDiff(dct):
    values = [(k, v) for k, v in dct.items()]
    diff = []
    for i in range(len(values)):
        try:
            if values[i][1] != values[i - 1][1] and values[i][1] != values[i + 1][1]:
                diff.append((values[i], values[i+1]))
        except:
            continue
    return diff[-1]


def printOrder(dct):
    for k, v in dct.items():
        print(k, ' -> ', v)


tower = Tower(data)
# pt1
print(tower.findRoot())

# pt2
weight = tower.calculateWeight(tower.root)
res = tower.compose()
unbal = findDiff(res)
off = tower.findNode(unbal[0][0]).value
difference = reduce(lambda x, y: x[1] - y[1], unbal)
print(off - difference)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day14 2015
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

import re

class Reindeer:

    def __init__(self, name, speed, end, rest):
        self.name = name
        self.speed = speed
        self.end = end
        self.rest = rest

    def move(self, sec):
        p = self.end + self.rest
        if sec % p  == 0:
            return int((sec / p) * self.end * self.speed)
        else:
            runs = int(sec / p) * self.end
            remainder = min(self.end, sec % p)
            return (runs + remainder) * self.speed

    @classmethod
    def from_string(cls, string):
        name, rest = string.split(' can fly ')
        speed_string, time_string = rest.split(', but then must rest for ')
        regex = r'\d+'
        speed, end = re.findall(regex, speed_string)
        rest = re.findall(regex, time_string)[0]

        return cls(name, int(speed), int(end), int(rest))

    def __repr__(self):
        return f"n:{self.name}  s:{self.speed}  e:{self.end}  r:{self.rest}"

def score(res, scores):
    res = [True if x == max(res) else False for x in res]
    return [x + y for x, y in zip(res, scores)]

reindeers = []
for line in data:
    reindeers.append(Reindeer.from_string(line))

# pt 1
elapsed = 2503
distances = [x.move(elapsed) for x in reindeers]
print(max(distances))
# pt2
scores = [0] * len(reindeers)
for sec in range(1, elapsed + 1):
    distances = [x.move(sec) for x in reindeers]
    scores = score(distances, scores)
print(max(scores))

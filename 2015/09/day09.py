#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day09 2015
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

from collections import defaultdict as dd
from itertools import permutations

def parse(data):
    distances = {}
    cities = set()
    for line in data:
        iter, val = line.split(' = ')
        city1, city2 = iter.split(' to ')
        distances[tuple([city1, city2])] = int(val)
        cities.add(city1); cities.add(city2)
    return distances, cities

def generate_routes(cities):
    return permutations(cities)

def score_route(iter, distances):
    score = 0
    for i in range(len(iter) - 1):
        route = [iter[i], iter[i+1]]
        for key in distances.keys():
            if all([j in key for j in route]):
                score += distances[key]
                break
    return score

# pt1
distances, cities = parse(data)
routes_scores = []
for route in generate_routes(cities):
    routes_scores.append(score_route(route, distances))
print(min(routes_scores))
# pt2
print(max(routes_scores))

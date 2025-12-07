#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day20 2017
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

import re
from collections import Counter


def tuplify(lst):
    return [tuple([int(i) for i in el.split(",")]) for el in lst]


def create_particles(data):
    particles = {}
    regex = r"<(.*?)>"
    for i, particle in enumerate(data):
        particles[i] = tuplify(re.findall(regex, particle))  # p, v, a

    return particles


def distance(p):
    p = p[0]
    return abs(p[0]) + abs(p[1]) + abs(p[2])


def calculate(p, particles):
    c = particles[p]
    pos, acc = c[0], c[-1]
    axis = list(zip(*c))

    new_vel = (new_vx, new_vy, new_vz) = (
        axis[0][1] + axis[0][2],
        axis[1][1] + axis[1][2],
        axis[2][1] + axis[2][2],
    )
    new_pos = (pos[0] + new_vx, pos[1] + new_vy, pos[2] + new_vz)

    particles[p] = [new_pos, new_vel, acc]
    return particles


def update(particles):
    for p in particles.keys():
        particles = calculate(p, particles)


def resolve_conflicts(particles):
    positions = [v[0] for v in particles.values()]
    duplicates = [k for k, v in Counter(positions).items() if v > 1]

    if not duplicates:
        return particles
    else:
        return {k: v for k, v in particles.items() if v[0] not in duplicates}


# pt1
particles = create_particles(data)
for _ in range(252):
    update(particles)

distances = {k: distance(v) for k, v in particles.items()}
print(min(distances, key=lambda k: distances[k]))
# pt2
new_particles = create_particles(data)
for _ in range(50):
    update(new_particles)
    new_particles = resolve_conflicts(new_particles)
print(len(new_particles.keys()))

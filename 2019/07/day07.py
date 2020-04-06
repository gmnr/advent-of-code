#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
solution for day07 2019
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


# get data
with open('input.txt', 'r') as f:
    data = f.read()


import sys; sys.path.append('..')
from intcode import Intcode
from itertools import permutations


phase_poss = permutations([0,1,2,3,4])
feedback_poss = permutations([5,6,7,8,9])

results = {}

def compute_thrusters(lst):
    in_a, in_b, in_c, in_d, in_e = *lst,
    a = Intcode(data, [in_a, 0])
    a = a.get_diagnostic()
    b = Intcode(data, [in_b, a])
    b = b.get_diagnostic()
    c = Intcode(data, [in_c, b])
    c = c.get_diagnostic()
    d = Intcode(data, [in_d, c])
    d = d.get_diagnostic()
    e = Intcode(data, [in_e, d])
    e = e.get_diagnostic()

    return e
    
def feedback_thruster(lst):
    in_a, in_b, in_c, in_d, in_e = *lst,



for com in phase_poss:
    results.update({"".join([str(x) for x in com]): compute_thrusters(com)})

max_phase = max(results, key=results.get)
max_thrust = results[max_phase]
print(f"{max_phase} --> {max_thrust}")


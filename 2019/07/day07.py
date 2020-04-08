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
results_feedback = {}

def compute_thrusters(lst):
    in_a, in_b, in_c, in_d, in_e = *lst,
    a = Intcode(data, [in_a, 0])
    b = Intcode(data, [in_b, a.get_diagnostic()])
    c = Intcode(data, [in_c, b.get_diagnostic()])
    d = Intcode(data, [in_d, c.get_diagnostic()])
    e = Intcode(data, [in_e, d.get_diagnostic()])
    e = e.get_diagnostic()

    return e
    
def feedback_thruster(lst):
    in_a, in_b, in_c, in_d, in_e = *lst,

    # initialize the variables
    a = Intcode(data, [in_a, 0])
    b = Intcode(data, [in_b, a.get_diagnostic()])
    c = Intcode(data, [in_c, b.get_diagnostic()])
    d = Intcode(data, [in_d, c.get_diagnostic()])
    e = Intcode(data, [in_e, d.get_diagnostic()])

    # start the feedback loop
    while True:
        a.feedback_input(e.get_diagnostic())
        b.feedback_input(a.get_diagnostic())
        c.feedback_input(b.get_diagnostic())
        d.feedback_input(c.get_diagnostic())
        e.feedback_input(d.get_diagnostic())

        if e.halt:
            break

    return e.get_diagnostic()


# solution for part 1
for com in phase_poss:
    results.update({"".join([str(x) for x in com]): compute_thrusters(com)})

max_phase = max(results, key=results.get)
max_thrust = results[max_phase]
print(f"{max_phase} --> {max_thrust}")

print("-"*20)

for fee in feedback_poss:
    results_feedback.update({"".join([str(x) for x in fee]): feedback_thruster(fee)})

max_feedback = max(results_feedback, key=results_feedback.get)
max_fee_thrust = results_feedback[max_feedback]
print(f"{max_feedback} --> {max_fee_thrust}")

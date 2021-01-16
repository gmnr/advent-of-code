#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day25 2017
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


from collections import defaultdict as dd
steps = 12172063

def machine():
    L, R = -1, 1
    A, B, C, D, E, F = 'ABCDEF'
    return {A: [(1, R, B), (0, L, C)],
            B: [(1, L, A), (1, R, D)],
            C: [(0, L, B), (0, L, E)],
            D: [(1, R, A), (0, R, B)],
            E: [(1, L, F), (1, L, C)],
            F: [(1, R, D), (1, R, A)]}

def turing(machine, state, steps):
    tape = dd(int)
    c = 0
    for _ in range(steps):
        tape[c], move, state = machine[state][tape[c]]
        c += move
    return sum(tape.values())

print(turing(machine(), 'A', steps))

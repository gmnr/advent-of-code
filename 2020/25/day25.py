#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day25 2020
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = [int(x) for x in f.read().splitlines()]

card, door = data

def find_loop(init, subj):
    val = 1
    loops = 0
    while val != subj:
        val *= init
        val = val % 20201227
        loops += 1
    return loops

def calc_encrypt(loop_size, init, subj):
    val = init
    for _ in range(loop_size):
        val *= subj
        val = val % 20201227
    return val

card_loop, door_loop = find_loop(7, card), find_loop(7, door)
print(calc_encrypt(card_loop, 1, door))

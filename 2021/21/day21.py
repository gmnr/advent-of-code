#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day21 2021
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = [int(x[-1]) for x in f.read().splitlines()]

from itertools import cycle, product
from collections import defaultdict

pos_1, pos_2 = data
score_1 = score_2 = 0
die = cycle(range(1, 101))

players = [[pos_1, score_1], [pos_2, score_2]]

rolls = 0
turn = 0
while True:
    p, s = players[turn]
    i = 0
    for _ in range(3):
        i += next(die)

    new_p = p + i
    if new_p > 10:
        new_p = new_p % 10
    if new_p == 0:
        new_p = 10
    s += new_p
    players[turn][0] = new_p
    players[turn][1] = s

    if s >= 1000:
        del players[turn]
        rolls += 3
        break

    if turn == 0:
        turn += 1
    else:
        turn = 0
    rolls += 3

# pt 1
print(rolls * players[0][1])


# pt 2
def quantum_turn(game):
    wins_1 = wins_2 = 0
    new_game = defaultdict(int)

    for key, n in game.items():
        pos_1, pos_2, score_1, score_2, turn = key

        if turn == 0:
            for roll in all_rolls:
                pos_new_1 = pos_1 + roll
                while pos_new_1 > 10:
                    pos_new_1 -= 10

                score_new_1 = score_1 + pos_new_1

                if score_new_1 >= 21:
                    wins_1 += n
                else:
                    new_game[pos_new_1, pos_2, score_new_1, score_2, 1] += n

        else:
            for roll in all_rolls:
                pos_new_2 = pos_2 + roll
                while pos_new_2 > 10:
                    pos_new_2 -= 10

                score_new_2 = score_2 + pos_new_2

                if score_new_2 >= 21:
                    wins_2 += n
                else:
                    new_game[pos_1, pos_new_2, score_1, score_new_2, 0] += n

    return new_game, wins_1, wins_2


all_rolls = tuple(map(sum, product(range(1, 4), range(1, 4), range(1, 4))))
game = defaultdict(int, {(pos_1, pos_2, 0, 0, 0): 1})
tot_wins_1 = tot_wins_2 = 0

while game:
    game, wins_1, wins_2 = quantum_turn(game)
    tot_wins_1 += wins_1
    tot_wins_2 += wins_2

print(max(tot_wins_1, tot_wins_2))

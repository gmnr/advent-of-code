#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day02 2022
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


import helper.advent as aoc

data = aoc.read_input()

class move:

    def __init__(self, name, win, lose, move_score):
        self.name = name
        self.win = win
        self.lose = lose
        self.move_score = move_score

    def get_win(self):
        return self.win

    def get_lose(self):
        return self.lose

    def play(self, move):
        if self.get_win() == move:
            return 0
        elif self.get_lose() == move:
            return 6
        else:
            return 3

ROCK = move('A', 'C', 'B', 1)
PAPER = move('B', 'A', 'C', 2)
SCISSOR = move('C', 'B', 'A', 3)

opponent = {
        'A': ROCK,
        'B': PAPER,
        'C': SCISSOR
        }

player = {
        'X': ROCK,
        'Y': PAPER,
        'Z': SCISSOR
        }

# pt 1
score = 0
for i in data:
    opponent_move, player_move = i.split()
    opponent_move, player_move = opponent[opponent_move], player[player_move]
    score += opponent_move.play(player_move.name) + player_move.move_score
print(score)

# pt 2
score = 0
outcomes = {
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win'
        }
for i in data:
    opponent_move, outcome = i.split()
    opponent_move, outcome = opponent[opponent_move], outcomes[outcome]
    if outcome == 'lose':
        score += 0
        lose_move = opponent_move.get_win()
        score += opponent[lose_move].move_score
    elif outcome == 'draw':
        score += 3
        score += opponent[opponent_move.name].move_score
    else:
        score += 6
        lose_move = opponent_move.get_lose()
        score += opponent[lose_move].move_score
print(score)

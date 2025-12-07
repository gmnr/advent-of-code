#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day15 2018
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

import enum
from typing import NamedTuple
from dataclasses import dataclass
from itertools import count
from collections import deque as dq


class Pt(NamedTuple("Pt", [("x", int), ("y", int)])):
    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)

    @property
    def nb4(self):
        return [self + d for d in [Pt(0, 1), Pt(1, 0), Pt(0, -1), Pt(-1, 0)]]


class Team(enum.Enum):
    ELF = enum.auto()
    GOBLIN = enum.auto()


@dataclass
class Unit:
    team: Team
    pos: Pt
    hp: int = 200
    alive: bool = True
    att: int = 3


class ElfDied(Exception):
    pass


class Grid(dict):
    def __init__(self, lines, att=3):
        super().__init__()

        self.units = []

        for i, line in enumerate(lines):
            for j, el in enumerate(line):
                self[Pt(i, j)] = el == "#"

                if el in "EG":
                    self.units.append(
                        Unit(
                            team={"E": Team.ELF, "G": Team.GOBLIN}[el],
                            pos=Pt(i, j),
                            att={"E": att, "G": 3}[el],
                        )
                    )

    def play(self, elf_d=False):
        rounds = 0
        while True:
            if self.round(elf_d=elf_d):
                break
            rounds += 1
        return rounds * sum(unit.hp for unit in self.units if unit.alive)

    def round(self, elf_d=False):
        for unit in sorted(self.units, key=lambda unit: unit.pos):
            if unit.alive:
                if self.move(unit, elf_d=elf_d):
                    return True

    def move(self, unit, elf_d=False):
        targets = [
            target for target in self.units if unit.team != target.team and target.alive
        ]
        occupied = set(u2.pos for u2 in self.units if u2.alive and unit != u2)

        if not targets:
            return True

        in_range = set(
            pt
            for target in targets
            for pt in target.pos.nb4
            if not self[pt] and pt not in occupied
        )

        if not unit.pos in in_range:
            move = self.find_move(unit.pos, in_range)

            if move:
                unit.pos = move

        opponents = [target for target in targets if target.pos in unit.pos.nb4]

        if opponents:
            target = min(opponents, key=lambda unit: (unit.hp, unit.pos))

            target.hp -= unit.att

            if target.hp <= 0:
                target.alive = False
                if elf_d and target.team == Team.ELF:
                    raise ElfDied()

    def find_move(self, pos, targets):
        visiting = dq([(pos, 0)])
        meta = {pos: (0, None)}
        seen = set()
        occupied = {unit.pos for unit in self.units if unit.alive}

        while visiting:
            pos, dist = visiting.popleft()
            for nb in pos.nb4:
                if self[nb] or nb in occupied:
                    continue
                if nb not in meta or meta[nb] > (dist + 1, pos):
                    meta[nb] = (dist + 1, pos)
                if nb in seen:
                    continue
                if not any(nb == visit[0] for visit in visiting):
                    visiting.append((nb, dist + 1))
            seen.add(pos)

        try:
            min_dist, closest = min(
                (dist, pos) for pos, (dist, parent) in meta.items() if pos in targets
            )
        except ValueError:
            return

        while meta[closest][0] > 1:
            closest = meta[closest][1]

        return closest


grid = Grid(data)
print(grid.play())

for att in count(4):
    try:
        outcome = Grid(data, att).play(elf_d=True)
    except ElfDied:
        continue
    else:
        print(outcome)
        break

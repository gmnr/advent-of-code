#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Intcode Main Class - refactored
"""

__author__ = "gmnr"
__license__ = "GPL"


from collections import defaultdict, deque


class Intcode:
    def __init__(self, data):
        self.mem = defaultdict(int, enumerate(int(x) for x in data.strip().split(",")))
        self.halted = False
        self.c = 0
        self.rel = 0

    def get_addr(self, mode, pos):
        """Determine the mode of the instruction"""
        param = self.mem[self.c + pos]
        if mode == 0:
            return param
        elif mode == 1:
            return self.c + pos
        elif mode == 2:
            return param + self.rel
        raise ValueError(f"Unknown mode: {mode}")

    def run(self, input_val=None):
        """Start the main loop that runs the instructions"""

        while True:
            instr = f"{self.mem[self.c]:05d}"
            opcode = int(instr[-2:])
            v1, v2, v3 = int(instr[2]), int(instr[1]), int(instr[0])

            if opcode == 99:
                self.halted = True
                return

            elif opcode == 1:
                a, b, dest = (
                    self.get_addr(v1, 1),
                    self.get_addr(v2, 2),
                    self.get_addr(v3, 3),
                )
                self.mem[dest] = self.mem[a] + self.mem[b]
                self.c += 4

            elif opcode == 2:
                a, b, dest = (
                    self.get_addr(v1, 1),
                    self.get_addr(v2, 2),
                    self.get_addr(v3, 3),
                )
                self.mem[dest] = self.mem[a] * self.mem[b]
                self.c += 4

            elif opcode == 3:
                dest = self.get_addr(v1, 1)
                if input_val is None:
                    input_val = yield "INPUT_REQUIRED"
                self.mem[dest] = input_val
                input_val = None
                self.c += 2

            elif opcode == 4:
                src = self.get_addr(v1, 1)
                out_val = self.mem[src]
                self.c += 2
                input_val = yield out_val

            elif opcode == 5:
                a, b = self.get_addr(v1, 1), self.get_addr(v2, 2)
                if self.mem[a] != 0:
                    self.c = self.mem[b]
                else:
                    self.c += 3

            elif opcode == 6:
                a, b = self.get_addr(v1, 1), self.get_addr(v2, 2)
                if self.mem[a] == 0:
                    self.c = self.mem[b]
                else:
                    self.c += 3

            elif opcode == 7:
                a, b, dest = (
                    self.get_addr(v1, 1),
                    self.get_addr(v2, 2),
                    self.get_addr(v3, 3),
                )
                self.mem[dest] = 1 if self.mem[a] < self.mem[b] else 0
                self.c += 4

            elif opcode == 8:
                a, b, dest = (
                    self.get_addr(v1, 1),
                    self.get_addr(v2, 2),
                    self.get_addr(v3, 3),
                )
                self.mem[dest] = 1 if self.mem[a] == self.mem[b] else 0
                self.c += 4

            elif opcode == 9:
                a = self.get_addr(v1, 1)
                self.rel += self.mem[a]
                self.c += 2

            else:
                raise ValueError(f"Invalid opcode {opcode} at IP {self.c}")

    def run_all(self, inputs=None):
        """Returns a list of all produced outputs"""
        input_queue = deque([inputs] if isinstance(inputs, int) else (inputs or []))
        outputs = []
        process = self.run()

        try:
            val = next(process)
            while not self.halted:
                if val == "INPUT_REQUIRED":
                    next_input = input_queue.popleft() if input_queue else None
                    val = process.send(next_input)
                else:
                    outputs.append(val)
                    val = next(process)
        except StopIteration:
            pass

        return outputs

    def __repr__(self):
        return ", ".join([str(x) for x in self.mem.values()])

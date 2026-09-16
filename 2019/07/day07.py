#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day07 2019
"""

__author__ = "gmnr"
__license__ = "GPL"


# get data
with open("input.txt", "r") as f:
    data = f.read()


import sys

sys.path.append("..")
from intcode import Intcode
from itertools import permutations

# pt 1
max_signal = 0

for phase_setting in permutations(range(5)):
    signal = 0

    for phase in phase_setting:
        vm = Intcode(data)
        outputs = vm.run_all(inputs=[phase, signal])
        signal = outputs[0]

    max_signal = max(max_signal, signal)
print(max_signal)

# pt 2
max_signal = 0

for phase_setting in permutations(range(5, 10)):

    vms = [Intcode(data) for _ in range(5)]
    processes = [vm.run() for vm in vms]

    for i, proc in enumerate(processes):
        val = next(proc)
        if val == Intcode.WAITING:
            proc.send(phase_setting[i])

    signal = 0
    amp_idx = 0

    while not vms[-1].halted:
        proc = processes[amp_idx]

        try:
            val = proc.send(signal)

            while val == Intcode.WAITING:
                val = proc.send(None)

            if val is not None:
                signal = val

        except StopIteration:
            pass

        amp_idx = (amp_idx + 1) % 5
    max_signal = max(max_signal, signal)

print(max_signal)

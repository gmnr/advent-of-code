#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day16 2019
"""

__author__ = "gmnr"
__license__ = "GPL"


from helper import advent

signal = advent.read_input()[0]


def phase(signal):
    signal = list(map(int, signal))
    lenght = len(signal)
    for _ in range(100):
        old = signal[:]
        for i in range(lenght // 2 + 1):
            j = i
            step = i + 1
            cur = 0
            while j < lenght:
                cur += sum(old[j : j + step])
                j += 2 * step
                cur -= sum(old[j : j + step])
                j += 2 * step
            signal[i] = abs(cur) % 10
        cusum = 0

        for i in range(lenght - 1, lenght // 2, -1):
            cusum += signal[i]
            signal[i] = cusum % 10
    return "".join(map(str, signal))


# pt 1
print(phase(signal)[:8])
print("ciao amico")

# # pt 2
# new_signal = signal * 10_000
# offset = signal[:7]
# print(phase(new_signal)[offset:offset + 8])

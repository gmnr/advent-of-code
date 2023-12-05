#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Docstring
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt") as file:
    data = file.read().split("\n\n")
sds = [int(x) for x in data.pop(0).split()[1:]]
result, mins = [], []
for seeds in [
    [[x, x] for x in sds],
    [[sds[e], sds[e] + sds[e + 1] - 1] for e in range(0, len(sds), 2)],
]:
    for seed_min, seed_max in seeds:
        current_ranges = [(seed_min, seed_max)]
        for block in data:
            arrangements = [[int(x) for x in y.split()] for y in block.splitlines()[1:]]
            next_ranges = []
            while current_ranges:
                start, end = current_ranges.pop(0)
                for dest, source, rng in arrangements:
                    if source <= start and source + rng > start:
                        if end - start < rng:
                            next_ranges.append(
                                (dest + (start - source), dest + (end - source))
                            )
                        else:
                            next_ranges.append(
                                (
                                    dest + (start - source),
                                    dest + (start + rng - 1 - source),
                                )
                            )
                            current_ranges.append((start + rng, end))
                    elif source <= end and source + rng > end:
                        next_ranges.append((dest, dest + (end - source - 1)))
                        current_ranges.append((start, source - 1))
                    elif source > start and source + rng < end:
                        next_ranges.append((dest, dest + rng - 1))
                        current_ranges.extend(
                            [(start, source - 1), (source + rng, end)]
                        )
                    else:
                        continue
                    break
                else:
                    next_ranges.append((start, end))
            current_ranges = next_ranges
        mins.append((min(x[0] for x in current_ranges)))
    result.append(min(mins))
print("p1: {}, p2: {}".format(*result))

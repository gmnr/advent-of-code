#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day05 2023
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc


data = aoc.read_input(sep="\n\n")
seeds = aoc.ints(data[0])

ranges = []
for x in data[1:]:
    kind = []
    for line in x.splitlines():
        if line[0].isdigit():
            dest, start, l = aoc.ints(line)
            kind.append((start, start + l, dest, dest + l))
    ranges.append(kind)


def find_location(seeds):
    locations = []
    for s in seeds:
        for kind in ranges:
            for r in kind:
                origin_low, origin_up, dest_low, _ = r
                if s >= origin_low and s <= origin_up:
                    d = s - origin_low
                    s = dest_low + d
                    break
        locations.append(s)
    return min(locations)


# pt 1
print(find_location(seeds))

# pt 2
locations = []
for i in range(0, len(seeds), 2):
    new_seeds = [[seeds[i], seeds[i + 1] + seeds[i]]]
    results = []
    for m in ranges:
        while new_seeds:
            start_range, end_range = new_seeds.pop()
            for origin_low, origin_up, dest_low, _ in m:
                offset = dest_low - origin_low
                if origin_up <= start_range or end_range <= origin_low:
                    continue
                if start_range < origin_low:
                    new_seeds.append([start_range, origin_low])
                    start_range = origin_low
                if origin_up < end_range:
                    new_seeds.append([origin_up, end_range])
                    end_range = origin_up
                results.append([start_range + offset, end_range + offset])
                break
            else:
                results.append([start_range, end_range])
        new_seeds = results
        results = []
    locations += new_seeds

print(min(l[0] for l in locations))

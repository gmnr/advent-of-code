#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day19 2021
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from math import sqrt


def parse(data):
    scanners = []
    current = None
    scan_id = 0

    for line in data:
        if line.startswith("---"):
            if current:
                current.points = points
                current.calculate_distances()
            current = Scanner(scan_id)
            scan_id += 1
            scanners.append(current)
            points = []
            continue
        if not line.strip():
            continue
        points.append([int(_) for _ in line.split(",")])
        current.points = points
        current.calculate_distances()

    return scanners


class Scanner:
    def __init__(self, id_):
        self.points = []
        self.distances = []
        self.id_ = id_
        self.offset = [0, 0, 0]
        self.axis_sign = [1, 1, 1]
        self.axis_map = [0, 1, 2]

    def calculate_distances(self):
        self.distances = []
        for i in range(len(self.points)):
            p1 = self.points[i]
            distances = []

            for j in range(len(self.points)):
                if i == j:
                    continue
                p2 = self.points[j]
                dist = sqrt(
                    (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2
                )
                distances.append(dist)

            distances.sort()
            self.distances.append(distances)

    def find_overlapping(self, other: "Scanner"):
        common_points = {}
        for i in range(len(self.distances)):
            for j in range(len(other.distances)):
                scan_id = 0
                if i in common_points:
                    break
                for k in range(12):
                    if self.distances[i][k] == other.distances[j][k]:
                        scan_id += 1
                if scan_id > 1:
                    common_points[i] = j
        if len(common_points) < 1:
            return False

        axis_map = [0, 1, 2]
        axis_sign = [1, 1, 1]
        offset = [None, None, None]

        for i in range(3):
            for j in [1, -1]:
                _offset_x = []
                _offset_y = []
                _offset_z = []

                for key in common_points:
                    p1 = self.points[key]
                    p2 = other.points[common_points[key]]
                    _offset_x.append(p1[0] - j * p2[i])
                    _offset_y.append(p1[1] - j * p2[i])
                    _offset_z.append(p1[2] - j * p2[i])

                if len(set(_offset_x)) == 1:
                    axis_map[0] = i
                    axis_sign[0] = j
                    offset[0] = _offset_x[0]
                if len(set(_offset_y)) == 1:
                    axis_map[1] = i
                    axis_sign[1] = j
                    offset[1] = _offset_y[0]
                if len(set(_offset_z)) == 1:
                    axis_map[2] = i
                    axis_sign[2] = j
                    offset[2] = _offset_z[0]

        if any([_ == None for _ in offset]):
            return False

        other.offset = offset
        other.axis_map = axis_map
        other.axis_sign = axis_sign
        other.align_points()
        return True

    def align_points(self):
        for i in range(len(self.points)):
            x, y, z = self.axis_map
            sx, sy, sz = self.axis_sign

            new_x = self.offset[0] + sx * self.points[i][x]
            new_y = self.offset[1] + sy * self.points[i][y]
            new_z = self.offset[2] + sz * self.points[i][z]

            self.points[i][0] = new_x
            self.points[i][1] = new_y
            self.points[i][2] = new_z


scanners = parse(data)
# pt 1
to_process = scanners[:]
processed = [scanners[0]]
to_process.pop(0)
while to_process:
    scanner = to_process.pop(0)
    for i, aligned in enumerate(processed):
        ok = aligned.find_overlapping(scanner)
        if ok:
            break
    if ok:
        processed.append(scanner)
    else:
        to_process.append(scanner)

points = []
for scanner in processed:
    for point in scanner.points:
        if point in points:
            continue
        else:
            points.append(point)
print(len(points))

# pt 2
res = 0
for i in range(len(processed)):
    for j in range(i, len(processed)):
        s1 = processed[i]
        s2 = processed[j]

        dist = (
            abs(s1.offset[0] - s2.offset[0])
            + abs(s1.offset[1] - s2.offset[1])
            + abs(s1.offset[2] - s2.offset[2])
        )
        if dist > res:
            res = dist
print(res)

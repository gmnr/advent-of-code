#!/usr/bin/python3


import re

# open input file
with open('input.txt', 'r') as f:
    data = f.readlines()    # to remove the last carriage return


regex = r"\d+"

checksum = 0
for line in data:
    row = re.findall(regex, line)

    # convert strings into int
    row = [int(x) for x in row]

    checksum += max(row) - min(row)

print(checksum)

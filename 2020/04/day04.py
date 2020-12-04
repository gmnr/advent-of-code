#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 4 2020
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read()


import re


blank = r"(?:\r?\n){2,}"
data = re.split(blank, data)


class Passports:

    def __init__(self, data):
        self.passports = [Document.fromString(x) for x in data]

    def valids(self):
        return sum(x.valid() for x in self.passports)

class Document:

    def __init__(self, birth, issue, exp, height, hair, eye, p_id, c_id):
        self.birth = birth
        self.issue = issue
        self.exp = exp
        self.height = height
        self.hair = hair
        self.eye = eye
        self.p_id = p_id
        self.c_id = c_id

    def valid(self):
        return False not in list(self.__dict__.values())

    def validateField(field, value):
        if field == "byr":
            value = int(value)
            if value in range(1920, 2003):
                return value
            else:
                return False
        elif field == "iyr":
            value = int(value)
            if value in range(2010, 2021):
                return value
            else:
                return False
        elif field == "eyr":
            value = int(value)
            if value in range(2020, 2031):
                return value
            else:
                return False
        elif field == "hgt":
            val = value[0:-2]
            dim = value[-2:]
            if dim == 'in':
                val = int(val)
                if val in range(59, 77):
                    return str(val) + dim
                else:
                    return False
            elif dim == "cm":
                val = int(val)
                if val in range(150, 194):
                    return str(val) + dim
                else:
                    return False
            else:
                return False
        elif field == "hcl":
            return bool(re.match(r"#[0-9a-f]{6}", value))
        elif field == "ecl":
            return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        elif field == "pid":
            return bool(re.match(r"^\d{9}$", value))

    @classmethod
    def fromString(cls, string):
        sep = r"\n+| +"
        characteristics = re.split(sep, string)
        characteristics = filter(None, characteristics)

        c = {
            "byr": False,
            "iyr": False,
            "eyr": False,
            "hgt": False,
            "hcl": False,
            "ecl": False,
            "pid": False,
            "cid": "Invalid"
        }

        for char in characteristics:
            ch, value = char.split(':')
            c[ch] = cls.validateField(ch, value)   # apply function for pt 2
            # c[ch] = value   # uncomment for soluton of pt. 1

        params = [v for k,v in c.items()]
        return cls(*params)

pas = Passports(data)
print(pas.valids())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Intcode Class and helper functions
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


class Intcode():

    def __init__(self, data):
        self.data = data


    @property
    def instructions(self):

        instructions = self.data.strip().split(",")
        instructions = [int(x) for x in instructions]

        return instructions

    


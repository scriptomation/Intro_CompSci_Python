#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 13:28:18 2017

@author: tstone
"""

s = 'bobobooooobbbooobobbo'
count = 0
for vowel in s:
    if vowel in 'bob':
        count += 1
print("Number of times bob occurs is: " + str(count))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 18:18:14 2017

@author: tstone
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    index = len(aStr) // 2
    if aStr == '':
        return False
    elif char == aStr[index]:
        return True
    elif len(aStr) <= 1:
        return False
    elif char < aStr[index]:
        return isIn(char,aStr[:index])
    else:
        return isIn(char,aStr[index:])
    
    

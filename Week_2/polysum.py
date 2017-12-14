#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:55:31 2017

@author: tstone
"""

def polysum(n,s):
    '''
    This functions sums the area and perimeter of the regular polygon.
    
    Returns the sum, rounded to 4 decimal places
    '''
    from math import tan
    from math import pi
    
    area = (0.25 * n * s**2)/tan(pi/n)
    perimeter = n*s
    
    return round(area + perimeter**2,4)

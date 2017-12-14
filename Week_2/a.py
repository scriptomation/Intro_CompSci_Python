#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:56:31 2017

@author: tstone
"""
def polysum(n,s):
    '''
    This functions imports the tan and pi function from the math module.
    
    This function will take two variables: n and s
    n is the number of sides for the polygon
    s is the length of the sides
    
    The function will calculate the area and perimeter of the polygon.
    
    Returns the sum of the area and square of the perimeter, roudn to 4 decimal 
    places
    '''
    from math import tan
    from math import pi
    
    area = (0.25 * n * s**2)/tan(pi/n)
    perimeter = n*s
    
    return round(area + perimeter**2,4)
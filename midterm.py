# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 12:22:33 2016

@author: mathias
"""
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    new = num // base
    for i in range(new):
        cal = base ** i
        if cal > num:
            if cal-num > base ** (i-1):
                return i-1
            else:
                return i
    
print(closest_power(9, 70)) # returns 2





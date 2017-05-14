# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:02:01 2016

@author: mathias


Using a list of function and apply a number
"""

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


def square(a):   
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1
    
L = [1,2,3]

print(applyEachTo([inc, max, int], -3))
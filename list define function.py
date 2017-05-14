# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 19:58:08 2016

@author: mathias
"""

def inc(a):
    return a+1
    

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
        
testList = [1, -4, 8, -9]

#applyToEach(testList, inc)

def mult(a):
    return a*a
    
applyToEach(testList, mult)
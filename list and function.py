# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 19:47:29 2016

@author: mathias
"""

"""
assumes L is a list , f is a function
mutates L by replacing each element e, of L by f(e)
"""

def applyToEach (L,f):
    
    for i in range(len(L)):
        L[i] = f(L[i])
        print(L[i])
        

L = [1,-2,3.4,4]


applyToEach(L, abs)
applyToEach(L, int)

map(abs, [1,-2,3.4])

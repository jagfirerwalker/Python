# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 20:54:51 2016

@author: mathias
"""

def mult(a,b):
    if b == 1 :
        return a
    else:
        return a + mult(a, b-1)
        
    
print (mult(1,10))

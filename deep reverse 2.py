# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 13:58:31 2016

@author: mathias
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    for i in range(len(L)):
        L[i].reverse() 
    L.reverse()
    return L
        
L = [[0, 1, 2], [1, 2, 3]]
print(deep_reverse(L)) 




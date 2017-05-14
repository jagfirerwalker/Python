# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 21:08:39 2016

@author: ericgrimson
"""

def dotProduct(L1, L2):
    """ 
    listA: a list of numbers
    listB: a list of numbers of the same length as listA

    """
    multiplication = []
    cal = 0
    for index in range(len(L1)):
        multiplication.append(L1[index]*int(L2[index]))
    for index in range(len(multiplication)):
        cal += multiplication[index]
    return cal

L1 = [1, 2, 3]
L2 = [4, 5, 6]

print(dotProduct(L1, L2))
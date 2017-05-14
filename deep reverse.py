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
    sortedList= []
    
    sortedList = sorted([item for sublist in L for item in sublist], reverse=True)

    itemsCounter = 0
    subItemsCounter = 0
    sortedListCounter = 0
    for items in L:
        for subitems in items:
            L[itemsCounter][subItemsCounter] = sortedList[sortedListCounter]
            sortedListCounter += 1
            subItemsCounter += 1
        subItemsCounter = 0
        itemsCounter += 1
     
    return L
        
L = [[0, -1, 2, -3, 4, -5]]
deep_reverse(L) 
print(L)

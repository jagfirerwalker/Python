# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:42:57 2016

@author: mathias
"""

animals = { 'a': [], 'b': [1, 7, 5, 4, 3, 18, 10, 0]}


def biggest(aDict):
    
    result = 0
    for counter in aDict:
        
        result = max(aDict.keys())
    return result
    
print (biggest(animals))
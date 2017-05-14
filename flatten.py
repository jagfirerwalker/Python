# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 13:53:04 2016

@author: mathias
"""

def flatten(l, ltypes=(list, tuple)):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)
        
list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(list))


# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 20:12:58 2016

@author: mathias
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    difference = {}    
    intersect = {}
    tpl = ()
    
    
    difference_list = list(d1.keys() - d2.keys()) + list(d2.keys() - d1.keys())
    intersect_list = list(d1.keys() & d2.keys())
    
    
    for i in intersect_list:
        intersect[i] = f(d1.get(i),d2.get(i))
    
    
    for i in difference_list:
        if d1.get(i):
            difference[i] = d1.get(i)
        elif d2.get(i):
            difference[i] = d2.get(i)
        else:
            difference[i] = 0
    tpl = (intersect,difference)
    
    return tpl


def f(a,b):
    return a > b
    
d1 = {1: 0, 2: 1, 3: 2, 4: 3, 5: 0}
d2 = {1: 1, 2: 2, 3: 3, 4: 5, 6: 2}

print(dict_interdiff(d1, d2))
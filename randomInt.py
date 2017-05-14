# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 10:04:05 2016

@author: mathias
"""

import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.randrange(0,100,2)
    
print (genEven())

def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1
        

def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)
    
def dist5():
    return int(random.random() * 10)

def dist6():
    return random.randint(0, 10)
    
'''
The random.random() distribution is uniform, and so is the random.randint() distribution. 
However unlike random.randrange(start, end), random.randint(start, end) returns a distribution that is inclusive of 
both the given start and end points.
Thus dist5 is a discrete uniform distribution over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
but dist6 is a discrete uniform distribution over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
'''
        
print (dist5() , dist6())
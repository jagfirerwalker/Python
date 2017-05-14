# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 10:11:20 2016

@author: mathias
"""
import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randrange(10, 22, 2)

print(stochasticNumber())
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 18:10:05 2016

@author: mathias
"""

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
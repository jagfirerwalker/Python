# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 18:15:07 2016

@author: mathias
"""

x = 25
epsilon = 0.001
numGuesses = 0
low = 0.0
high = x

ans = (high + low) / 2.0

while abs(ans**2-x) >= epsilon:
    print('low = ' +str(low) + ' high = ' + str(high))
    print('test ans = ' +str(ans))
    numGuesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0

print('numGuesses = ' + str(numGuesses))
print(str(ans) + 'is close to square root of ' + str(x))

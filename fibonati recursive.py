# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 22:42:28 2016

@author: mathias
"""

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
        
#for i in range(121):
#    print('fib(' + str(i) +') =' , fib(i))
    
def powerfib(n, memo = {}):
    
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = powerfib(n-1, memo) + powerfib(n-2, memo)
        memo[n] = result
        return result
        
for i in range(131):
    print('fib(' + str(i) +') =' , powerfib(i))
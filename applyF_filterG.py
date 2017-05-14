# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 12:56:49 2016

@author: mathias
"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    
    counter = 0     #helper counter
    listMatchingRule = []   #list of number that match the rule
    
    for i in range(len(L)):
          if g(f(L[i])):
              listMatchingRule.append(L[i]) #if number in L matches rule put them in listmatchRule
    
    Lcopy = L.copy() #create copy of L to allow loop function
    
    for i in range(len(Lcopy)):
        if not L[counter] in listMatchingRule: #if number in L is not matching to listMatchRule
            L.remove(L[counter]) #remove it from the lst
            counter = counter #everytime a number is remove stay in the same spot and rerun 
        else:
            counter += 1 #else move on
    
    if len(listMatchingRule) > 0:
        return max(listMatchingRule)
    else:
        return -1


def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)
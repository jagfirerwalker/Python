# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 13:06:24 2016

@author: mathias
"""

def genSubsets(L):
        res = []
        if len(L)==0:
            return [[]] #list of empty list
        smaller = genSubsets(L[:-1]) # all subsets without last element
        
        extra = L[-1:] #create a list of just last element
        new = []
        for small in smaller:
            new.append(small+extra) # for all smaller solutions, add one with last element
        return smaller+new # combine those with last elemtn and those without
        

L = [1,2,3,4]
print(genSubsets(L))
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 21:35:40 2016

@author: mathias
"""

def printMove(n,fr, to):
        print(str(n) + " disk move from " + str(fr) + " to " + str(to))
        

def Tower(n, fr, to, spare):
    if n == 1:
        printMove(n, fr, to)
    else:
        Tower(n-1, fr, spare, to)
        Tower(1, fr, to, spare)
        Tower(n-1, spare, to, fr)
        
        
print(Tower(3, "P1", "P2", "P3"))
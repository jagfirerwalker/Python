# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 18:44:37 2016

@author: mathias
"""

"""
creating an alias for the same list
"""


hot = ['red', 'orange', 'yellow']
warm = []

warm = hot

hot.append('pink')
print (hot)
print (warm)

"""
creating a clone
"""

cool = ['blue', 'green', 'grey']
cold = []

cold = cool[:]

print (cold)

cold.append('black')

print (cold)
print (cool)

"""
List of list

"""

brightcolour = [warm]
print (brightcolour)

brightcolour.append(cold)
print (brightcolour)

cold.append('silver')

print (brightcolour)

"""
remove dublicated WRONG WAY!!!!!
"""

def removedub(L1,L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
            
L1 = [1,2,3,4,5]
L2 = [1,2,5,6]

removedub(L1,L2)
print('wrong way')
print (L1)
print (L2)

"""
remove dublicate RIGHT WAY!!!
"""

def removedub_new(L1,L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
            
L3 = [1,2,1,3,4,5]
L4 = [1,2,5,6]

removedub_new(L3,L4)
print('right way')
print (L3)
print (L4)           



# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:17:38 2016

@author: mathias
"""

grades = {'Mike':'B','John':'C','Jennifer':'A+'}

grades.keys()
grades.values()

"""
add value to dictionaries

"""

grades['Bruna'] = 'A'

grades['John']


"""
Examples Dictionaries

"""


animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'
'donkey' in animals.values() #is the word donkey as a value in animals
len(animals['a']) #how many characteres has the 'a' index
animals.keys()
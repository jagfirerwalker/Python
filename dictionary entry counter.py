# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:35:14 2016

@author: mathias

Counter of entries
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(animals):
    counter = 0
    for i in animals.values():
        counter += len(i)
    return counter
    
print (how_many(animals))

def how_many_1(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will 
        #  be a list of lists
        result += len(value)
    return result
    
print (how_many_1(animals))

def how_many_2(aDict):
    '''
    Another way to solve the problem.

    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result
    
print(how_many_2(animals))
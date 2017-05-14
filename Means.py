# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:12:55 2016

@author: mathias
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    n = len(L)
    if n == 0:
        return float('NaN')
    lengths = [len(s) for s in L] # calculation with characters
    
    means = sum(lengths) / n 
    print(means)
    
    squareLen = [l**2 for l in lengths]
    variance =  sum(squareLen) / n - means**2
    return variance ** (.5)
    
#L = ['apples', 'oranges', 'kiwis', 'pineapples']
#print(stdDevOfLengths(L))

def coefficentOfVariance(L):
    """
    L: a list of int
    
    returns: calculation of coeffience of Variance 
    to find the ratio of standard deviation ((σ) to mean (μ). The main purpose of finding coefficient of variance (often abbreviated as CV) is used to study of quality assurance by measuring the dispersion of the population data of a probability or frequency distribution, or by determining the content or quality of the sample data of substances. The method of measuring the ratio of standard deviation to mean is also known as relative standard deviation often abbreviated as RSD. It only uses positive numbers in the calculation and expressed in percentage values. Therefore, the resultant value of this formula CV = (Standard Deviation (σ) / Mean (μ)) will be multiplied by 100. CV is important in the field of probability & statistics to measure the relative variability of the data sets on a ratio scale. In probability theory and statistics, it is also known as unitized risk or the variance coefficient.
    
    """
    n = len(L)
    if n == 0:
        return float('NaN')
    
    mean = sum(L) / float(len(L))
    tot = 0.0
    for number in L:
        tot += (number - mean)**2
    std = (tot/len(L))**0.5
    coef = std / mean
    return mean, std, coef
    
    
L = [10, 4, 12, 15, 20, 5]
print(coefficentOfVariance(L))

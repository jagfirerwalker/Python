# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:26:04 2016

@author: mathias
"""
import math


def polysum(n,s):
 
    
    area = (0.25 * n * s**2) / (math.tan(math.pi/n))
    area = area+((n*s)**2)
    return  round(area,4)

#print("%.4f" % polysum(85,86))
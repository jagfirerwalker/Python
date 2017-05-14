# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:17:10 2016

@author: mathias
"""

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''

    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si','5':'wu', '6':'liu', 
    '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
          
    numberList = list(us_num)
    chinieseNumb = ""
    
    if int(us_num) < 10:
        chinieseNumb += trans[numberList[0]]
    elif int(us_num) == 10:
        chinieseNumb += trans['10']
    elif (int(us_num) > 10) and (int(us_num) < 20):
        chinieseNumb += trans['10'] + ' ' + trans[numberList[1]]
    elif int(us_num) >= 20:
        if not numberList[1] == '0':
                chinieseNumb += trans[numberList[0]] + " " + trans['10'] + " " + trans[numberList[1]]
        else:
                chinieseNumb += trans[numberList[0]] + " " + trans['10']
    
    return chinieseNumb
    
    
print(convert_to_mandarin('70'))
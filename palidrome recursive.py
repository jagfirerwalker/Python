# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 22:53:12 2016

@author: mathias
"""

def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmopqrstuvwxyz':
                ans = ans+c
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else: 
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))
    

print(isPalindrome('eve'))
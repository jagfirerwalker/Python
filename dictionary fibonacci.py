# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:55:39 2016

@author: mathias


Fibonaci solution done with dictionary

Much better as it doesn't need to recalculate ever single step anew, it can remember what it has calculated, save it and recall it to speed 
up the process.
"""


def fib_recursive(x): #Fib recursive

    if x == 0 or x == 1:
        return 1
    else:
        return fib_recursive(x-1) + fib_recursive(x-2)
        
def fib_recursive_2(n): #same as the example above but with a slide change in calculation
    global numFibCalls #global variable 
    
    numFibCalls += 1

    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib_recursive_2(n-1)+fib_recursive_2(n-2)

def fib_efficient(n,d): #Fib dictionary
    global numFibCalls #global variable 
    
    numFibCalls += 1
    
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1,d) + fib_efficient(n-2,d)
        d[n] = ans
        return ans
        

rabbits = 12



numFibCalls = 0
print("Fib done via recursive: ", fib_recursive_2(rabbits))
print ("Amount of Fib calls nedded: ", numFibCalls)


d = {1:1, 2:2}
numFibCalls = 0
print ("Fib done via dictionary: ", fib_efficient(rabbits,d))
print ("Amount of Fib calls nedded: ", numFibCalls)
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 18:15:07 2016

@author: mathias
"""

x = int(input("Please think of a number between 0 and 100! "))

numGuesses = 0
low = 0
high = 100
epsilon = 0
ans = int((high + low) / 2)


while abs(ans-x) >= epsilon:
    print("Is your secret number " +str(ans) + "?")
    numGuesses += 1
    answer = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    if answer == "l":
        low = ans
        ans = int((high + low) / 2)
    elif answer == "h":
        high = ans
        ans = int((high + low) / 2)
    elif answer == "c":
        print("Game over. Your secret number was: " + str(ans))
        break
    else: 
        print("Sorry, I did not understand your input.")
        
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 14:09:22 2016

@author: mathias

Calculating credit card interest rates, over an x amount of months, while only paying the absolute minimum necessary.
Printing out end of year balance after each month x% has been paid.
Program is meant to run in recursive manner
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month_counter = 0


def credit_card_pay_off(remaining_balance):
    global month_counter
    
    if month_counter == 12:
               
        return remaining_balance
        
    else:
        month_counter +=1
        
        minimum_monthly_payment = remaining_balance * monthlyPaymentRate
        unpaid_balance = remaining_balance - minimum_monthly_payment
        
        interest = annualInterestRate / 12 * unpaid_balance
        
        return round(credit_card_pay_off(unpaid_balance + interest),2)
        
        
        
        
        
print ("Remaining Balance: " + str(credit_card_pay_off(balance)))
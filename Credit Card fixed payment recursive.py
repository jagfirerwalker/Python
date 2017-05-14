# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 15:46:38 2016

@author: mathias
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 14:09:22 2016

@author: mathias

Calculating credit card interest rates, over an x amount of months, while only paying the absolute minimum necessary.
Printing out end of year balance after each month x% has been paid.
Program is meant to run in recursive manner
"""
#
#
#balance = 3329
#annualInterestRate = 0.2
#payment_variable = 0
#annualInterest = annualInterestRate * balance
#monthlyInterestRate = annualInterestRate /12


#def credit_card_fixed_payment(remaining_balance):
#    global payment_variable
#    global month
#    
#    print (payment_variable, total_balance - payment_variable * 12, total_balance)
#    if  corrent_answer <= payment_variable:         
#        return payment_variable
#        
#    else:
#        payment_variable += 10
#        
#        remaining_balance = credit_card_fixed_payment((remaining_balance - payment_variable) + monthlyInterestRate)       
#        return payment_variable
#        
#                
#print (" Lowest Payment:", credit_card_fixed_payment(balance))  
#        
#

        

balance = 3329
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
monthlyPayment = 0
newbalance = balance
while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance
    month = 1
    while month <= 12 and newbalance > 0:
        newbalance -= monthlyPayment
        newbalance += (monthlyInterestRate * newbalance)
        month += 1    
print ("Lowest Payment:",monthlyPayment)
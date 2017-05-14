# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 15:46:38 2016

@author: mathias
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 14:09:22 2016

@author: mathias

Using Bisectional search to discover that the optimial monthly credit card payment should be
"""

        

#balance = 999999 
#annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate/12
annualBalance = balance + balance*annualInterestRate


low_bound_balance = balance /12 #lowest possible payment, if no interest apply
high_bound_balance = balance*((1+monthlyInterestRate)**12)/12 #highest possible interest if no payment is being done till last months
monthlyPayment = (low_bound_balance+high_bound_balance)/2 #calculating first test scenario for payment
newbalance = balance    

epsilon = 0.001 #margin of error


while abs(newbalance) > epsilon:
#    print('low = ', round(low_bound_balance,2), ' high = ', round(high_bound_balance,2))
#    print('Monthly Payment = ',round(monthlyPayment,2))
#    print('Left to pay = ', round(annualBalance-(monthlyPayment*12),2))
#    print('New Balance = ', newbalance)
    
    newbalance = balance
    month = 1
    
    while month <= 12 and newbalance > 0:
        newbalance -= monthlyPayment
        newbalance += (monthlyInterestRate * newbalance)
        month += 1  
        
    if (newbalance) > epsilon:
        low_bound_balance = monthlyPayment
    else:
        high_bound_balance = monthlyPayment
    monthlyPayment = (low_bound_balance+high_bound_balance)/2
    
    
print ("Lowest Payment:",round(monthlyPayment,2))

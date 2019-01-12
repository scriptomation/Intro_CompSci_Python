#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:54:16 2018

@author: tstone
"""

balance = [3329, 4773, 3926]
annualInterestRate = 0.2

def monthlyPayments(balance,annualInterestRate,monthlyPaymentRate = 0):
    '''
    Calculates the required monthly payments to pay off loan in 1 year
    mIR: monthly interest rate
    nbalance: new balance
    
    '''
    mIR = annualInterestRate / 12
    nbalance = balance
    for i in range(1,13):
        nbalance = nbalance - monthlyPaymentRate
        nbalance = nbalance*(mIR + 1)
    if nbalance <= 0:
        return monthlyPaymentRate
    else:
        return monthlyPayments(balance,annualInterestRate,monthlyPaymentRate + 10)


print('Lowest Payment:',monthlyPayments(balance, annualInterestRate))
    

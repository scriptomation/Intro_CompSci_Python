#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 17:09:36 2018

@author: tstone

Complete 
"""

balance = 320000
annualInterestRate = 0.2

def monthlyPayments(balance,annualInterestRate,uB = 0, lB = 0):
    '''
    Calculates the required monthly payments to pay off loan in 1 year
    mIR: monthly interest rate
    nbalance: new balance
    lB: lower bound for bisection search
    uB: upper bound for bisectino search
    '''
    mIR = annualInterestRate/12
    uB = (balance*(1+mIR)**12)/12
    lB = balance/12
    nbalance = balance
    while nbalance >= 0.001:
        nbalance = balance
        guess = (uB + lB)/2
        for i in range(1,13):
            nbalance = nbalance - guess
            nbalance = nbalance*(mIR + 1)
        if nbalance < 0.00:
            uB = guess
        elif nbalance > 0.00:
            lB = guess
        else:
            break
        nbalance = abs(nbalance)
    return round(guess,2)

print('Lowest Payment:',monthlyPayments(balance, annualInterestRate))

    

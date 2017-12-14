#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:37:05 2017

@author: tstone

This was not completed, will come back to later - Dec 10 20:37:05 2017
"""

#Outstanding balance on the credit card

def cc_balance(balance,annualInterestRate,monthlyPaymentRate):
    '''
    Function calculates the remaining balance after payint the credit card
    for 1 year
    
    balance: outstanding balance on the credit card


    annualInterestRate: Annual interest rate as a decimal

    monthlyPaymentRate: Minimum monthly payment rate as a decimal
    
    returns the remaining balance
    

    monthlyInterestRate = annualInterestRate/12.0
    minMonPayment = monthlyPaymentRate * previousBalance
    unpaidBalance = previousBalance - minMonPayment
    balance = unpaidBalance + monthlyInterestRate * unpaidBalance

    returns the remaining balance after 12 months
    '''

    monthlyInterestRate = annualInterestRate/12.0
    minMonPayment = monthlyPaymentRate * balance
    unpaidBalance = balance - minMonPayment
    totalMonPayment = 0

    month = 0
    while month < 12:
        month += 1
        minMonPayment = round(monthlyPaymentRate * balance,2)
        unpaidBalance = round(balance - minMonPayment,2)
        balance = round(unpaidBalance + monthlyInterestRate * unpaidBalance,2)
        totalMonPayment += minMonPayment
    print('Remaining Balance:',str(balance))
    print('Total payments made:',str(round(totalMonPayment,2)))

#!/usr/balancein/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:43:10 2018

@author: tstone

balancealance: the outstanding balancealance on the credit card
annualInterest rate: annual intestest rate as a decimal
monthlyPaymentRate: minimum monthly payment rate as a decimal 
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def monthlyPayments(balance,annualInterestRate,monthlyPaymentRate):
    mIR = annualInterestRate / 12
    for i in range(1,13):
        balance = balance*(mIR + 1)
        mP = balance * monthlyPaymentRate
        nbalance = balance - mP
        balance = nbalance
    return round(balance,2)


print('Remaining balance:',monthlyPayments(balance, annualInterestRate,monthlyPaymentRate))


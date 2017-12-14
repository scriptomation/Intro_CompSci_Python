#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 23:12:28 2017

@author: tstone
"""

balance = 3926
annualInterestRate = 0.2

def staticMonPay(balance,aIntRate,MonPayRate):
    mon = 0
    mIntRate = aIntRate/12.0
    upBal = round(balance - MonPayRate,2)
    while mon < 12:
        mon += 1
        balance = round(upBal + upBal*mIntRate,2)
        upBal = round(balance - MonPayRate,2)
    return balance

monthlyPayment = 0
remaining = balance
while remaining >= 0:
    monthlyPayment += 10
    remaining = staticMonPay(balance,annualInterestRate,monthlyPayment)
print('Lowest Payment:',str(monthlyPayment))
    

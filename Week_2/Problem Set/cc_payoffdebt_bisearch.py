#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 00:22:32 2017

@author: tstone
"""

balance = 4773
annualInterestRate = 0.2

def staticMonPay(balance,aIntRate,MonPayRate):
    '''
    staticMonPay takes the balance, Annual Interest Rate, and Monthly Payment
    and returns the balance after making 12 payments.  
    '''
    mon = 0
    mIntRate = aIntRate/12.0
    nbalance = balance
    upBal = round(nbalance - MonPayRate,2)
    while mon < 12:
        mon += 1
        nbalance = round(upBal + upBal*mIntRate,2)
        upBal = round(nbalance - MonPayRate,2)
    if nbalance <= 0:
        return MonPayRate
    else:
        return staticMonPay(balance,aIntRate,MonPayRate)

def noPayment(balance,aIntRate):
    mon = 0
    mIntRate = aIntRate/12.0
    while mon < 12:
        mon += 1
        balance = round(balance + balance*mIntRate,2)
    return balance

lbound = round(balance / 12,2)
ubound = round(noPayment(balance,annualInterestRate),2)



    

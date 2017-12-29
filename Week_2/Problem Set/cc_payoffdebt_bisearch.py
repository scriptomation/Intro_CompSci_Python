#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 00:22:32 2017

@author: tstone
"""

balance = 999999
annualInterestRate = 0.18
mIntRate = annualInterestRate/12.0

def staticMonPay(balance,mIntRate,MonPayRate):
    '''
    given the balance, monthly interest rate and monthly payment rate the 
    function will return the balance after paying off the debt for 12 months
    '''
    month = 0
    nbalance = balance
    upBal = nbalance - MonPayRate
    while month < 12:
        month += 1
        nbalance = upBal + upBal*mIntRate
        upBal = nbalance - MonPayRate
    return nbalance

lbound = balance / 12.0
ubound = (balance * (1 + mIntRate)**12) / 12.0

guess = (ubound + lbound) / 2
gremaining = staticMonPay(balance,mIntRate,guess)
lremaining = staticMonPay(balance,mIntRate,lbound)
uremaining = staticMonPay(balance,mIntRate,ubound)

while round(gremaining,2) != 0:
    if gremaining < 0:
        ubound = guess
    else:
        lbound = guess
    guess = (ubound + lbound) / 2
    gremaining = staticMonPay(balance,mIntRate,guess)
    lremaining = staticMonPay(balance,mIntRate,lbound)
    uremaining = staticMonPay(balance,mIntRate,ubound)
print(str(round(guess,2)))
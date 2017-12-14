#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 23:12:28 2017

@author: tstone
"""

balance = 4773
annualInterestRate = 0.2

def staticMonPay(balance,aIntRate,MonPayRate):
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
        return staticMonPay(balance,aIntRate,MonPayRate+10)
    

    

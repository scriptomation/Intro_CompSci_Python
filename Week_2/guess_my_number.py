#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 00:17:52 2017

@author: tstone
"""

letter = ''
guess = 50
low = 0
high = 100
guess = int((high + low)/2)
num_guess = 0
print("Please think of a number between 0 and 100!",)
while letter != 'c':
    print("Is your secret number " + str(guess) + "? ")
    letter = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    while letter != 'h' and letter != 'l' and letter != 'c':
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(guess) + "? ")
        letter = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if letter == 'h':
       high = int(guess)
    elif letter == 'l':
        low = int(guess)
    else:
        break
    guess = int((high + low)/2)
    num_guess += 1
print("Game over. Your secret number was: " + str(guess))
    

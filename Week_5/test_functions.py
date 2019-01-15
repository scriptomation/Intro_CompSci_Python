#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 18:00:13 2019

This is a test function

@author: tstone
"""

import string
import ps6

#Testing the build_shift_dict method for the Message class
testMes = Message('hello')

alphabet_test = string.ascii_lowercase
shift3 = 'defghijklmnopqrstuvwxyzabc'
shift1 = 'bcdefghijklmnopqrstuvwxyza'
shift19 = 'tuvwxyzabcdefghijklmnopqrs'
testDict3 = testMes.build_shift_dict(3)
testDict1 = testMes.build_shift_dict(1)
testDict19 = testMes.build_shift_dict(19)
def test_build_function(shift_letters,test_dict):
     for i in range(0,26):
         if shift_letters[i] !=  test_dict[alphabet_test[i]]:
             print('mismatch at index ' + str(i))
             print('for letter ' + shift_letters[i] + ' comes to ' + \
                   test_dict[alphabet_test[i]])
print()
print('starting test for shift3 and testDict3...')
test_build_function(shift3, testDict3)
print('starting test for shift1 and testDict1...')
test_build_function(shift1, testDict1)
print('starting test for shift19 and testDict19...')
test_build_function(shift19,testDict19)


#Testing for Apply shift


def test_apply(caesar, testMes,shift):
     if caesar != testMes.apply_shift(shift):
         print('*************')
         print(caesar + ' does not equal ' + testMes.apply_shift(shift))
         print('*************')


print('testing Apply shift function for all lower case')
testMes3 = Message('hello')
caesar3 = 'khoor'
testMes3U = Message('HelLo')
caesar3U = 'KhoOr'
print('testing all lower case')
test_apply(caesar3, testMes3,3)
print('testing mix upper case and lower')
test_apply(caesar3U, testMes3U,3)
 
print('testing Apply shift function for all lower case')
testMes19 = Message('hello')
caesar19 = 'axeeh'
testMes19U = Message('HelLo')
caesar19U = 'AxeEh'
print('testing all lower case')
test_apply(caesar19, testMes19,19)
print('testing mix upper case and lower')
test_apply(caesar19U, testMes19U,19)

print()
print('testing Apply shift function for all upper, lower and numbers')
testMes19 = Message('He!l lo5')
caesar19 = 'Ax!e eh5'
testMes19U = Message('hel**Lo5')
caesar19U = 'axe**Eh5'
print('testing all lower case')
test_apply(caesar19, testMes19,19)
print('testing mix upper case and lower')
test_apply(caesar19U, testMes19U,19)

#Test functions for problem 2
print()
print('Testing Plaintextmessage class.....')
pt3 = PlaintextMessage('hello',3)
if caesar3 != pt3.message_text_encrypted:
    print('encrypted text is incorrect. Is ' + t2.message_text_encrypted \
          + ' should be ' + caesar3)
pt3.change_shift(19)
caesar19 = 'axeeh'
if caesar19 != pt3.message_text_encrypted:
    print("shift did not work. Is " + pt3.message_text_encrypted + \
          " should be " + caesar19)

print()
print("Testing CiphertextMessage class ......")
with open('story.txt') as f:
    content = f.readlines()
content = "".join(content)
ciphertext2 = CiphertextMessage(content)
print('Story line is:', ciphertext2.decrypt_message())



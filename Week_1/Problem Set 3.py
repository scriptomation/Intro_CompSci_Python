# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#s = 'azcbobobegghakl'
s = 'abcbcd'

#alphabetical order
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#temporary storage of alphabet
sindex = 0
tmpletter = ''
tmporder = ''
#variable used to store the string with the longest alphabetical order
laorder = ''

count = 0
aindex = 0
for letter in s:
    #function to find where the letter is in the alphabet string
    for item in alphabet:
        if item == letter: #or (aindex >= len(alphabet) - 1):
            break
        aindex += 1
    #goes through each letter in string starting from index and compares to the
    #last
    tmpletter = letter
    for item2 in s[sindex:]:
        if tmpletter <= item2:
            tmpletter = item2
            tmporder += tmpletter
        else:
            break
    if len(tmporder) > len(laorder):
        laorder = tmporder
    #reset alphabet index   
    aindex = 0
    #Increment string index
    sindex += 1
    tmporder = ''
print('Longest substring in alphabetical order is: ' + laorder)
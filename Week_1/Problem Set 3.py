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
lindex = 0
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
            #print("s letter is: " + letter)
            #print("Alphabet letter is: " + item)
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



    #function will test to see if the next letter is the same as the letter in
    #in the alphabet.  If it is it will add it to the tmporder variable
    #If not it will continue the function
#    for aletter in alphabet[aindex:]:
#        if aletter == letter or aletter == alphabet[aindex]:
#            count += 1
#            tmporder += aletter
#        else:
#            break
#        if len(tmporder) > len(laorder):
#            laorder = tmporder
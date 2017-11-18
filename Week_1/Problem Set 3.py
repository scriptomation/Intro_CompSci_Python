# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#s = 'azcbobobegghakl'
s = 'azcbobobegghakl'

#alphabetical order
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#temporary storage of alphabet
lindex = 0
tmporder = ''
#variable used to store the string with the longest alphabetical order
laorder = ''

count = 0
aindex = 0
for letter in s:
    #function to find where the letter is in the alphabet string
    for item in alphabet:
        if item == letter: #or (aindex >= len(alphabet) - 1):
            print("s letter is: " + letter)
            print("Alphabet letter is: " + item)
            break
        aindex += 1

    #function  
    aindex = 0


#reset variables
tmpindex = 0
tmporder = ''
laorder = ''
count = 0
index = 0   


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
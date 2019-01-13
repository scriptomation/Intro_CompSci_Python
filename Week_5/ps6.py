import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        if shift > 26:
            shift = shift % 26
        lowerAlphabet = string.ascii_lowercase
        shiftAlphabet = lowerAlphabet[shift:] + lowerAlphabet[:shift]
        shift_dict = {}
        for i in range(0,26):
            shift_dict[lowerAlphabet[i]] = shiftAlphabet[i]
            shift_dict[lowerAlphabet[i].upper()] = shiftAlphabet[i].upper()            
        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift)
        caesar_string = ""
        for l in self.message_text :
            try:
                caesar_string = caesar_string + shift_dict[l]
            except KeyError:
                caesar_string = caesar_string + l
        return caesar_string

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        pass #delete this line and replace with your code here

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        pass #delete this line and replace with your code here

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        pass #delete this line and replace with your code here

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        pass #delete this line and replace with your code here

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        pass #delete this line and replace with your code here


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        pass #delete this line and replace with your code here

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        pass #delete this line and replace with your code here

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())

#Testing the build_shift_dict method for the Message class
#testMes = Message('hello')
# =============================================================================
# #alphabet_test = string.ascii_lowercase
# #shift3 = 'defghijklmnopqrstuvwxyzabc'
# shift1 = 'bcdefghijklmnopqrstuvwxyza'
# shift19 = 'tuvwxyzabcdefghijklmnopqrs'
# testDict3 = testMes.build_shift_dict(3)
# testDict1 = testMes.build_shift_dict(1)
# testDict19 = testMes.build_shift_dict(19)
# def test_build_function(shift_letters,test_dict):
#     for i in range(0,26):
#         if shift_letters[i] !=  test_dict[alphabet_test[i]]:
#             print('mismatch at index ' + str(i))
#             print('for letter ' + shift_letters[i] + ' comes to ' + \
#                   test_dict[alphabet_test[i]])
# print()
# print('starting test for shift3 and testDict3...')
# test_build_function(shift3, testDict3)
# print('starting test for shift1 and testDict1...')
# test_build_function(shift1, testDict1)
# print('starting test for shift19 and testDict19...')
# test_build_function(shift19,testDict19)
# =============================================================================

#Testing for Apply shift

# =============================================================================
# def test_apply(caesar, testMes,shift):
#     if caesar != testMes.apply_shift(shift):
#         print('*************')
#         print(caesar + ' does not equal ' + testMes.apply_shift(shift))
#         print('*************')
# =============================================================================

# =============================================================================
# print('testing Apply shift function for all lower case')
# testMes3 = Message('hello')
# caesar3 = 'khoor'
# testMes3U = Message('HelLo')
# caesar3U = 'KhoOr'
# print('testing all lower case')
# test_apply(caesar3, testMes3,3)
# print('testing mix upper case and lower')
# test_apply(caesar3U, testMes3U,3)
# 
# print('testing Apply shift function for all lower case')
# testMes19 = Message('hello')
# caesar19 = 'axeeh'
# testMes19U = Message('HelLo')
# caesar19U = 'AxeEh'
# print('testing all lower case')
# test_apply(caesar19, testMes19,19)
# print('testing mix upper case and lower')
# test_apply(caesar19U, testMes19U,19)
# =============================================================================
# =============================================================================
# print()
# print('testing Apply shift function for all upper, lower and numbers')
# testMes19 = Message('He!l lo5')
# caesar19 = 'Ax!e eh5'
# testMes19U = Message('hel**Lo5')
# caesar19U = 'axe**Eh5'
# print('testing all lower case')
# test_apply(caesar19, testMes19,19)
# print('testing mix upper case and lower')
# test_apply(caesar19U, testMes19U,19)
# =============================================================================


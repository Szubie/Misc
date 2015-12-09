# -*- coding: utf-8 -*-
#5.2. Boolean Operations — and, or, not

#These are the Boolean operations, ordered by ascending priority:
#Operation 	Result 	Notes
#x or y 	if x is false, then y, else x 	(1)
#x and y 	if x is false, then x, else y 	(2)
#not x 	if x is false, then True, else False 	(3)

#Notes:

# This is a short-circuit operator, so it only evaluates the second argument if the first one is False.
# This is a short-circuit operator, so it only evaluates the second argument if the first one is True.
# not has a lower priority than non-Boolean operators, so not a == b is interpreted as not (a == b), and a == not b is a syntax error.


#DO NOT USE THE KEYWORD "in".

def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    vowel = "a" or "e" or "i" or "o" or "u"
    #have to repeat the = sign or this does not work.
    if char == vowel:
        return True
    else:
        return False
#This doesn't work, it doesn't recognise any vowels.

   
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    elif char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        return True
    else:
        return False
        
        
#Then required to add an "in". I just added a useless one into this code, however, the following is the proper way:
def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    if char in 'aeiouAEIOU':
        return True
    else:
        return False


# A shorter solution
def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    return char.lower() in 'aeiou'
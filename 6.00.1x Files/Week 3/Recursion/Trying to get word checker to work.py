secretWord = "lol"
lettersGuessed = "lol"

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    charB = " "
    n=0
    n2=0
    result =0
    charA = lettersGuessed[n2]
    charB =  secretWord[n]
    
    while True:
        if result == len(secretWord): 
            return True        
        if str(charA) == charB:
            result += 1
            n2 += 1
        else:
            if n+1 > len(secretWord) != False:
                n+1
            else: n2 += 1

    else:
        return False

isWordGuessed ("lol", "lol")


#Probably your code is using "if" they don't loop through the complete list.

#The idea of the question is that you should take a letter in "lettersGuessed" and loop through the "secret word" or vice versa. 

#Using a "for" loop, don't use a "while loop" with it, it doesn't go anywhere.
#Think you need to specify that everything is a string otherwise it will default to True when comparing them??

#Need to think smarter.
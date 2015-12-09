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
    
    while (n2) < (len(lettersGuessed)) and n < (len(secretWord)):
        charA = lettersGuessed[n2]
        charB = secretWord[n]       
        if str(charA) == str(charB):
            result += 1
            n2 += 1
        if str(charA) != str(charB):
            if (n + 1) < len(secretWord):
                n += 1
            else:
                if n2 + 1 < len(lettersGuessed):
                    n2 +=1
            #just n+1 doesn't work, need to have = sign to rebind it

    if result == len(secretWord): 
        return True
    else:
        return False

isWordGuessed ("lol", "lol")
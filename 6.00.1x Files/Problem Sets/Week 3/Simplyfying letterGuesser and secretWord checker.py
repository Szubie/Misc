secretWord = "lol"
lettersGuessed = "lol"

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    result = 0
    if len(lettersGuessed) == 0:
        return False
    for char in secretWord:
        if char in str(lettersGuessed):
            result += 1
    if result == len(secretWord):
        return True     
    if result < len(secretWord):
        return False
        
#interestingly, it only worked with "if char in lettersGuessed".
#"if char in lettersGuessed == True" did not work.
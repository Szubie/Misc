secretWord = "lol"
lettersGuessed = "lol"

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    n=0
    result = 0
    if len(lettersGuessed) == 0:
        return False
    #whoops, they checked result for empty guesses, didn't account for that.
    charB = lettersGuessed[n]
    
    for char in secretWord:
        n=0
        #also need to rebind n every time.
        charB = lettersGuessed [n]
        #must also be rebound
        if result == len(secretWord):
            return True
        if char == charB:
            result += 1
        if char != charB:
            while n < (len(lettersGuessed)-1):
                n += 1
                charB = lettersGuessed[n]
                #necessary to rebind it in loop
                if char == charB:
                    result += 1
                    break
                    #use breaks
                if (n + 1) > (len(lettersGuessed)-1):
                    break
    if result == len(secretWord):
            return True
    else:
        return False
        
#this SORT OF works, but actually doesn't count backwards for values of charB. So need to fix it checks each value of char with every possible value of charB.
# eventually reached this solution, but it seems overly complex, must be an easier and quicker way of doing it....
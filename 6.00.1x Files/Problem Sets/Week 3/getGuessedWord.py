lettersGuessed = "eikprs"
secretWord = "apple"

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    collect = ""
    #a collect string to catch all the answers and present them as a single output with proper formatting.
    for char in secretWord:
        if char in lettersGuessed:
            collect += char
        else:
            collect += "_ "
    return collect
    
#Forgot that a function NEEDS a return command, otherwise it will output "None".
#Well this went smoother than the other one....
#Although formatting is a bit dodgy here. Is it possible to fix?
#Possibility: set up a counting string which includes all of them.
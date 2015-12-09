lettersGuessed = "eikprs"
x=0
collect = ""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    x=0
    collect = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter in lettersGuessed:
            x+0
        else:
            collect += letter
    return collect
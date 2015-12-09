# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)



import random
import string

WORDLIST_FILENAME = "C:/Users/Benjy/Dropbox/Python/6.00.1x Files/Week 3/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

chooseWord(wordlist)


secretWord = chooseWord(wordlist)
lettersGuessed = ""

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
        
#interestingly, it only worked with "if char in lettersGuessed".
#"if char in lettersGuessed == True" did not work.





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
    
#Forgot that a function NEEDS a return command, otherwise it will output "None".
#Well this went smoother than the other one....
#Although formatting is a bit dodgy here. Is it possible to fix?
#Possibility: set up a counting string which includes all of them.





def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    collect = ""
    x=0
    collect = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter in lettersGuessed:
            x+0
        else:
            collect += letter
    return collect
    

n= 8
y = 0

def hangman(secretWord):
    
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''


    
    mistakesMade = 0
    lettersGuessed = ""
    user = 0
    turns = 8  
    lettersGuessed = ""
    n =8
    y=0

       
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is", len(str(secretWord)) , "letters long." #really wanted a comma before the len
    print "-------------"
    
    while mistakesMade < 3 and turns>1:
        mistakesMade = y
        turns = n
        
        if isWordGuessed(secretWord, lettersGuessed):
            return "Congratulations, you won!"          
        else:
            print str("You have"), turns, "guess left."  
            print "Available letters: ", getAvailableLetters(lettersGuessed)
            user = raw_input ("Please guess a letter: ")
            user = user.lower()
        if user in lettersGuessed:
            lettersGuessed += user
            print "Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed)
            print "-------------"   
            
        elif user in secretWord:
            lettersGuessed += user 
            print "Good guess:", getGuessedWord(secretWord, lettersGuessed)
            print "-------------"
        else:
            lettersGuessed += user
            n -=1    
            print "Oops! That letter is not in my word:" , getGuessedWord(secretWord, lettersGuessed)                
            print "-------------"
            
    if isWordGuessed(secretWord, lettersGuessed):
        return "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses. The word was:", secretWord
    
    







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

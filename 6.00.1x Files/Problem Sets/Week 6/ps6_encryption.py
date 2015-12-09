# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "C:/Users/Benjy/Dropbox/Python/6.00.1x Files/Problem Sets/Week 6/words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|//:;'<>?,.//")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("C:/Users/Benjy/Dropbox/Python/6.00.1x Files/Problem Sets/Week 6/story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    lowerCase = string.ascii_lowercase
    upperCase = string.ascii_uppercase
    lowerNew = string.ascii_lowercase[:] + string.ascii_lowercase[:]
    upperNew = string.ascii_uppercase[:] + string.ascii_uppercase[:]
    
    
    Dict = {}
    
    for num in range(26):
        Dict[lowerCase[num]] = lowerNew[num + shift]
        
    for num in range(26):
        Dict[upperCase[num]] = upperNew[num + shift]
        
    return Dict
    
    

def applyCoder(text , coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    newTxt = ""
    temp = ""
    for letter in text:
        temp = coder.get(letter, letter)
        # have to use the coder.get() method to get the value just in case it is not in the dictionary
        #the second "letter" is the default value that will be returned in case the 'letter' is not found in the dictionary: in this case, it simply returns that 'letter' unchanged.
        # thus, a comma remains a comma.
        newTxt += temp
    return newTxt

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """

    ### HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift))

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    maxShifts = 0
    validWords = 0
   
    # We will have to apply all 26 possible shifts one at a time.
    
    for shift in range(26):
        tempValidWords = 0
        temp = applyShift(text, shift)[:]

     #After trying a shift, split the string and then test how many of the words are valid.
        for word in temp.split(" "):
        # the problem was here: temp was called, not the split form of temp.    
            if isWord(wordList, word):
                tempValidWords += 1


#check to see if this is the greatest number of valid words: if so, then overwrite the old max number and the old answer.
        if tempValidWords > validWords:
            validWords = tempValidWords
            maxShifts = shift
    return maxShifts

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList = loadWords()
    text = getStoryString()
    bestShift = findBestShift(wordList, text)
    return applyShift(text, bestShift)
    
#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()

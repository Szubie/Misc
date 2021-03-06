word = "honey"
hand = {'a': 3, 'p': 2, 'r': 1, 'u': 2, 't': 1}

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    UpHand = {}
    UpHand = hand.copy()
    
    if word not in wordList:
        return False
    for letter in word:
        if letter not in UpHand:
        #This is what you have to use. "if....not in..." rather than "if _ in _ is not True". Likewise above for the wordList check. Very important to remember this!!!
            return False
        if letter in UpHand:
            if UpHand[letter] == 0:
                return False
            else:
                UpHand[letter] -= 1
            
    return True
    

isValidWord(word, hand, wordList)
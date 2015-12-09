def isWordValid(word, hand, wordList):
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
    

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0

    # Create a new variable to store the best word seen so far (initially None)
    bestWord = None  

    # For each word in the wordList
       
    
    for word in wordList:

        # If you can construct the word from your hand
        if isWordValid(word, hand, wordList):
        
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth
            getWordScore(word, n)

            # If the score for that word is higher than your best score
            if getWordScore>maxScore:
            
                # Update your best score, and best word accordingly
                maxScore = getWordScore(word, n)
                bestWord = word


    # return the best word you found.
    return bestWord
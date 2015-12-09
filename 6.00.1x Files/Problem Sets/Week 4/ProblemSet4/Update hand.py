hand = { 'h': 1, 'e' : 1, 'l': 2, 'o': 1}
word = "hello"


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    UpHand = {}
    UpHand = hand.copy()
    
    #for letter in hand:
        #if letter in word:
         #   UpHand[letter] -= 1
        #the reason this doesn't work is because it only checks to see if the letter is present at all, not how many there are. 
    for letter in word:
        if letter in hand:
            UpHand[letter] -= 1
            
    return UpHand
    
updateHand(hand, word)

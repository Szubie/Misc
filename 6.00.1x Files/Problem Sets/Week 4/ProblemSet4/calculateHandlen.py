hand = {'a':1, 'x':2, 'l':3, 'e':1}

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    ans = 0
    for i in hand:
        ans += hand[i]
    return ans
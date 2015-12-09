def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    n = HAND_SIZE
    handNumber = 0
    hand = {}
    
    while True:
        User = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if User == "e":
            break
        elif User == "r":
            #You need to use "elif" for situations like this, otherwise "invalid command" will always print
            if handNumber == 0:
                print "You have not played a hand yet. Please play a new hand first!"
            else:
                playHand(hand, wordList, n)
        elif User == "n":
            hand = dealHand(n)
            playHand(hand, wordList, n)
            handNumber += 1
     #   elif User == "n":
     #       dealHand(n)
     #       hand = dealHand(n)
     #       playHand(hand, wordList, n)
     #       handNumber += 1
     #       hand = hand
     # The above is a mess, and it caused the grader to mark all as incorrect. much briefer code below.
     
        else:
            print "Invalid command."
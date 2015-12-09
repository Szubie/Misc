from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#

#My addition
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
 #My addition   


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
            wordScore = getWordScore(word, n)
            
            #WHY IS IT NECESSARY TO BIND getWordScore to wordScore? It does seem to solve the problem, but WHY?
            #Was is applying "getWordScore" twice, then?? Unsure.
            #Was is because we bound maxScore to a function, which is variable, rather than to a fixed value below?

            # If the score for that word is higher than your best score
            if wordScore>maxScore:
            
                # Update your best score, and best word accordingly
                maxScore = wordScore
                bestWord = word


    # return the best word you found.
    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    lettersLeft = calculateHandlen(hand)
    totalScore = 0
    compWord = ""

    while lettersLeft>0:
        
     
        # Display the hand
        print "Current hand:",
        str(displayHand(hand))
        print 
        

        # Computer chooses a word:
        compChooseWord(hand, wordList, n)
        if compChooseWord(hand, wordList, n) == None:
            break
        else:
            compWord = compChooseWord(hand, wordList, n)
            totalScore +=  getWordScore(compWord, n)
            print '"{}"'.format(compWord), "earned",  getWordScore(compWord, n) , "points. Total:",totalScore,"points."
            #This is a method of making it print a word surrounded by quotation marks!
            
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            print 
            # Update the hand 
            hand = updateHand(hand, compWord)
            lettersLeft -= len(compWord)

                

    if lettersLeft == 0:
        print "Total score:", totalScore , "points."
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    else:
        print "Total score:", totalScore ,"points."


    
#
# Problem #8: Playing a game
#
#
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
                User2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if User2 != "u" and User2 != "c":
                    while User2 != "u" and User2 != "c" :
                        print "Invalid command." 
                #while User2 == "u" and User2 == "c" is False: (???)
                #THE ABOVE MUST BE "AND" RATHER THAN "OR". VERY IMPORTANT. BOOLEAN OPERATIONS.
                #only continue while BOTH are False: i.e., when 1 AND 2 are both False.                      
                        User2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
                        if User2 == "u":
                            playHand(hand, wordList, n)
                        elif User2 == "c":
                            compPlayHand(hand, wordList, n)
                elif User2 == "u":
                    playHand(hand, wordList, n)
                elif User2 == "c":
                    compPlayHand(hand, wordList, n)




        elif User == "n":
            hand = dealHand(n)
            User2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
            if User2 != "u" and User2 != "c":
                while User2 != "u" and User2 != "c" :
                    print "Invalid command." 

                    #while User2 == "u" and User2 == "c" is False:
                #THE ABOVE MUST BE "AND" RATHER THAN "OR". VERY IMPORTANT. BOOLEAN OPERATIONS.
                #only continue while BOTH are False: i.e., when 1 AND 2 are both False.                      
                    User2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
                    if User2 == "u":
                        playHand(hand, wordList, n)
                        handNumber += 1
                    elif User2 == "c":
                        compPlayHand(hand, wordList, n)
                        handNumber += 1
            elif User2 == "u":
                playHand(hand, wordList, n)
                handNumber += 1
            elif User2 == "c":
                compPlayHand(hand, wordList, n)
                handNumber += 1


        else:
            print "Invalid command."
            

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)



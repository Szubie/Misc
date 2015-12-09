#Unsure what to make. Thinking back to what I did during edX: hangman?

#How about a tic-tac-toe program? Text only, but with a computer opponent.
#Perhaps could work on something that checks the possible outcomes for next turn and selects the best.
#Could implement that first, then allow it to check multiple moves in advance? To truly choose the best move.


#Need to categorise: available moves (remove squares already taken from the equation). (a-c, 1-3)
#                    game-ending condition (win, three in a row. Or board full, draw). (every possible 3 in a row (including diagonals))
#                    a way to make moves (taking user input). A user interface.

#                    Maybe do that first, a game for 2 people. Can work on a computer opponent later.


#How would I do this using Object-Oriented Programming? Uh-oh, can you remember how to OOP?

class Tile(object):
    def __init__(self, other, other2):
        self.tile=other
        self.Tile=other2
    def retrieve(self):
        """returns tile value"""
        return self.tile
    def set(self,argument):
        #This doesn't really work either. Doesn't filter inputs other than X or O. Changed it away from an "if argument == X OR O", works...
        #How does OR work then?? Ah, this works.
        #This is BUGGED, not setting anything. Once again, typo, title
        """sets the tile to the argument provided. Please use only "X" or "O"."""
        if argument == "X" or argument == "O":
            self.tile=argument
    def check(self):
        """checks to see if this tile has been played before, if it is a valid square to play"""
        return self.tile==""
    def reset(self):
        #RESET DOESN'T WORK? Typo: "title, rather than tile". Fixed.
        """sets tile back to original value, perhaps could be used with an Undo feature"""
        self.tile=""
    def name(self):
        """remembers what tile it is"""
        #Why doesn't this work? This is where the BUG is. The reason is probably because you were using the SAME NAME for the method as for the object.
        #So, self.tile was returning the value for tile inside of self, not using this method?
        return self.Tile

#Board
a1=Tile("","a1")
a2=Tile("","a2")
a3=Tile("","a3")
b1=Tile("","b1")
b2=Tile("","b2")
b3=Tile("","b3")
c1=Tile("","c1")
c2=Tile("","c2")
c3=Tile("","c3")

class board(object):
    def __init__(self):
        self.a1=a1
        self.a2=a2
        self.a3=a3
        self.b1=b1
        self.b2=b2
        self.b3=b3
        self.c1=c1
        self.c2=c2
        self.c3=c3
        self.all=[a1, a2, a3, b1, b2, b3, c1, c2, c3]
    def playedMoves(self):
        """returns a list of all moves made. 
        Each item of the list is a tuple, first displaying the tile name, then the value of the tile ("X" or "O")"""
        #Ooof, how do I make it return the tile name? I need to have a method in tile for that.
        List=[]
        for item in [a1, a2, a3, b1, b2, b3, c1, c2, c3]:
            if item.retrieve()!="":
                #List += item     #This adds each letter separately...
                List.append((item.name(), item.retrieve())) 
        return List
    def availableSquares(self):
        """returns a list of all squares that have not been played"""
        List2=[]
        for item in self.all:
            if item.retrieve()=="":
                List2.append(item.name())
        return List2
    def availableSquares2(self):
        """returns a list of all squares that have not been played. The object itself, not a string."""
        List3=[]
        for item in self.all:
            if item.retrieve()=="":
                List3.append(item)
        return List3        
    def returnAll(self):
        return self.all

#Need to substantiate the class.
board=board()

#Player 1 is "O", Player 2 is "X".


#Win condition checker. Is there another way to do this, less copy pasting? Ugh, forgot brackets for method call. Ugly but works.
def winCondition():
    #This is bugged. They are all the same normally, before they are bound.
    #Thus, as soon as a move is played, it declares a winner.
    if a1.retrieve()!="":
        if a1.retrieve() == a2.retrieve() == a3.retrieve():
            if a1.retrieve() == "O":
                print "Player 1 is the winner!"
                return True
            if a1.retrieve() == "X":
                print "Player 2 is the winner!"
                return True
    if b1.retrieve()!="":    
        if b1.retrieve() == b2.retrieve() == b3.retrieve():
            if b1.retrieve() == "O":
                print "Player 1 is the winner!"
                return True
            if b1.retrieve() == "X":
                print "Player 2 is the winner!"
                return True
    if c3.retrieve()!="":
        if c1.retrieve() == c2.retrieve() == c3.retrieve():
            if c1.retrieve() == "O":
                print "Player 1 is the winner!"
                return True
            if c1.retrieve() == "X":
                print "Player 2 is the winner!"
                return True
    if a1.retrieve()!="":
        if a1.retrieve() == b1.retrieve() == c1.retrieve():
            if a1.retrieve() == "O":
                print "Player 1 is the winner!"
                return True
            if a1.retrieve() == "X":
                print "Player 2 is the winner!"
                return True
    if a2.retrieve()!="":
        if a2.retrieve() == b2.retrieve() == c2.retrieve():
            if a2.retrieve() == "O":
                print "Player 1 is the winner!"
                return True
            if a2.retrieve() == "X":
                print "Player 2 is the winner!"
                return True
    if c3.retrieve()!="":
        if a3.retrieve() == b3.retrieve() == c3.retrieve():
            if a3.retrieve() == "O":
                print "Player 1 is the winner!"
                return True
            if a3.retrieve() == "X":
                print "Player 2 is the winner!"
                return True
            
    #diagonal victory
    if b2.retrieve()!="":
        if a1.retrieve() == b2.retrieve() == c3.retrieve():
            if a1.retrieve() == "O":
                print "Player 1 is the winner!"
                return True
            if a1.retrieve() == "X":
                print "Player 2 is the winner!"
                return True
                
    if b2.retrieve()!="":
        if a3.retrieve() == b2.retrieve() == c1.retrieve():
            if a3.retrieve() == "O":
                print "Player 1 is the winner!"
                return True
            if a3.retrieve() == "X":
                print "Player 2 is the winner!"
                return True
    else:
        return False
                            

#A class for players? But what would I do with the players? Dunno.
class player(object):
    def __init__(self, other):
        self.player=other
    def retrieve(self):
        return self.player
    def p1win(self):
        """checks all available moves to see if p1 can win with the next move. Changes the value, tests, then changes it back.
        It returns the name of the winning move. If no move will win the game, returns False."""
        #Since fixing tile.reset(), this no longer works.
        for item in board.availableSquares2():
            item.set("O")
            if winCondition():
                item.reset()
                return item.name()
            else:
                item.reset()
        #If no move will win the game, returns False."
        return False
    def p2win(self):
        """checks all available moves to see if p2 can win with the next move. Changes the value, tests, then changes it back.
        It returns the name of the winning move. If no move will win the game, returns False."""
        for item in board.availableSquares2():
            item.set("X")
            if winCondition():
                item.reset()
                return item.name()
            else:
                item.reset()
        #If no move will win the game, returns False."
        return False            
p1=player(1)
p2=player(2)

class comp(player):
    def __init__(self, other):
        self.player=other

comp=comp(comp)

#Progress report: implemented board and tiles. Also a function to check if win-condition has been met.
#Player class created, not many ideas for it yet though.
#To do next: implement a function that will control the flow of the game.

#Actually, first, maybe implement a turn?
#Turns could probably have been a class...

        
def turn1():
    #First, display played moves.
    print "Played moves:", board.playedMoves()
    #check all available squares.
    print "Available Squares:", board.availableSquares()

    move=raw_input("Player 1 to play. Please choose a square: ")
    
    #Checks for NAME (not value), if it exists, plays it.
    for item in board.returnAll():
        if str(item.name())==str(move):
            item.set("O")
    if item not in board.returnAll():
        print "Invalid move"
        return turn1()

def turn2():
    #First, display played moves.
    print "Played moves:", board.playedMoves()
    #check all available squares.
    print "Available Squares:", board.availableSquares()

    move=raw_input("Player 2 to play. Please choose a square: ")
    
    #Checks for NAME (not value), if it exists, plays it.
    for item in board.returnAll():
        if str(item.name())==str(move):
            item.set("X")
    if item not in board.returnAll():
        print "Invalid move"
        return turn2()
        
#tracks last turn, so it knows who to pass it to next
#Doesn't work! Has to be inside the function.


#Control flow for game.
def main():
    while winCondition()!=True:
        lastTurn=0
        if lastTurn==0 or lastTurn==2:
            lastTurn=1
            turn1()
        #Have to check win condition after every turn.
        if winCondition()==True:
            return winCondition()
        if lastTurn==1:
            lastTurn=2
            turn2()
        if winCondition()==True:
            return winCondition()
            
#Now, how to do implement a computer opponent? This one is a bit more tricky.
#Make it look into the future to make moves that block you?
#Work with it looking one turn into the future, maybe can work from there?

#At this point, it seems pretty hard to allow the players to select noughts or crosses, since it's hard-coded. How would you solve this?

#Should be able to make something that will check if it is possible to win next turn. Checks all available moves. 
#Then what? Try changing it, see if winCondition would trigger, and then change it back? Would that work?
#Put this method in Player class, and make computer a sub-class of that?


#We have the beginnings of something that will check to see whether a victory is possible next turn. However, it always
#prints out a victory statement, and that needs to change. Will be difficult to alter.

#Then, we need to provide the framework for the computer to start making use of this method.
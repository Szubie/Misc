import Sudoku_board
import Sudoku_eliminationTest
import Sudoku_view
import Sudoku_validCheck
import Sudoku_main
import timeit

""" A Backtracking program  in Python. to solve Sudoku problem"""


"""Creating scenario"""
Sudoku_main.createScenario3()  #TEMP
 
# UNASSIGNED is used for empty cells in sudoku grid
UNASSIGNED=0
 
# N is used for size of Sudoku grid. Size will be NxN
N=9
 

def findUnassignedLocation(tileList):
    """This function finds an entry in grid that is still unassigned. 
        Returns Boolean false if it can't find an unassigned item. Otherwise, returns item."""
    for item in Sudoku_board.board.tileList():
        if item.value()==-1:
            return item
    else:
        return False
    
# Checks whether it will be legal to assign num to the given tile
def isValid(tile, num):
    """Checks whether it will be legal to assign num to the given tile. NOTE: this function doesn't check whether the item is unassigned. Please don't call this on already assigned tiles, or it will overwrite them."""
    col=Sudoku_board.board.columnList()[tile.col()-1]
    row=Sudoku_board.board.rowList()[tile.row()-1]
    square=Sudoku_board.board.squareList()[tile.square()-1]
    
    if not (col.valueExists(num) or row.valueExists(num) or square.valueExists(num)):
        return True
    else:
        return False


#start_time = timeit.default_timer()
Sudoku_validCheck.validChecker(Sudoku_board.board.tileList())

def solveSudoku(tileList):
    """ Takes a partially filled-in grid and attempts to assign values to
    all unassigned locations in such a way to meet the requirements
    for Sudoku solution (non-duplication across rows, columns, and boxes) """

    index=findUnassignedLocation(tileList)
#    print index.name()
 
    # If there is no unassigned location, we are done
    if (findUnassignedLocation(tileList)==False):
       Sudoku_view.view()
       return True # success!
 
    # consider digits 1 to 9
    for num in index.validValues():
        if (isValid(index,num)):
            index.setValue(num)
            if solveSudoku(tileList):
                return True
            index.setValue(-1)
    return False # this triggers backtracking

#solveSudoku(Sudoku_board.board.tileList())
#elapsed = timeit.default_timer() - start_time

#print elapsed
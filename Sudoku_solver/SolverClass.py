import Sudoku_board
import Sudoku_view
import Sudoku_validCheck
import Sudoku_main

""" A Backtracking program  in Python to solve Sudoku problem"""
 
class Sudoku_solver(object):
    def __init__(self):
        self
    
    def findUnassignedLocation(self,tileList):
        """This function finds an entry in grid that is still unassigned. 
            Returns Boolean false if it can't find an unassigned item. Otherwise, returns item."""
        for item in Sudoku_board.board.tileList():
            if item.value()==-1:
                return item
        else:
            return False
    
    def isValid(self,tile, num):
        """Checks whether it will be legal to assign num to the given tile. 
        NOTE: this function doesn't check whether the item is unassigned. Don't call this on already assigned tiles, or it will overwrite them."""
        col=Sudoku_board.board.columnList()[tile.col()-1]
        row=Sudoku_board.board.rowList()[tile.row()-1]
        square=Sudoku_board.board.squareList()[tile.square()-1]
        
        if not (col.valueExists(num) or row.valueExists(num) or square.valueExists(num)):
            return True
        else:
            return False




    def solveSudoku(self,tileList):
        """ Takes a partially filled-in grid and attempts to assign values to
        all unassigned locations in such a way to meet the requirements
        for Sudoku solution (non-duplication across rows, columns, and boxes) """
        Sudoku_validCheck.validChecker(Sudoku_board.board.tileList())
    
        index=self.findUnassignedLocation(tileList)
    
        # If there is no unassigned location, we are done
        if (self.findUnassignedLocation(tileList)==False):
            Sudoku_view.view()
            return True # success!
 
        # consider valid digits
        for num in index.validValues():
            if (self.isValid(index,num)):
                index.setValue(num)
                if self.solveSudoku(tileList):
                    return True
                index.setValue(-1)
        return False # this triggers backtracking

solveSudoku=Sudoku_solver()
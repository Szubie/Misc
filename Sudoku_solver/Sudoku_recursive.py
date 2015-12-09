import Sudoku_board
import Sudoku_eliminationTest
import Sudoku_view
import Sudoku_validCheck
import Sudoku_main

""" A Backtracking program  in C++ to solve Sudoku problem"""

 
# UNASSIGNED is used for empty cells in sudoku grid
UNASSIGNED=0
 
# N is used for size of Sudoku grid. Size will be NxN
N=9
 

def FindUnassignedLocation(grid, row, col):
    """This function finds an entry in grid that is still unassigned. 
        Returns Boolean."""
    return
    
    
# Checks whether it will be legal to assign num to the given row,col
def isSafe(grid, row, col, num):
    return
 

def SolveSudoku(grid, row, col):
    """ Takes a partially filled-in grid and attempts to assign values to
    all unassigned locations in such a way to meet the requirements
    for Sudoku solution (non-duplication across rows, columns, and boxes) """

    row, col;
 
    # If there is no unassigned location, we are done
    if (not FindUnassignedLocation(grid, row, col)):
       return true; # success!
 
    # consider digits 1 to 9
    for num in range(1,10):
    
        #if looks promising
        if (isSafe(grid, row, col, num)):
            # make tentative assignment
            grid[row][col] = num;
 
            # return, if success, yay!
            if (SolveSudoku(grid)):
                return true
 
            # failure, unmake & try again
            grid[row][col] = UNASSIGNED;
        
    
    return false; # this triggers backtracking

 

def FindUnassignedLocation(grid, row, col):
    """ Searches the grid to find an entry that is still unassigned. If
   found, the reference parameters row, col will be set the location
   that is unassigned, and true is returned. If no unassigned entries
   remain, false is returned. """
    for row in range(N):
        for col in range(N):
            if (grid[row][col] == UNASSIGNED):
                return true;
    return false;

 

def UsedInRow(int grid[N][N], int row, int num):
    """ Returns a boolean which indicates whether any assigned entry
   in the specified row matches the given number. """
    for (int col = 0; col < N; col++)
        if (grid[row][col] == num)
            return true;
    return false;
}
 

def UsedInCol(int grid[N][N], int col, int num)
    """ Returns a boolean which indicates whether any assigned entry
   in the specified column matches the given number."""
    for (int row = 0; row < N; row++)
        if (grid[row][col] == num)
            return true;
    return false;

 

def UsedInBox(int grid[N][N], int boxStartRow, int boxStartCol, int num)
   """ Returns a boolean which indicates whether any assigned entry
   within the specified 3x3 box matches the given number. """
    for (int row = 0; row < 3; row++)
        for (int col = 0; col < 3; col++)
            if (grid[row+boxStartRow][col+boxStartCol] == num)
                return true;
    return false;
}


def isSafe(int grid[N][N], int row, int col, int num):
    """ Returns a boolean which indicates whether it will be legal to assign
   num to the given row,col location. """
    # Check if 'num' is not already placed in current row,
    # current column and current 3x3 box 
    return !UsedInRow(grid, row, num) &&
           !UsedInCol(grid, col, num) &&
           !UsedInBox(grid, row - row%3 , col - col%3, num);

 

def printGrid(int grid[N][N])
    """ A utility function to print grid  """
    for (int row = 0; row < N; row++)
    {
       for (int col = 0; col < N; col++)
             printf("%2d", grid[row][col]);
        printf("\n");
    }
}
 

def main():
    """ Driver Program to test above functions """

    # 0 means unassigned cells
    grid[N][N] =     {{3, 0, 6, 5, 0, 8, 4, 0, 0},
                      {5, 2, 0, 0, 0, 0, 0, 0, 0},
                      {0, 8, 7, 0, 0, 0, 0, 3, 1},
                      {0, 0, 3, 0, 1, 0, 0, 8, 0},
                      {9, 0, 0, 8, 6, 3, 0, 0, 5},
                      {0, 5, 0, 0, 9, 0, 6, 0, 0},
                      {1, 3, 0, 0, 0, 0, 2, 5, 0},
                      {0, 0, 0, 0, 0, 0, 0, 7, 4},
                      {0, 0, 5, 2, 0, 6, 3, 0, 0}};
    if (SolveSudoku(grid) == true)
          printGrid(grid)
    else
         print "No solution exists"
 
    return 0
}
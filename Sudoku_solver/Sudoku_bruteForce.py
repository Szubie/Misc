import Sudoku_board
import Sudoku_validCheck
import Sudoku_view
import Sudoku_main

Sudoku_main.createScenario1()
Sudoku_validCheck.validCheck(Sudoku_board.board.tileList())

def recursive(n=0):
    validNums=[1,2,3,4,5,6,7,8,9]
    for j in range(n,len(Sudoku_board.board.tileList())):
        for num in validNums:
            if num in Sudoku_board.board.tileList()[j].validValues():
                Sudoku_board.board.tileList()[j].setValue(num)
                Sudoku_validCheck.validChecker(Sudoku_board.board.tileList())
                recursive(n=n+1)
                print n   #How to backtrack?
        print n
        Sudoku_view.view()
    
    if n==len(Sudoku_board.board.tileList())-1 and num in Sudoku_board.board.tileList()[n].validValues():
        Sudoku_board.board.tileList()[n].setValue(num)
        Sudoku_view.view()
        return True
        
    if n==len(Sudoku_board.board.tileList())-1 and num not in Sudoku_board.board.tileList()[n].validValues():
        return False
        

import Sudoku_main
import Sudoku_board
import Sudoku_validCheck
import Sudoku_eliminationTest
import Sudoku_view

Sudoku_main.createScenario1()

def attempt():
    validNums=[1,2,3,4,5,6,7,8,9]
    Sudoku_validCheck.validCheck(Sudoku_board.board.tileList())
    Sudoku_eliminationTest.elimination(Sudoku_board.board.tileList()[0])
    for item in Sudoku_board.board.tileList():
        if item.value()==-1:
            print item.name()
            col=Sudoku_board.board.columnList()[item.col()-1]
            row=Sudoku_board.board.rowList()[item.row()-1]
            square=Sudoku_board.board.squareList()[item.square()-1]
            for num in validNums:
                if not (col.valueExists(num) or row.valueExists(num) or square.valueExists(num)): #But how to backtrack here...?
                    item.setValue(num)
                    Sudoku_validCheck.validCheck(Sudoku_board.board.tileList())
                    Sudoku_eliminationTest.elimination(item)
                else:
                    continue
            

    return "Done"
    

#If you've checked all possible numbers for the last case and it isn't true, reject this solution.
def attempt2(iteration, validNumbers=[1,2,3,4,5,6,7,8,9], keyMax=9):
    Sudoku_validCheck.validCheck(Sudoku_board.board.tileList())
    Sudoku_eliminationTest.elimination(Sudoku_board.board.tileList()[0])
    
    keyMax
    key=0
    iteration=0
    
    while iteration<len(Sudoku_board.board.tileList()):
        col=Sudoku_board.board.columnList()[Sudoku_board.board.tileList()[iteration].col()-1]
        row=Sudoku_board.board.rowList()[Sudoku_board.board.tileList()[iteration].row()-1]
        square=Sudoku_board.board.squareList()[Sudoku_board.board.tileList()[iteration].square()-1]
        while key<keyMax:
            if key==keyMax:
                if not (col.valueExists(validNumbers[key-1]) or row.valueExists(validNumbers[key-1]) or square.valueExists(validNumbers[key-1])):
                    Sudoku_board.board.tileList()[iteration].setValue(validNumbers[key])
                    Sudoku_validCheck.validCheck(Sudoku_board.board.tileList())
                    Sudoku_eliminationTest.elimination(Sudoku_board.board.tileList()[iteration])
                    return attempt2(iteration+1)
                else:
                    return attempt2(iteration-1,validNumbers[1:0],keyMax=keyMax-1)
            else:
                if not (col.valueExists(validNumbers[key-1]) or row.valueExists(validNumbers[key-1]) or square.valueExists(validNumbers[key-1])):
                    Sudoku_board.board.tileList()[iteration].setValue(validNumbers[key])
                    Sudoku_validCheck.validCheck(Sudoku_board.board.tileList())
                    Sudoku_eliminationTest.elimination(Sudoku_board.board.tileList()[iteration])
                    return attempt2(iteration+1)
                key+=1
        iteration+=1
                
    
def attempt3():
    Sudoku_validCheck.validCheck(Sudoku_board.board.tileList())
    Sudoku_eliminationTest.elimination(Sudoku_board.board.tileList()[0])
        
    for item in Sudoku_board.board.tileList():
        col=Sudoku_board.board.columnList()[item.col()-1]
        row=Sudoku_board.board.rowList()[item.row()-1]
        square=Sudoku_board.board.squareList()[item.square()-1]
        for num in item.validValues():
            if not (col.valueExists(num) or row.valueExists(num) or square.valueExists(num)):
                item.setValue(num)
                Sudoku_validCheck.validCheck(Sudoku_board.board.tileList())
                Sudoku_eliminationTest.elimination(Sudoku_board.board.tileList()[item])
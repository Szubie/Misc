"""I can think of a brute force back-tracking algorithm that will check all valid numbers for every square...Horrifically inefficient, but possible."""
#How exactly to implement, though? 81 nested for loops sounds ridiculous...
#Recursion?
import operator

import Sudoku_board
import Sudoku_main
import Sudoku_eliminationTest
import Sudoku_view
import Sudoku_validCheck

Sudoku_main.createScenario3()
Sudoku_validCheck.validCheck(Sudoku_board.board.tileList())

tileList = Sudoku_board.board.tileList()
    
def merge(left, right, compare):
    result=[]
    i , j = 0 , 0    
    while i<len(left) and j<len(right):
        if compare(len(left[i].validValues()), len(right[j].validValues())):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while (i<len(left)):
        result.append(left[i])
        i+=1
    while (j<len(right)):
        result.append(right[j])
        j+=1
    return result
    
def mergeSort(L, compare=operator.lt):
    """sortBySmallestValidValues"""
    if len(L)<2:
        return L[:]
    else:
        middle=int(len(L)/2)
        left=mergeSort(L[:middle] , compare)
        right=mergeSort(L[middle:], compare)
        return merge(left, right, compare)

sortedList=mergeSort(tileList, operator.lt)

def stripEmptyInList(aList):
    output=[]
    for item in aList:
        if len(item.validValues())!=0:
            output.append(item)
    return output
    
strippedList=stripEmptyInList(sortedList)

for thing in strippedList:
    print thing.name(), thing.validValues()

def backtrack(strippedList):
    Sudoku_validCheck.validCheck(Sudoku_board.board.tileList())
    for tile in sortedList:
        for validValue in tile.validValues():
            tile.setValue(validValue)
            Sudoku_validCheck.validCheck((Sudoku_board.board.tileList())) #Keep things up to date here...
            Sudoku_main.main()
            if Sudoku_main.isComplete()==True:
                return 
            else:
                Sudoku_main.reset()
                Sudoku_main.createScenario3() #Ah, this solves the mystery
                Sudoku_view.view()
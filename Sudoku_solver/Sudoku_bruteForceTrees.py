import Sudoku_board
import Sudoku_validCheck
import Sudoku_view
import Sudoku_main

#Need to look at trees.

Sudoku_main.createScenario1()
Sudoku_validCheck.validCheck(Sudoku_board.board.tileList())
"""
def recursive(n=0):
    toSearch=[1,2,3,4,5,6,7,8,9]
    key=0
    
    if n==len(Sudoku_board.board.tileList())-1 and toSearch[key] in Sudoku_board.board.tileList()[n].validValues():
        Sudoku_board.board.tileList()[n].setValue(toSearch[key])
        Sudoku_view.view()
        return True
        
    if n==len(Sudoku_board.board.tileList())-1 and toSearch[key] not in Sudoku_board.board.tileList()[n].validValues():
        return False
"""        

#Need to create the tree first. Algorithms to do that. 

def constructTree():
    validNums=[1,2,3,4,5,6,7,8,9]
    BinaryTree=binaryTree(Sudoku_board.board.tileList()[0])
    for thing in Sudoku_board.board.tileList()[1:]:
        for item in validNums:
            if item==1:
                
        
    
              
class binaryTree(object):
    
    def __init__(self, value):
        self.value = value
        self.firstBranch = None
        self.secondBranch = None
        self.thirdBranch = None
        self.fourthBranch = None
        self.fifthBranch = None
        self.sixthBranch = None
        self.seventhBranch = None
        self.eighthBranch = None
        self.ninthBranch = None
        
        self.setBranchList= [
            self.firstBranch,
            self.secondBranch,
            self.thirdBranch,
            self.fourthBranch,
            self.fifthBranch,
            self.sixthBranch,
            self.seventhBranch,
            self.eighthBranch,
            self.ninthBranch] 
                   
        self.parent = None
        

        
    def setFirstBranch(self, node):
        self.firstBranch = node
    def setSecondBranch(self, node):
        self.secondBranch = node
    def setThirdBranch(self, node):
        self.thidBranch = node
    def setFourthBranch(self, node):
        self.fourthBranch = node
    def setFifthBranch(self, node):
        self.fifthBranch = node
    def setSixthBranch(self, node):
        self.sixthBranch = node
    def setSeventhBranch(self, node):
        self.seventhBranch = node
    def setEighthBranch(self, node):
        self.eighthBranch = node
    def setNinthBranch(self, node):
        self.ninthBranch = node     
    def setParent(self, parent):
        self.parent = parent
        

    def getValue(self):
        return self.value
    def getFirstBranch(self):
        return self.firstBranch
    def getSecondBranch(self):
        return self.secondBranch
    def getThirdBranch(self):
        return self.thidBranch
    def getFourthBranch(self):
        return self.fourthBranch
    def getFifthBranch(self):
        return self.fifthBranch
    def getSixthBranch(self):
        return self.sixthBranch
    def getSeventhBranch(self):
        return self.seventhBranch
    def getEighthBranch(self):
        return self.eigthBranch
    def getNinthBranch(self):
        return self.ninthBranch

    def getParent(self):
        return self.parent
    def __str__(self):
        return self.value
    
def DFSBinary(root, fcn):
    queue = [root]
    while len(queue) > 0:
        print 'at node ' + str(queue[0].getValue())
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            if temp.getRightBranch():
                queue.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                queue.insert(0, temp.getLeftBranch())
    return False

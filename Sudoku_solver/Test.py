import Sudoku_board

invalidValues=[1, 4, 5, 8]
invalid2=Sudoku_board.b9.invalidValues()
print invalid2
TileList=[Sudoku_board.b7]



for tile in TileList:
    print tile.name()
    print "Invalid values: ", invalidValues
    print "Base invalid values:", invalid2
    for thing in invalidValues:
        if thing not in invalid2:
            invalidValues.remove(thing)
            print "Current invalid values list: "
            print invalidValues
        elif thing==tile.value():
            invalidValues.remove(thing)
            print "Current invalid values list: "
            print invalidValues
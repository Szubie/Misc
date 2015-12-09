#Multidimensional lists.


"""
x_col=[-1,-1,-1,-1,-1,-1,-1,-1,-1]
x_axis=[x_col]*9

y_row=[-1,-1,-1,-1,-1,-1,-1,-1,-1]
y_axis=[y_row]*9

board=[x_axis, y_axis]

#board[0][8]=8
"""

"""
board=[]

board.append([])
board.append([])

board[0].append(1)
board[0].append(2)

board[1].append(3)
board[1].append(4)

print board[0][0]

# Display entire list.
print board
    
for row in board:
    # Loop over columns.
    for column in row:
        print column,
    print
"""

"""
board=[]
for x_axis in range(9):
    board.append([])

for x_axis in range(9):
    for n in range(9):
        board[x_axis].append([-1])
    
"""

board=[]

#def sizeOfBoard():
#    n=raw_input("How big should the board be? \n")
    
for x_axis in range(9):
    board.append([])
    
for x_axis in range(9):
    for n in range(9):
        board[x_axis].append(-1)
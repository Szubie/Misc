from __future__ import print_function

s="00000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000"
#s="1101010"

def array(x):
    """Takes in a string of numbers (0 or 1), creates a boolean array out of them. Tacks on "ghost" values False at both the start and the end."""
    new_list=[False]
    for item in s:
        if item == "1":
            new_list.append(True)
        if item == "0":
            new_list.append(False)
    new_list.append(False)
    return new_list
    
def read_list(x):
    """Takes in a boolean array, prints it out as a line. Ignores the ghost values on either end of the list."""
    for n in range(1, len(x)-1):
        if x[n] == True:
            print("x", end="")
        elif x[n] == False:
            print(" ", end="")
    print("") #Ends by starting a new line.

def next_list(x):
    """Takes in the previous list (an array of Booleans), and uses it to calculate the next list."""
    new_list=[False]                     #Also must output a list complete with the False ghost values tacked onto both ends (but ignoring them).
    for n in range(1, len(x)-1):
        if x[n-1]==x[n+1]:
            new_list.append(False)
        elif x[n-1]!=x[n+1]:
            new_list.append(True)
    new_list.append(False)
    return new_list                     #Since the function is built to deal with lists with ghost values tacked on, we should tack them back on in the output. Then we can continue to re-use the function.    
    
def main(x):
    y=array(x)
    read_list(y)
    for n in range(25):
        y=next_list(y)
        read_list(y)
        
main(s)
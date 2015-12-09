import sys

s="00000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000"
#s="1101010"

def array(x):
    """Takes in the string of numbers and creates an array of boolean values from them."""
    x=str(x)
    prev_list=[False]              #Every new list that comes through here will have a False tacked onto the start and end.  HOWEVER, this is only called once.
    for item in x:
        if item == "0":
            prev_list.append(False)
        if item == "1":
            prev_list.append(True)
    prev_list.append(False)         #The list ends with a False, as well as starts with one.
    return prev_list
    
    
def readLine(x):
    """Takes as input the list of booleans. Reads the line, prints the x's and spaces."""
#    x=str(x) #Make sure the input is a string. No longer required, change of plans.
    for n in range(1, len(x)-1):    #Needed to alter this so that it only printed the values in between, not the whole thing (including the "ghost values" you tack onto the ends).
        if x[n]==False:   #These conditionals might change?
            sys.stdout.write(" ")
        elif x[n]==True:
            sys.stdout.write("x")

def next_list(x):
    """Takes in the list of booleans to calculate the next list"""
    new_list=[False]                   #Please keep in mind what exactly you are altering. new_list or x.
    #First, tackle the old list. Add it onto the new_list base.
#    x.insert(0,False)           #Inserting these is now unnecessary, since we already have a full list with them tacked on? Just don't change them, and they'll stay there?
            
    for n in range(1,len(x)-1):
        if x[n-1]==x[n+1]:
            new_list.append(False)
        elif x[n-1]!=x[n+1]:
            new_list.append(True)
    new_list.append(False)
#    new_list.append(False)        #Every new list that comes through here will have a False tacked onto the start and end.   Remember to use () round brackets, not square ones...
#    if x[-1]==x[-3]:                   #Dealing with the last number. Need to treat it differently. Calculate what it's going to be by adding a False onto the end, and then insert the result into the list in the correct place.
#        new_list.insert(-2,False)
#    elif x[-1]!=x[-3]:
#        new_list.insert(-2,True)          #Inputting False on either branch of the logic tree...
#    for n in range(1, len(x)-1):          #However, when returned, it drops them.
#        new_list2.append(new_list[n])
    return new_list

def main(x):
    """Controls other functions"""
    y=array(x)
    readLine(y)
    print ""
    for n in range(24):
        y=next_list(y)
        readLine(y)
        print ""
        

#Eeek, that was still quite a mess indeed...
#Made a ton of errors, especially in the next_list function. Ranging from altering the input (instead of the list that we would ultimately be outputting), unsure if using new_list ([False]) or original input.
#Dealing with the edge cases: this time, I simply altered the original input by inserting values at the start and end of the list.


#This actually still doesn't work...
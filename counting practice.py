
def count(x):
    """counts up from 0 to x, while printing values from x to 0."""
    y=0 # This is the counting up part. (Wait, recursively calling this will constantly reset y to 0).
    while x>=0:
        print x
        y+=1
        x-=1
    return y, x #Interestingly, this returns "101" as the value for y, not 100. In fact, I suppose the real value for x will be -1 right now, but it is not the value printed. Yep.
    
    #What would you do if you wanted to change this behaviour?
    
    
#Also, it is probably possible to do this recursively by defining y in the variables defined when the function is called.

def count2(x,y):
    """define y as 0"""
    if x==0:
        print x
        return y
    print x
    return count2(x-1, y+1)
    
#So THAT'S how you do recursion! 


#Additionally, the extra unecessary loop has been cut in this function.
#How would you cut that extra loop in an iterative solution?

def count3(x, y):
    print x #Start off with the number you're beginning at, then enter the loop. (Is this optimal?)
    while x>=1: #whoops, with this construction x, we must stop earlier than "x>=0"
        x-=1
        y+=1    #wow, that's a huge typo that ruins the results. "y=+1" binds y to 1 every time. "y+=1" increases y by 1 each time. CAREFUL.
        print x
    return y
        
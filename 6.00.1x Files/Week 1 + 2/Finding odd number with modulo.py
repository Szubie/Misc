#Looking for odd numbers. True is odd, False otherwise.

#You should use the % (mod) operator, not if. (modulo operator yields the remainder from the division).
#YOU CANNOT USE "if" keyword.

def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    x = x%2
    if x==0:
        print "even"
    else:
        print "odd"

#Answer is not in Boolean form, and the strings printed out are not a useful return. Works at least.

def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    y = x%2
    if y!=0:
        return True
    else:
        return False
    #remember, != is "is not equal to"
    #removed " " around true and false: now it can recognise it as a Boleean response.
    
#Whoops, can't use "if"!    

def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    y = x%2
    return y!=0
    
#Cut out unnecessary bits.
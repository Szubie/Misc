def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1
#    if exp == 1:
#        return base
#above is not true in this function.
    elif exp%2 == 0:
        return base * base * recurPowerNew (base, exp/2)   
    elif exp%2 != 0:
        return base * recurPowerNew (base, exp-1)
#the above doesn't work.
 #       return base * base * recurPowerNew (base, exp/2)
 #wrong
#return (base**2)**(exp/2), pre-simplification, another way of writing it is above.

# exp may start as even, but become odd after being halved: then the other side of the equation must take over.
#Likewise, odd becomes even after 1 is subtracted from it.
#this function does not operate in two halves, they need each other.

#Couldn't do it, gave up, answer stored in another doc.
# want to multiply base by itself exp times.Cannot use ** or loops.

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    
#First, what is the base case? if exp = 0, then the answer is 1. (If exp = 1, the answer is base)
#Now need to think of a recursive step. Simplify the problem, and in a way that it reduces the value of exp each time.
# recurPower = base * base * base (exp times)
#    recurPower        = base * recurPower(base, exp -1)

    if exp == 0:
        return 1
    elif exp ==1:
        return base
        #actually the above line is unecessary, as the below returns the correct value for exp=1
    else:
        return base * recurPower (base, exp-1)
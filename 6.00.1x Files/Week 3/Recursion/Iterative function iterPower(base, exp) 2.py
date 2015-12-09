def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    #define result internally first, but not inside the loop.
    while exp > 0:
        result = result * base
        exp -= 1
    return result
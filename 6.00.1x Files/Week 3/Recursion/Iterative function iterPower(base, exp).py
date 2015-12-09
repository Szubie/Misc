#multiply base to itself exp times

#def iterPower(base, exp):
 #   '''
  #  base: int or float.
   # exp: int >= 0
 
    #returns: int or float, base^exp
#    '''
#    result = 0
#    #define result internally first, but not inside the loop.
#    while exp > 0:
#        result = base * base
#        exp -= 1
#    return result
    
#the above is wrong because result is not changing: it returns base * base every time.

#def iterPower(base, exp):
#    '''
#    base: int or float.
#    exp: int >= 0
# 
#    returns: int or float, base^exp
#    '''
#    result = base
#    #define result internally first, but not inside the loop.
#    while exp > 0:
#        result = result * base
#        exp -= 1
#    return result
    
#the above is also wrong, multiplying the number by itself 1 too many times.

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = base
    #define result internally first, but not inside the loop.
    while exp > 1:
        result = result * base
        exp -= 1
    return result
    
#THE ABOVE WORKS BUT ONLY FOR POWERS GREATER THAN 0 (which should return the answer of "1".
#solved by changing result to "1", and adjusting the "while" loop to stop before 0 again (instead of "1").
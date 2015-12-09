def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    ans = 0
    temp = b

    
    while temp <= x:
        temp = temp*b 
        ans += 1
    return ans

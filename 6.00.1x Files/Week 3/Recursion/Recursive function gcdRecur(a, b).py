#    If b = 0, then the answer is a
#    Otherwise, gcd(a, b) is the same as gcd(b, a % b)
#    Euclid's algorithm being used to find the gcd.

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b==0:
        return a
    else:
        return gcdRecur (b, a % b)

#WOW, it works!
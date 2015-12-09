#Searching for the largest common divisor of two positive integers.
#Will start from the lower of the two integers and count downwards by 1 until I reach the answer.

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    x= min(a, b)
    while a % x != 0 or b % x !=0:
#My first choice of key word here, "and", doesn't work: it simply outputs the smallest value of a or b in the end.
#For some reason, "or" works though.
        x = x - 1
    return x
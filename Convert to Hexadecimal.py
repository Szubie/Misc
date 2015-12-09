# -*- coding: utf-8 -*-
"""Division-remainder in source base[edit]
As with all bases there is a simple algorithm for converting a representation of a number to hexadecimal by doing integer division and remainder operations in the source base. In theory, this is possible from any base, but for most humans only decimal and for most computers only binary (which can be converted by far more efficient methods) can be easily handled with this method.

Let d be the number to represent in hexadecimal, and the series hihi−1...h2h1 be the hexadecimal digits representing the number.

i ← 1
hi ← d mod 16
d ← (d − hi) / 16
If d = 0 (return series hi) else increment i and go to step 2
"16" may be replaced with any other base that may be desired.

The following is a (JavaScript) Python implementation of the above algorithm for converting any number to a hexadecimal in String representation. Its purpose is to illustrate the above algorithm. To work with data seriously, however, it is much more advisable to work with bitwise operators."""


def toChar(n):
    alpha="0123456789ABCDEF"
    return alpha[n]

def toHex(d):
    r=d%16
    result=0
    if d-r==0:
        result=toChar(r)
    else:
        result=toHex( (d-r)/16) + toChar(r)
    return result
    

#The above can also be written in a shorter version, as it is below.     
def toHex2(d):
    r=d%16
    if d-r==0:
        return toChar(r)
    else:
        return toHex( (d-r)/16) + toChar(r)
    

#Below is the implementation for converting to binary:
#The divisions by 16 are replaced by divisions by 2, and the set of available charcters reduced to 0s and 1s.
#Of course, all the "toChar" functions are changed, as is the recursive call to "toBinary"!

def toChar2(n):
    alpha2="01"#23456789ABCDEF"
    return alpha2[n]

def toBinary(d):
    r=d%2
    result=0
    if d-r==0:
        result=toChar2(r)
    else:
        result=toBinary( (d-r)/2) + toChar2(r)
    return result
    

#To base 10 conversion below:
#Actually, no, you're missing the point. This will simply return the same value as put in (assumes the value put in is in base 10, and then outputs the same value.
#The nature of numbers: the rightmost one is the remainder when the whole is divided by 10 as many times as possible.
#Then, disregarding that reminader, the next column is the remainder of the rest of the value when divided by 10.

def toChar3(n):
    alpha2="0123456789"#ABCDEF"
    return alpha2[n]

def toDecimal(d):
    r=d%10
    result=0
    if d-r==0:
        result=toChar3(r)
    else:
        result=toDecimal( (d-r)/10) + toChar3(r)
    return result
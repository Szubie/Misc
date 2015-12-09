
# ** is the operator for "to the power of" in python.

#So we want to convert the number into a string, take the length of the string, then convert each value back into an integer, multiply it by a power of 16 and add it to the total.

def hex2dec(x, power=-1):
    x=str(x)
    l=len(x)
    power+=1
    if l==1:
        return int(x)*(16**power)
    else:
        y=int(x[-1])
        return hex2dec(x[:-1], power)  + (y*(16**power))  #This is how string slicing works in Python! [:-1]
        
#Now that's a neat little trick to remember. Using default values, and then incrementing them within a recursive call of the function.


def binary2dec(x, power=-1):
    x=str(x)
    l=len(x)
    power+=1
    if l==1:
        return int(x)*(2**power)
    else:
        y=int(x[-1])
        return binary2dec(x[:-1], power)  + (y*(2**power))
        
#binary2dec(1010011010)

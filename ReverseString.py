
def reverseString(x):
    if len(x)==1 or len(x)==0:
        return x
    x[0]=x[-1], x[-1]=x[0] #This line causes the error, since "str" object doesn't support item assignment
    return reverseString(x[range(1, -2)])
    
    
"""In Python, strings are immutable, so you can't change their characters in-place.""" #Plus, I think this doesn't work anyway

"""You can, however, do the following:

for i in str:
    srr += i

The reasons this works is that it's a shortcut for:

for i in str:
    srr = srr + i

The above creates a new string with each iteration, and stores the reference to that new string in srr."""


def reverseString2(x):
    if len(x)==1 or len(x)==0:
        return x
    return x[-1] + reverseString2(x[:-1]) #This works because it isn't trying to change an immutable string, just returning elements of the string.
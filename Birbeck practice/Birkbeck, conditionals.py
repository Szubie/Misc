# -*- coding: utf-8 -*-
x=raw_input("Husband's salary:")
y=raw_input("Wife's salary:")
#
#if x+y>40000:
#    print "You have gone over the limit of £40,000 and have to pay more tax"


#Above works fine. Now to do it as a function.

def addAndCheck(x, y):
    """Takes as input husband's salary, and wife's, respectively. Returns text which explains whether the combined income limit has been reached."""
    if int(x)+int(y)>40000:
        print "Your combined income has made you liable to pay a higher tax rate, as it exceeds £40,000"
    else:
        print "Your combined income is below £40,000 and thus you do not need to pay a higher tax rate."
    
#Bugged! Because the raw input takes the user input and remembers it AS A STRING. Need to convert it into an int!
s=raw_input ("Input a number")

print s

str=str(s)

#for str[num] in range(1, len(str)-1):          Find a different way to implement this. This doesn't work syntatictically.
#    print num


#for num in range (1,len(str)-1):                         #string indices must be integers, not str 
#    print num                                           #Whoops, this just prints the numbers inside the range...
        
        
#'long' object is not iterable . You must convert it into a str if you want to do this!

for num in range(1, len(str)-1):
    print str[num]
    
#Wow, that just completely didn't work...what happened?

"""Global frame
s	2.2300745198530623e+43
str	"22300745198530623141535718272648361505980416"


s
Out[14]: 22300745198530623141535718272648361505980416L
"""

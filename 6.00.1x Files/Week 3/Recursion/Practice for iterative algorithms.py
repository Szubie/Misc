
#Using loops, run through the computation in succession, each time altering the values used.
#Loops: "for" or a "while" loop.

#Doing multiplication by adding a number to itself multiple times.

#Must track TWO THINGS: the iteration number
#and also the result. THE RESULT SHOULD START AT 0.

#(i=0
#this is the iteration number
#result=0
#tracks the final answer
#) This was not ultimately used. Unnecessary.


#x= 10
#y= 12
#result = 0

#the variables that change. (result should start at 0!)

#while i!=0:
 #   result = x+x
  #  print "result = "
   # print result
    #y = y-1

#above is wrong, only gets 20 repeatedly. i never changes, and when changed to y, x never does.

#while y!=0:
 #   x = x+x
  #  print "result = "
   # print x
    #y = y-1

#this also is wrong, as it is adding inflated values of x to itself. Need to track another variable: must keep the original x intact.

#while y!=0:
 #   result += x
  #  print "result = "
   # print result
    #y = y-1
#above adds it once too many times. changed "result= x" to "result=0". Now correct.

#while y>0:
 #   result += x
  #  print "result = "
   # print result
    #y = y-1
    
#must have something that ticks down and will end the process at the right time. 
#updates the rules each time until it reaches that point.

#upside to an iterative computation: if you stop the process at any time you will know where you are at that point.


#NOW TO DO IT AS A FUNCTION.

#def iterMul (x, y):
 #   """
  #  #this text should be shown to the end user to inform them of what they need to input in order to get the desired result.
   # """
    #result =0 
    ##internally defines "result" for inside this function only.
#    while y>0:
#        result += x
#        print "result = "
#        print result
#        y -= 1
#        return result
        #have to remember to use "return" with a function.
        
# x and y are abstract, not defined in the function. Define them when you call the function.

#the above DOESN'T WORK because of the indentation of the "return" command, which instantly ends the function and returns a "result" on the first iteration.

def iterMul (x, y):
    """
    #this text should be shown to the end user to inform them of what they need to input in order to get the desired result.
    """
    result =0 
    #internally defines "result" for inside this function only.
    while y>0:
        result += x
        print "result = "
        print result
        y -= 1
    return result
        #have to remember to use "return" with a function. AND TO INDENT  IT PROPERLY (not inside the "while" loop).
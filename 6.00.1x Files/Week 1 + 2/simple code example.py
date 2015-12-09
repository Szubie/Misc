x = float(raw_input ("Enter a number: "))
p = int(raw_input ("Enter an integer power: "))
result = 1

for turn in range (p):
    print ("iteration: " + str (turn) + \
    "current result: " + str(result))
    result = result * x
print result

#he used 'return result' instead, but 'return' only works inside of functions (the things that have to be defined but are reusable).

#now to do the above as a procedure using a function:

def iterativePower (x, p):
    result = 1
    #internal definition of result, used only inside this enviroment, not the global environment. Doesn't effect global environ.
    for turn in range(p):
        print ("iteration: " + str(turn) + "current result: " + str(result))
        result = result * x
    return result
    #keyword return for a function to return the result when done. Needs to be in the function (indented), but only once, or errors.
    #return looks up the result for this computation in this enviroment
    
#Black box created.
#Can reuse this procedure elsewhere with different parameters. The notion of abstraction very powerful.
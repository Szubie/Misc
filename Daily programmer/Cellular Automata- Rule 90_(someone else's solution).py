import sys

#inputString = sys.stdin.read()
inputString="1101010"
#inputString="00000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000"

automataLength = len(inputString)

# Create array of booleans with leading and trailing false values.     #I need to remember this method!!
nextSequence = [ False ] * ( automataLength + 2 )
lastSequence = [ False ] * ( automataLength + 2 )

for i in range(1, automataLength + 1):

    if inputString[i - 1] == "1":
        lastSequence[i] = True

for i in range(1, automataLength + 1):
    if ( lastSequence[i] ):
        sys.stdout.write("x")
    else:
        sys.stdout.write(" ")
print

for k in range(25):
    for i in range(1, automataLength + 1):

        argA = lastSequence[ i - 1 ]
        argB = lastSequence[ i + 1 ]


        if  ( (not (argA and argB)) and ( argA or argB )):
            nextSequence[ i ] = True
        else:
            nextSequence[ i ] = False


    for i in range(1, automataLength):
        if ( nextSequence[i] ):
            sys.stdout.write("x")
        else:
            sys.stdout.write(" ")
    print

    lastSequence = list(nextSequence)
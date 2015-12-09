def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
testList = [1, -4, 8, -9]


 >>> print testList
  [1, 4, 8, 9]
#testList = [1, -4, 8, -9]

applyToEach(testList, abs)



>>> print testList
[2, -3, 9, -8]
  
  #testList = [1, -4, 8, -9]

def PlusOne(a):
   return a + 1

applyToEach(testList, PlusOne)



 >>> print testList
[1, 16, 64, 81]
#testList = [1, -4, 8, -9]

def AbsSquare(a):
    return abs(a*a)

applyToEach(testList, AbsSquare)
x=5

In [27]: p=3

In [28]: result =1

In [29]: for turn in range (p):
    ...:     print ("iteration" + str(turn) + "current result" + str(result))
    ...:     result = result * x
    ...:     
iteration0current result1
iteration1current result5
iteration2current result25

In [30]:  for turn in range (p):
    ...:     print ("iteration  " + str(turn) + "current result  " + str(result))
    ...:     result = result * x
    ...:    
iteration  0current result  125
iteration  1current result  625
iteration  2current result  3125

In [31]: for turn in range (p):
    ...:     print ("iteration  " + str(turn)   + "current result  " + str(result))
    ...:     result = result * x
    ...:     
iteration  0current result  15625
iteration  1current result  78125
iteration  2current result  390625

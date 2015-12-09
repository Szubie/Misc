# Hint: String slicing may be useful in this problem... 
# Hint: How would you check if a string is empty without using len()? An easy way you can check if a string, s, is empty is to check the condition,

#  s == ''
#Note that there is NO SPACE here. 


def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    
#test ="baba"



#"test"[0] == "test"[2]
#Out[6]: False

#But: if aStr[0] == aStr[-1]:
  #  print 1
 #   
#1

#So, lenRecur[x] = [x+0] + [x+1] + [x+2] ...+ [x-1]

#What is the base case?
#When length = 0. 


    
    if aStr == '':
        return 0
    
    

    # Recursive case: If the string is not zero-length, then remove the first
    #  character and the length is 1 + the length of the rest of the string
    return 1 + lenRecur(aStr[1:])

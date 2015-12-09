#Could find the max possible number made by two 3-digit numbers being multiplied together
#And then count backwards to find the biggest palindrome. From there, is there a way to check whether this palindrome can be made by multiplying two 3-digit numbers together?


def isPalindrome(x):
    """converts the number x into a string"""
    x=str(x)
    if len(x)<2:
        return True
    if x[0] == x[-1]:
        return isPalindrome(x[1:-1])
    else:
        return False

def two3digit(m):
    """attempts to divide m by all 3-digit numbers. Return "True" if a sucessful division results in a 3-digit number. False otherwise."""
    #This does not work correctly currently.
    n=999
    while n > 99:
        if m%n == 0:
            #The above AND BELOW symbols were the wrong way around!!!
            temp = m/n
            temp = str(temp)
            if len(temp) == 3:
                return True
            else:
                n -= 1
        else:
            n-=1
    return False

def findPalindrome(m):
    #From max
    #m=998001
    if m <=10000:
        return "None in range"
    if isPalindrome(m):
        #Then need to check to see if this number can be constructed by two 3-digit numbers being multiplied together.
        if two3digit(m):
            return m
        else:
            m -=1
            return findPalindrome(m)
    else:
        m -= 1
        return findPalindrome(m)
    #Need some way to stop this: it is recursive forever.
    
    
def findPalindrome2(m):
    #iterative approach, to evade max recursion limit.
    while m >9999:
        if isPalindrome(m):
        #Then need to check to see if this number can be constructed by two 3-digit numbers being multiplied together.
            if two3digit(m):
                return m
            else:
                m = m-1
        else:
            m = m-1
    return "None in range"
    
#Not sure why this doesn't work really...

def findPalindrome3():
    maxPalindrome = 1
    for x in range(100, 1000):
        for y in range(100, 1000):
            temp = x*y
            if isPalindrome(temp):
                if temp>maxPalindrome:
                    maxPalindrome = temp
#            if x*y<maxPalindrome:
#                break
    return maxPalindrome
    
#Remember the concept of: "Nested Loops". This is how you can check every possible answer.
#That other question you were stuck on may have been solvable through the use of triple nested loops.
#This approach is expensive, but clear-cut and works: yours didn't (not entirely sure why...)
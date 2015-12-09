#Oops, needed to revise how to check palindromes recursively. Stole this previously written code.    
#Recursive code needes to work towards making the problem smaller, and needs to have termination flags that will always trigger, either returning True or False accurately.
def convertString(x):
    """takes an int as input, returns a string"""
    return str(x)
    
def convertInt(x):
    """takes a string as an input, converts it back into an int"""
    return int(x)

def isPalindrome(x):
    """takes int as an input. Converts to a string and then checks to see if it is palindromic"""
    x=str(x)
    if len(x)<2:
        #if the length of the remaining number is 0, or 1, it is palindromic (reflected reads the same way).
        return True
    if x[0] == x[-1]:
        return isPalindrome(x[1:-1])
    else:
        return False

counter=0

def reverseString(x):
    """reverses a string"""
    #for char in range(len(x)/2):
        #Problem: "str object does not support item assignment". Therefore, we need a new approach. Perhaps a placeholder empty string, add in the items backwards.
    #    x[a], x[b] = x[b], x[a]
    #    a+=1
    #    b-=1
    temp=""
    b=-1
    for char in x:
        temp+=x[b]
        b-=1
        #Need to remember to BIND things: using the = sign, otherwise nothing happens. Ok this works forwards, now to do it backwards...
    return temp
    
    
def main(x):
    """takes a number as an input, checks to see if it's palindromic. If not, it reverses the number, converts it back into an int and then adds it to the original number before checking if it's a palindrome once again.
       Additionally, it keeps track of the amount of steps taken to reach the palindromic number."""
    original=x
    temp=x
    counter=0
    while True:    
        if isPalindrome(x):
            print original, "becomes palindromic after", counter, "steps: ", x
            return None
        else:
            #Problem is here: you need to bind something to the result returned by the function, otherwise it doens't do anything (encapsulation). Thus, although we ran convertString, nothing happened, and reverseString failed.
            #Next problem, our functions aren't "returning" anything, thus x is being bound to "None".
            x=convertString(x)
            x=reverseString(x)
            x=convertInt(x)
            x =x+temp
            temp=x
            counter+=1
            #Not quite adding the right things together. Overwriting the reversed string before saving it in temp.Ok, fixed!
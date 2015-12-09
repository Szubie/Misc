"""ReverseString recursion practice.py"""

"""Lesson: it's better to avoid spaces in source file names, you can't import them properly. There is a way to force it to, but it behaves differently:
foo_bar = __import__("foo bar")"""

import ReverseString

def palindrome(x):
    if ReverseString.reverseString2(x)==x:
        return True
    else:
        return False
        
#Above can be shorted:

def palindrome2(x):
    return ReverseString.reverseString2(x)==x
    
    
#Now if you just added a check to see if it's a valid word, it's good to go (would need a word list for that).
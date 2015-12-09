#Default Value Exercise

def isAlphabeticalWord(word, wordList=None):
    if (len(word) > 0):
        curr = word[0]
    for letter in word:
        if (curr > letter):
            return False
        else:
            curr = letter
    if wordList is None:
        return True
    return word in wordList
    
    
#Don't Use Mutable Types As Default Values! They don't generate a new list everytime, they keep using the old one.


def f(x, myList = []):
    myList.append(x)
    return myList
""">>> f(6)
[6]
>>> f(10)
[6, 10]"""

#This won't work.

def f(x, myList = None):
    if myList == None:
        # This WILL allocate a new list on every call to the function.
        myList = []
    myList.append(x)
    return myList
""">>> f(6)
[6]
>>> f(10)
[10]"""


#This does.


"""Rules for using default values:
- complexWithDefaults("cat", "werewolf", 40, frogsFound=80)

-The keyword assignment must go at the end

-You can even specify things that do not have a default value using keyword assignments. 
- complexWithDefaults(anotherthing="werewolf", something="cat", sillywalks=40)"""

def lotsOfParameters2(a=1,b=2,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e
    
"""cannot assign multiple values to one keyword argument (like "a")."""
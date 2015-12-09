# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string 
    """
    #result = ""
    #for ch in aStr:
    #    result = ch + result
    #return result

    if aStr == '':
        return ''

    return aStr[-1] +  reverseString(aStr[:-1])

#print reverseString('abc')

#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if x == "":
        return True
    n = word.find(x[0]) 
    return n >= 0 and x_ian(x[1:], word[n:])

#    for ch in x:
#    #while x > "":
#        try:
#            n = word.index(x[0])
#        except:
#            return False
#        word = word[n:]
#        x = x[1:]
#    return True


#print  x_ian('john', 'mahjong')


#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.
    text: str
    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    #ltext = text.split()
    #result = ""
    #for w in ltext:
    #    result += w
    #    if len(w) >= lineLength:
    #        result += "\n"
    #    else:
    #        result += " " 
    #return result

    ltext = text.split()

    def incF(ltext, lineLength):
        if ltext == []:
            return ""
        if len(ltext[0]) >= lineLength:
            return ltext[0] + "\n" + incF(ltext[1:], lineLength)
        else:
            return ltext[0] + " " + incF(ltext[1:], lineLength)
    return incF(ltext, lineLength)

#print insertNewlines("John has five loooooooong fingers", 4)
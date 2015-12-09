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
    if len(aStr) == 1:
        return aStr
    if len(aStr) == 0:
        return aStr
    return aStr[-1] + reverseString(aStr[:-1])

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
    #temp = word[-1]
    #string = ""
    #if len(word) == 1:
    #    return x in reverseString(string)
    #if temp in x:
    #    string += temp
    #return x_ian(x, word[:-1])
    
    
    

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    #if len(text) <= lineLength:
    #    return text[:lineLength]
    #return text[:lineLength] + "\n" + insertNewlines(text[lineLength:], lineLength)
#This works to a degree, but it cuts words in half. Rereading the question, I realise we were supposed to cut after the end of the word...
#The other person has solved this by splitting the string and creating a list. Thus, the breaks can come after elements of the list (the words).

#Below is my somewhat more ugly solution (which uses an iterative loop within the recursive loop....).
    x = 0
    if (len(text)+x) <= lineLength:
        return text[:lineLength]
    while text[lineLength+x] != " ":
        x += 1
        if (lineLength+x+1) > len(text):
            return text
    return text[:lineLength+x] + "\n" + insertNewlines(text[lineLength+x:], lineLength)
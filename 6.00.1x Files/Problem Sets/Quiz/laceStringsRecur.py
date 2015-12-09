def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return s2[len(s1):]
        if s2 == '':
            return s1[len(s2):]
        else:
            return out + helpLaceStrings (s1, s2,'')
    return helpLaceStrings(s1, s2, '')

#laceStringsRecur('abcd','efghi')

#Only three lines of code allowed....perhaps I could do it recursively if allowed more, but idk how to do it this way.

#This doesn't really work either. Only if one or more of the strings are empty. 
#Nabbed 1.66 points for it at least, I guess....
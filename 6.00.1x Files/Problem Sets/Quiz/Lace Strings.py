def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    s3= ""
    x=0
    
    while x < len(s1):
        s3 += s1[x]
        s3 += s2[x]
        x += 1
        if x >= len(s2):
            s3 += s1[len(s2):]
            return s3
        
    s3 += s2[len(s1):]
    return s3
    
#'abcd' and 'efghi'
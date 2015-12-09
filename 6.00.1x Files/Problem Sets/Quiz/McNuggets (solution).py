def McNuggets(n):
    if n == 0:
        return True
    #Below code is actually unecessary, but is my addition. An attempt to make the code more efficient.
    if n%6 == 0:
        return True
    if n%9 == 0:
        return True
    if n%20 == 0:
        return True
    #end of my code
    elif n < 0:
        return False
    return McNuggets(n-6) or McNuggets(n-9) or McNuggets(n-20)
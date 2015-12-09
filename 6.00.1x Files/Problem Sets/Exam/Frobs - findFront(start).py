def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    #Must be done recursively
    if start.getBefore() == None:
        return start
    return findFront(start.getBefore())
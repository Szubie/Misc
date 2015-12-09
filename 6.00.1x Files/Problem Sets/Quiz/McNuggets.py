def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # 6a, 9b, 20c
    ####

    
    if n%6 == 0:
        return True
    if n%9 == 0:
        return True
    if n%20 == 0:
        return True
    
    if n == 0:
        return True
        
    if n%15 == 0:
        return True
        
    if n%26 == 0:
        return True
        
    if n%29 == 0:
        return True
        
    if n%35 == 0:
        return True
    
  
    



    
    return False
    
#This doesn't really work. Only the division tests work. Doesn't check every possible combination of values: but is there a mathematical trick to avoid huge compuation (or are we allowed to make very slow code?).
#How would you code it anyway?



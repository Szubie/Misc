def primes2(limit):
    if limit < 2: return []
    if limit < 3: return [2]        #Just get edge cases out of the way quickly.
    lmtbf = (limit - 3) // 2         # /2 does floating point division in Python 3: // is integer division (quotient without the remainder). So, half of the upperlimit(-3).
    buf = [True] * (lmtbf + 1)       #Creates a list of True elements, as long as the half of the limit.
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):                          # for i in range (length of the list, buf)
        if buf[i]:                                                              #If the element is True (by default it starts off as True):
                                                                                
                                                                                #Now things get cryptic: what's going on from here to the end?
            p = i + i + 3                                                       #"p"? first run: 0+0+3=3  second run:  = 1+1+3 = 5
            s = p * (i + 1) + i                                                 #"s"? first run: 3*(0+1)+0=3 second run:    = 5*(1+1)+1 = 11
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)                        #For the items in the list, beginning with "s", every "p" item is changed to False (timesed by:  (half the limit-"s") (divided by "p"+1))
                                                                                # ":" is the delimiter of the slice syntax to 'slice out' sub-parts in sequences , [start:end]   #" [::3]" it means 'nothing for the first argument, nothing for the second, and jump by three'. It gets every third item of the sequence sliced. Extended slices is what you want. New in Python 2.3  #While indexing is used to obtain individual characters, slicing allows you to otain a sub-string.                                                               
                                                                                #To help explain this code, this is what happens when you remove everything after [False]:
                                                                                #"ValueError: attempt to assign sequence of size 1 to extended slice of size 16." 
                                                                                #HOWEVER, replacing the code with "11" returns ValueError: attempt to assign sequence of size 11 to extended slice of size 16: thus, the latter code must evaluate to 16??


                                                                                #((48-3)//3+1)
                                                                                #Out[21]: 16
                                                                                                                                                                
                                                                                #The reason why is actually basic maths: the order of operations. (45//3)+1  
                                                                                
                                                                                #So, exactly 16 things needed to be changed in the list and exactly 16 Falses are available (they are stored in a list).  
                                                                                
                                                                               
                                                                                #The way this works is this: the string is split, returning a SUBSTRING of buf, which moves up in steps of p. 
                                                                                #The values of this substring are then rebound to False by equating them with a list full of "False" elements. The changes are reflected in main string.                                                                          


                                                                                
                                                                                #What did this achieve?
                                                                                #Run 1: The list, beginning with the "3"rd (4th, since 0 is an entry) entry, taking "3" steps each time = False* ((48-3)//(3+1))
                                                                                #                                                                = False* (45)//(4)
                                                                                #                                                               = False*11
                                                                                #But...there are 16 flags changed by this operation?
                                                                                
                                                                                
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]                  #returns a list with the value [2] to begin with, which is then added to by...     # [2] +[3] = [2, 3]
                                                                                # Run 1: [3+3+3 for 3, v in enumerate(buf) if v]    #v is each value in the "enumerate" list buf. Returns it "if v" (if True).
                                                                                #         [2+[9 for 3, 1]
                                                                                
                                                                                
                                                                                #At the very end, what it seems to do is: i starts at 0, begins counting up by 1 each time.
                                                                                #If the "i"-th element of the list is True, return i+i+3 (if i is 0, return 3, the second prime number (after 2)). If i=47, return 47+47+3 (97).
                                                                                #If False, do nothing.

                                                                                
                                                                                #In other words: for each prime number found in lower half of the limit bound, double it (it becomes even), and then add 3 (makes it odd again, and finds a prime number)?? #Provably wrong? 3+3+3=9 (not prime). 11+11+3=25 (not prime).

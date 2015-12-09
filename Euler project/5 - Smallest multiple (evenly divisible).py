

def count(n):
    n=2520
    lst= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    temp = lst
    if temp[0] == 21:
        return n
    while True:
        if n%lst[0] == 0:
            temp=lst[1:]
        elif  temp[0] == 21:
            return n
        else:
            n+=1
            temp = lst
            
#Initial implementation TOO SLOW.

#We can speed up by checking only the multiples on 20 at first, and going deeper when it passes that first test. (~20 times faster?)

def count2(n):
    lst= [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    counter=0
    while True:
        for x in range(2, 21):
            if n%lst[x]!=0:
                n+=20   
                counter = 0
                break
                #break, this is not the answer. Improves effiency (Although small cost, 1 extra check). Breaks out of the "range" "loop".
            if n%lst[x]==0:
                counter+=1
            if counter == 19:
                return n
        n+=20   
        counter = 0
    
# FIXED: n+=20 was INSIDE the loop checking the ranges.
#(This actually doesn't work, even when given the right answer to start with.)
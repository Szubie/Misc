def prob2(n):
    """recursive implementation. This will only return the probability that they do NOT share the same birthday."""
    
    #Edge case check.     #Base case first. We will DEcrease n by one every time to move towards this?
    if n==1 or n==0:
        return  1
        
    #Now the main part?

    #return 1- (float(365-n)/365*prob2(n))
        
        #How strange, this alternates between very high and very low. Must be to do with the 1-, which is messing stuff up.
        
    return -1/float(360-n) - (float(365-(n-1))/365*prob2(n-1))

    #This will accurately return the probability that they DON'T share the same birthday using recursion. Is there a way to make it do the 1-prob2(n) inside the function without breaking it?
 
    
prob2(23)


#Ooof, this doesn't quite work. Why not? It should be the right number of steps...
#Additionally, it seems to give an answer similar to the previous recursive answer....which is one which does not do the 1-(recursive answer)


#I guess this is because n is changing every time. We can actually control where exactly n changes though, by changing the variables used in the recursive call.


#Ah, still doesn't work.


#Because each recursive call is actually minusing the numbers that should be positive?

#Meh, nothing seems to work...
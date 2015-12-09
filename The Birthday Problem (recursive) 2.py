
def prob2(n):
    """recursive implementation. This will only return the probability that they do NOT share the same birthday."""
    
    
    #Edge case check.     #Base case first. We will DEcrease n by one every time to move towards this?
    if n==1 or n==0:
        return  1
        
    #Now the main part?
    n-=1
    #return 1- (float(365-n)/365*prob2(n))
        
        #How strange, this alternates between very high and very low. Must be to do with the 1-, which is messing stuff up.
        
    return (float(365-n)/365)*prob2(n)

    #This will accurately return the probability that they DON'T share the same birthday using recursion. Is there a way to make it do the 1-prob2(n) inside the function without breaking it?
 

#Wow, I can't believe how long it took you to piece the logic of this code together! You wrote it! 
#The addition of those brackets, although unecessary for the code to work, helps make the logic behind this much clearer to me.

#So basically, we're multiplying together fractions of 365-n/365 until we get to the limit, 364/365. 

#Then, when the limit is reached, we make prob2(1) return 1: this will simply multiply all the other fractions by 1, leaving them the same.
#The Birthday Problem

#def probability(n):
#    """where n is the number of people in the sample, calculate the probability of any two people having the same birthday.
#    The way to approach this is to calculate the probability of each individual having a pair with the same birthday as them. Thus, run through the whole group."""
#    a=float(1)/float(365) #constant probability of a person having the same birthday as you.
#    b=1
#    ans=0
    
    #First, you write for the first case. Compare the probability of 1st individual having the same birthday as another person.   
#    while b<n:
    
#        ans+=a*(n-b)
    
#        b+=1
        
#    return ans
    
#probability(23)

"""The reason this doesn't work is because 1/365 returns 0. It's rounding the answer automatically?"""
"""The only way I can find to make it work is to call:
    float(1)/float(365)
    """
    
"""Still isn't correct. In fact, whole methodology is wrong!
    I think the problem is that when there are 3 people, 1-2, 1-3 have a probability of 1/365, but 2-3 doesn't.
    It only gets worse the more people there are."""

def prob(n):
    """where n is the number of people in the sample, calculate the probability of any two people having the same birthday.
    The way to approach this is to calculate the probability of each individual NOT having the same birthday as another in the class.
    Then, you can do 1-(ans) to find the probability."""
    a=364 #This is the numerator. This divided by the denominator provides the probability that a person does NOT have the same birthday as another in the class.
    b=365 #denominator, doesn't actually change.
    
    c=0 #tracks the total probability.
    
    #For one person:
    #c=float(a)/float(b)
    #return 1-float(c)
    
    while a>(b-n):
        d=float(a)/float(b)
        if c==0:
            c=d
        else:
            c=c*d
        a-=1
        
    return 1-float(c)
    
prob(23)


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
 
    

def prob3(n):
    """takes in n and shows the probability that they DO share the same birthday by reversing the function prob2"""
    return 1-prob2(n)
    

    
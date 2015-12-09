"""The version below uses array lookup to test for primality. The function primes_upto() is a straightforward implementation of Sieve of Eratosthenesalgorithm. It returns prime numbers less than or equal to limit. """

def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1)  #Amazingly, this returns a list in which the first two items are False, and the rest (up to the limit) are True. TWO Falses start the list because 0 and 1 are not prime.
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)`` #This piece of code runs only for just over half of n (limit).  WHY? Because within this loop is the process that checks off multiples of a prime, STARTING WITH THE PRIME SQUARED.
        if is_prime[n]: #Checks to see whether the list entry is True or False. If true, exectues.
            for i in range(n*n, limit+1, n): #If it is a prime, it sets changes the list items later that are multiples of n (Again, starting from n squared).
                is_prime[i] = False #Changes the flag, from True to False. These multiples will now not be returned (as they are not primes).
    
            #So, firstly, the code creates a list and then crosses off all the multiples systematically BEFORE IT HAS RETURNED ANYTHING.
    
    return [i for i, prime in enumerate(is_prime) if prime] 
    #However, how does this return code work? Very mysterious.
    
    #Runs through the whole list again, keeping a running count of the number in i. (i for i, for each found in i?)
    #For each item ("prime") in the list "(enumerate(is_prime)" it will return it IF "prime" (if it is TRUE. If False, it does nothing but keeps running).
    
    
    #Encapsulation, is_prime is only accessible through calling this function.
    
    
#For the very large numbers, the list output seems to end in ...] Too long?
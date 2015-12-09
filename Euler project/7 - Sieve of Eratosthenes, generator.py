"""Using generator The following code may be slightly slower than using the array/list as above, but uses no memory for output: """

def iprimes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1)                               #Concept is the same: creates a list, first two elements indexed are False, rest are True (up to limit).
    for n in xrange(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``           #Again, checks half the list for primes (the multiples of primes above halfway will have already been marked by lower prime numbers, until prime squared).
        if is_prime[n]:
            for i in range(n * n, limit + 1, n): # start at ``n`` squared       #Eliminates multiples of prime numbers later in list.
                is_prime[i] = False
    for i in xrange(limit + 1):
        if is_prime[i]: yield i                                                 #Then "yields" the results, as is characteristic of generators. Generators, may be a bit slower, but save a lot of memory by only generating an item when needed.
                                                                                #As a result, there is no need to keep all the values in memory at once.
        
        
#Whoops, how do you use generators again?? How do you call them?

"""Generators have a next() method which starts/resumes execution of the procedure. 
Call this method on the generator like so: iprimes_upto(10).next()
"""

#Yield suspends execution and returns a value.
#Returning from a generator raises a StopIteration exception.

#Once you reach the end of the yields, it stops iteration too.


#for i in range(1, 10000000):
#    iprimes_upto(10000000).next()

#It hangs after running the above. Something wrong, or is it really that slow?

#The above code does not seem to actually be returning the right thing.


#This code works:
"""
for prime in iprimes_upto(10000000):
       print prime
"""

#This prints the generated numbers until the generator hits its limit.

"""Why use generators?

A generator separates the concept of computing a very long sequence of objects from the actual process of computing them explicity. (even a potentially infinite sequence)

Allows one to generate each new object as needed as part of another computation (rather than computing a very long sequence, only to throw most of it away while you do something on an element, then repeating the process.


Another way of thinking of it: the generator theoretically gives you every single fibonacci number in existance, and if you want to stop and do something to each one of them, you can do so.
"""
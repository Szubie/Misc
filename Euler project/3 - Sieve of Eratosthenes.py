factors = []

def primes_sieve2(limit):
    a = [True] * (limit/2 +1)                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
                
for prime in primes_sieve2(600851475143 ):
    if 600851475143 % prime == 0:
        factors.append(prime)
        
        
#This fails, because the amount of numbers to be stored in range() is too large.
#In your first example, primes_sieve doesn't maintain a list of primality flags to strike/unset (as in the algorithm),/
#but instead resizes a list of integers continuously, which is very expensive: removing an item from a list requires shifting all subsequent items down by one.

#In the second example, primes_sieve1 maintains a dictionary of primality flags, which is a step in the right direction, but it iterates over the dictionary in undefined order, /
#and redundantly strikes out factors of factors (instead of only factors of primes, as in the algorithm). You could fix this by sorting the keys, and skipping non-primes /
#(which already makes it an order of magnitude faster), but it's still much more efficient to just use a list directly. 

#(Note that this also includes the algorithmic optimization of starting the non-prime marking at the prime's square (i*i) instead of its double.)




#This fails due to MemoryError.

#An idea?
#To avoid memory issues, you could store your list of primes in a file on the hard disk. Store one prime per line and read the file every time you check a new number.


#Could also halve the number in range (factor cannot be more than half).
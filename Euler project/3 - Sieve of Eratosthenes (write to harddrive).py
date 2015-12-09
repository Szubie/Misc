primes_path = r'C:\temp\primes.txt'

def genPrimes():
    for line in open(primes_path, 'r'):
        yield int(line.strip())    

def addPrime(prime):
    primes_file = open(primes_path, 'a')
    primes_file.write('%s\n' % prime)
    primes_file.close()

def findPrimes(maxnum):
    for i in xrange(2, maxnum):
        is_mul = False
        for prime in genPrimes():  # generate the primes from a file on disk
            if i % prime == 0:
                is_mul = True    
                break            
        if not is_mul:           
            addPrime(i)  # append the new prime to the end of your primes file
            
            
    
#This still fails: Python int too large to convert to C long (xrange).


#import itertools
#for b in itertools.count(1):
	

    #!/usr/bin/python
    # xisk - May 2013
    # Python 2.7.3
    # License: Creative Commons BY-ND 3.0
     
def lpf(x):
        lpf = 2;
        while (x > lpf):
                if (x%lpf==0):
                        print "the lpf is:", lpf
                        x = x/lpf
                        lpf = 2
                        print x

                else:
                        lpf+=1;
        print("Largest Prime Factor: %d" % (lpf));
     
def main():
        x = long(raw_input("Input long int:"))
        lpf(x);
        return 0;
     
if __name__ == '__main__':
    main()

#This isn't the sieve of Eratosthenes. Actually, this is quite a simple, but effective approach.

#This takes a completely different approach to the problem, searching only for the highest prime factor. It counts from 2 to x, checking to see if x is divisible by the current number (that the current number is a factor of x)
#It saves the largest factor as it goes, overwriting previous smaller ones until it terminates upon reaching x.

#But how does it check that the factor is a prime number? (It works by dividing x by the smallest possible factor (which is by definition a prime factor) each time, and then checking if the resulting factor can be divided further.
#If so, it is not a prime factor, and the process continues. If the number cannot be divided any more, it is a prime factor (and the largest one, since all the other smaller prime factors have been found first by lpf).
#Need a solid understand of prime factors to get this solution.


#if x%lpf == 0 (if x is divisible by lpf):
# x = x/lpf
#lpf = 2

# so x becomes x/lpf
#and the count for the lowest factor begins again (and yes, it seems to search for the lowest factor??)



#%s Serves as a placeholder for a string value that will be supplied with values placed after the last % character in the print statement. 
#Likewise, %d serves as a placeholder for a signed integer decimal value.
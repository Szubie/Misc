"""The version below uses a set to store the multiples. set objects are much faster (usually O(log n)) than lists (O(n)) for checking if a given object is a member. 
Using the set.update method avoids explicit iteration in the interpreter, giving a further speed improvement. """

def eratosthenes2(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples: #if it's not in multiples, it is a prime, yields it.
            yield i
            multiples.update(range(i*i, n+1, i)) #Then, it updates the "set", multiples. Up to the number input, n+1. Marks off all the multiples of i, starting with i SQUARED (interestingly, if ascending up, earlier primes cover everything below the prime squared)
            #For instance, 5: 10 covered(by 2), 15 covered(by3), 20 covered(by2,4), 25.

 
print(list(eratosthenes2(10000000))) #This gathers all the numbers yielded by the generator (up to n) and stores them inside a list, which it then prints.




#Then, to find the 10,001st prime, request list(eratosthenes2(10000000))[10000]
#(10000 ,not 10001, remember that [0] is the first item of a list)
#This is very slow, however it actually works! How though? Need to learn from it, not just copy and paste it.



#Using set lookup
def genPrimes():
    x = 2
    p = [x]
    while True:
        for c in p:
            if x % c == 0:
                x += 1
            else:
                p.append(x)
                #have to use the .append method for lists
                x += 1
                yield (x-1)

                
genPrimes().next()

#Doesn't work.
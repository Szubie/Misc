def fib(n):
    if n>=0:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        else:
            return fib(n-1)+fib(n-2)
    else:
        print "Not a valid number!"
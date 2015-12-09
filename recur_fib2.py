def recur_fib2(x):
    if x==0:
        return 0
    elif x==1:     #A required bit! Else it runs forever (one of x-1 or x-2 WILL be odd, miss 0)
        return 1
    else:
        return recur_fib2(x-1) + recur_fib2(x-2)
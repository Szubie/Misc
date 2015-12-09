
#Recursive fibonacci.

def recur_fib(x, y=0, p=1):
    if x==0:
        return 0
    if x==1 or x==2:  #This was just slightly wrong
        return y+p
    else:
        return recur_fib(x-1, y=p, p=y+p)
        
        #Previously, I was wrong to have return y+p +recur_fib(x-1, y=p, p=y+p)
        
        
#def print_fib(y):   #Need to use a different binding, not also x?
#    while y>=0:
#        x=y
#        print recur_fib(x)
#        y=-1

#So weird, that doesn't work...
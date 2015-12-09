def fizzBuzz(x,y):
    """x is upper limit (100), y is the start (1)"""
    if x==1:
        return 100
    if y%3==0 and y%5==0:
        print "FizzBuzz"
    elif y%3==0:
        print "Fizz"
    elif y%5==0:
        print "Buzz"
    else:
        print y
    return fizzBuzz(x-1, y+1)
def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if f(guess) - guess < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess

def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit, 0.0001) #changing to tryit(x) does not work

#The error returned is that "'tryit' is not defined". How is this possible if it was defined just the line above?
#"return 'tryit'" doesn't fix it....

#To fix it, had to change "return fixedPoint(tryit(a), 0.0001)" to "return fixedPoint(tryit, 0.0001).
#Before it would just return a float which couldn't be called, now it returns a function which can be called?
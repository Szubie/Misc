#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquares(x):
    y=0
    #Range must be x+1, since you want to include x.
    for num in range(1, x+1):
        y+=num*num
    return y

def squareOfSum(x):
    y=0
    #Range must be x+1, since you want to include x.
    for num in range(1, x+1):
        y+=num
    return y*y
    
def main(x):
    return squareOfSum(x)-sumOfSquares(x)
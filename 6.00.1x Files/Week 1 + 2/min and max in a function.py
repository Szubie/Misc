def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return min(max(lo, x), hi)
    
    #conditional words ("if", "while") were not available for use in this task
    #Instead, the inbuilt functions "min" and "max" were suggested.
    
    #was unsure how to solve this without conditionals: found advice:
    
    #The function we are writing has three numbers as parameters: low, high and x.
    #We know that high is a bigger number than low, but we don't know where x fits in. 
    #Our function determines which of these 3 numbers is the one in the middle.
    #Since we do know that low can never be the biggest number, we use max(x, low) to 
    #determine which of these two numbers is the bigger one. There are two cases
    
    #low is bigger than x: We know now x is the smallest, low the middle and high the biggest number. 
    #So in this case we could simply return low but the second case shows why we need the min function on the outside

    #x is bigger than low. We now know that low is the smallest number. 
    #What we don't know is if x is bigger than high or the other way round. So that's why we check for the minimum of x and high

#result = 0
#placeholder for result, actually not even needed. (= result, return result)

#We are searching for the number in the middle of these 3.

#if lo is smaller than x, it will be printed, as it is smaller than hi.
#if x is greater than lo but smaller than hi, it will be printed.
#if x is greater than both lo and hi, hi will be printed

#Very neat and tidy!
#What if lo were not defined as being smaller than hi though??


#Alternative solutions:
result = (((lo + x + hi)) - max(lo,x,hi) - min(lo,x,hi))
finresult = round(result, 2) #the grading system accepts only rounded numbers? 
return finresult

#adding them all and taking away the biggest and the smallest, you are left with the middle number.

def clip(lo, x, hi):
    return sorted(lo, x, hi)[1]
#cheeky method, sorts them into a list and returns the 2nd in the list!

x=max(lo,x) x=min(x,hi) return x
#simple and effective. 
ans=0
temp1=1
temp2=1
add=0


while ans<4000000:
    #Need to store both previous numbers
    
    #Temporarily keeping value

    
    #Switching ans2 to current value, then using temp to add the previous value to the current value.
    ans= temp1 + temp2
    temp1=temp2
    temp2=ans
    
    #testing
    print ans
    
    if ans%2 == 0:
        add+=ans
        

print "the sum of even fibonacci numbers below 4 million is:", add
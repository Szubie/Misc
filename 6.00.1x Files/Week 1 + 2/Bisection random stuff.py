balance = 3926
annualInterestRate = 0.2
MinimumFixedMonthlyPayment= 327
newBalance = 5
UpperBound = 400
LowerBound = 300
MinimumFixedMonthlyPayment = ((UpperBound + LowerBound)/2.0) 

while newBalance>0:
    MinimumFixedMonthlyPayment = ((UpperBound + LowerBound)/2.0)
    print MinimumFixedMonthlyPayment

    if newBalance >0:
        LowerBound = MinimumFixedMonthlyPayment 
   
    if newBalance <0:
        UpperBound = MinimumFixedMonthlyPayment

   
print ('LowerBound = '+ str(LowerBound) + ' UpperBoand=  ' + str(UpperBound) \
+' MinimumFixedMonthlyPayment=  ' +str(MinimumFixedMonthlyPayment))



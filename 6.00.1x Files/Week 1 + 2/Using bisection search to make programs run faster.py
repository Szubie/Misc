balance = 3926
annualInterestRate = 0.2

#delete above

MonthlyInterestRate = (annualInterestRate/12.0)
newBalance = balance
UpperBound = (balance * (1+MonthlyInterestRate)**12/12.0)
LowerBound = balance/12.0
MinimumFixedMonthlyPayment = (UpperBound + LowerBound) /2.0
Error= 0.01

while newBalance !=0:
    Month = 1
    Int = 0 
    UnpaidBalance = balance - MinimumFixedMonthlyPayment
    
    newBalance = balance
    while Month <=12:
        MinimumFixedMonthlyPayment = (UpperBound + LowerBound)/2.0
        print MinimumFixedMonthlyPayment
        print "Month",
        print Month
        UnpaidBalance = newBalance - MinimumFixedMonthlyPayment
        Int = UnpaidBalance * (annualInterestRate/12)  
        newBalance = round(UnpaidBalance + Int, 2)
        print "Remaining balance:",
        print newBalance
        Month += 1
    if newBalance >0:
        LowerBound = MinimumFixedMonthlyPayment 
    if newBalance <0:
        UpperBound = MinimumFixedMonthlyPayment
    
print "Lowest Payment:",
print round(MinimumFixedMonthlyPayment, 2) 
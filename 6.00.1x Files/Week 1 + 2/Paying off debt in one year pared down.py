newBalance = balance
MinimumFixedMonthlyPayment = 10

while newBalance >0:
    Month = 1
    Int = 0 
    UnpaidBalance = balance - MinimumFixedMonthlyPayment
    MonthlyInterestRate = (annualInterestRate/12.0)
    newBalance = balance

    while Month <=12:
        UnpaidBalance = newBalance - MinimumFixedMonthlyPayment
        Int = UnpaidBalance * (annualInterestRate/12)  
        newBalance = round(UnpaidBalance + Int, 2)
        Month += 1
    MinimumFixedMonthlyPayment +=10
    
print "Lowest Payment:",
print MinimumFixedMonthlyPayment -10
balance = 3926
annualInterestRate = 0.2

#delete above

newBalance = balance
MinimumFixedMonthlyPayment = 10

while newBalance >0:
    Month = 1
    Int = 0 
    UnpaidBalance = balance - MinimumFixedMonthlyPayment
    MonthlyInterestRate = (annualInterestRate/12.0)
    newBalance = balance

    while Month <=12:
        print "Month",
        print Month
        UnpaidBalance = newBalance - MinimumFixedMonthlyPayment
        Int = UnpaidBalance * (annualInterestRate/12)  
        newBalance = round(UnpaidBalance + Int, 2)
        print "Remaining balance:",
        print newBalance
        Month += 1
    MinimumFixedMonthlyPayment +=10
    print MinimumFixedMonthlyPayment
print "Lowest Payment:",
print MinimumFixedMonthlyPayment -10
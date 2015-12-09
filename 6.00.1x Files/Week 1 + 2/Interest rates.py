balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#All of above is temporary and must be removed. Also need to round the answers below.

Month = 1
UnpaidBalance = 0
MinimumMonthlyPayment= balance * monthlyPaymentRate
Int = 0 
TotalPaid = 0

while Month <= 12:
    print "Month",
    print Month
    MinimumMonthlyPayment = round(balance * monthlyPaymentRate, 2)
    print "Minimum monthly payment:",
    print MinimumMonthlyPayment
    TotalPaid += MinimumMonthlyPayment
    UnpaidBalance = balance - MinimumMonthlyPayment
    Int = UnpaidBalance * (annualInterestRate/12)  
    balance = round(UnpaidBalance + Int, 2)
    print "Remaining balance:",
    print balance
    Month += 1
print "Total paid:",
print TotalPaid
print "Remaining balance:",
print balance
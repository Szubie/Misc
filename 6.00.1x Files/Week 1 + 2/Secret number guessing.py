x= 100
y=0
guess =0
attempts = 0

print "Please think of a number between 0 and 100!"
guess = (x + guess)/2
print "Is your secret number", 
print guess,
print "?"
feedback = raw_input("Enter 'h' to indicate that the guess is too high. Enter 'l' to indicate that the guess is too low. Enter 'c'to indicate that I guessed correctly.")
if feedback == "c":
       print "Game over. Your secret number was:",
       print guess


if feedback !="c":


    if feedback == "h":
        guess = (guess+y)/2
    
    
    
    if feedback == "l":
       guess = (guess+x)/2

else:
       print "invalid input, please try again."

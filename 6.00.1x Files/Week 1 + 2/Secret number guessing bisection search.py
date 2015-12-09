print "Please think of a number between 0 and 100!"

lower = 0
higher = 100
midPoint = (lower+higher)/2

while True:

    print "Is your secret number",
    print midPoint ,
    print "?"

    user = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if user == "h":
        higher = midPoint
        midPoint = (lower+higher)/2
    if user == "l":
        lower = midPoint
        midPoint = (lower+higher)/2
    if user == "c":
        print "Game over. Your secret number was:",
        print midPoint
        break
    elif user != "h" and user != "l" and user != "c":
        print "Sorry, I did not understand your input."
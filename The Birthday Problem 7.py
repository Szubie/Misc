prob = 1.0
classSize = 23

for i in range(classSize):
    prob = prob * (365-i)/365

print("probability of no shared birthdays = ", prob)

#The answer is actually wrong? should be 1-ans
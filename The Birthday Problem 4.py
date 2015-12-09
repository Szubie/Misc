import random

classSize = 23
year = [0]*365

for i in range(classSize):
    newBDay = random.randrange(365)
    year[newBDay] = year[newBDay] + 1

print(year)
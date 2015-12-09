#The Birthday Problem #2

import random
#Using the random library, very cool. Important, calling methods from it.

classSize=23
birthdayList=[]

for n in range(classSize):
    newBDay=random.randrange(365)
    birthdayList.append(newBDay)
    
print birthdayList

###

foundDupe = False   #Default value is False, changes to True when it finds what it's looking for. A common construction. 
for num in birthdayList:
    if birthdayList.count(num) > 1:
        #.count method, goes through list and counts how many times each birthday occurs.
       foundDupe = True
       
###

"""Now we need to wrap these loops into an outer loop that will repeat the experiment multiple times"""
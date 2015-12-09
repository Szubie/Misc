#String methods! Things to do with strings


str1 = 'exterminate!'
str2 = 'number one - the larch'

str1.upper
Out[9]: <function upper>
#MUST remember to add empty brackets if you want to evaluate the string.
str1.upper()
#.upper makes all letters upper case
Out[10]: 'EXTERMINATE!'

str1.islower
Out[11]: <function islower>
#no brackets and so it doesn't work

str1.islower()
Out[12]: True
#checks to see if it's lower (True) or not (False).

 str2 = str2.capitalize()
str2
='Number one - the larch'
#.capitalize capitalises the first letter and makes the rest lowercase.

str2.swapcase()
Out[17]: 'nUMBER ONE - THE LARCH'
#.swapcase switches all the cases.

 str1.index('e')
 Out[18]: 0

#CURIOUS. Seems to try to find the middle value?? 0?

str2.index('n')
Out[19]: 8

#Need to look at indexing more...

str2.find('n')
Out[20]: 8

#ok....?

str2.index('!')
ValueError: substring not found 

 str1.count('e')
Out[24]: 3


str1 = str1.replace('e', '*')
str1

Out[25]: '*xt*rminat*!'

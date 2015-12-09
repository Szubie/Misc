# -*- coding: utf-8 -*-
"""McDonald’s sells Chicken McNuggets in packages of 6, 9 or 20 McNuggets. Thus, it is possible, for example, to buy exactly 15 McNuggets (with one package of 6 and a second package of 9), but it is not possible to buy exactly 16 McNuggets, since no non- negative integer combination of 6's, 9's and 20's add up to 16. To determine if it is possible to buy exactly n McNuggets, one has to find non-negative integer (can be 0) values of a, b, and c such that

6a+9b+20c=n
Write a function, called McNuggets that takes one argument, n, and returns True if it is possible to buy a combination of 6, 9 and 20 pack units such that the total number of McNuggets equals n, and otherwise returns False. Hint: use a guess and check approach."""

#Attempt every possible combination. 
#To do this, use nested loops.

def mcNuggets(n):
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if 6*a + 9*b +20*c == n:
                    return True
    else: #Improper nesting! Only declare False once all options have been tested
        return False
                    
mcNuggets(20)

#Optimise below.

def mcNuggets2(n):
    for a in range(n/6+1):
        for b in range(n/9+1):
            for c in range(n/20+1):  #Requires a +1, otherwise it will fail to find mcNuggets2(20)
                if 6*a + 9*b +20*c == n:
                    return True
    else: #Improper nesting! Only declare False once all options have been tested
        return False
                    
mcNuggets2(20)


"""... we can write an exhaustive search to find the largest number of McNuggets that cannot be bought in exact quantity. The format of the search should probably follow this outline:
• Hypothesize possible instances of numbers of McNuggets that cannot be purchased exactly, starting with 1
• For each possible instance, called n, test if there exists non-negative integers a, b, and c, such that 6a+9b+20c = n. (This can be done by looking at all feasible combinations of a, b, and c)
• If not, n cannot be bought in exact quantity, save n
• When you have found six consecutive values of n that in fact pass the test of having an exact solution, the last answer that was saved (not the last value of n that had a solution) is the correct answer, since you know by the theorem that any amount larger can also be bought in exact quantity. Write an iterative program that finds the largest number of McNuggets that cannot be bought in exact quantity. Your program should print the answer in the following format (where the correct number is provided in place of (n)): “Largest number of McNuggets that cannot be bought in exact quantity: (n)”
Hint: your program should follow the outline above.
(The theorem referenced basically says that once you have six permissible values for n in a row, you can add six on to them indefinitely and there will be no more impermissible values for n.)"""

def largestNuggets():
    consecutive_count=0
    n=0
    largest_num=0
    while consecutive_count<6:
        n+=1
        if mcNuggets2(n)==True:
            consecutive_count+=1
        else:
            consecutive_count=0
            largest_num=n
    return largest_num
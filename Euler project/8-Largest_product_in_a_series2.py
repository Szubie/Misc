# -*- coding: utf-8 -*-

s="7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"


"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""

#My plan is: walk through the list on numbers, trying each combination. To try to make it more efficient, I might try a constantly updating list of the product, and the numbers that are being combined to make that product.
#As we go through the list, I simply cycle out the past numbers and include new ones (keeping the product up to date).

#I wonder if that's actually more efficient than simply recalculating it from scratch every time...?

#Ended up with the brute force method to start with. Let's try the other method in a new file.

key=12
highest_product=0
highest_product_nums=[]


current_numbers=[]
current_product=1

n=12
while n>=0:
    current_numbers.append(s[key-n])
    n-=1
for item in current_numbers:
    current_product=current_product*int(item)
    
if highest_product<current_product:
    highest_product=current_product
    highest_product_nums=list(current_numbers)       #This is the cause of all that grief. By explicity binding highest_product_nums to current_numbers (NOT A COPY OF IT, THE ACTUAL LIST, which is updated live, outside of a function), it continues to update along with the list.
    #To create a copy of a list, list(). Alternatively: new_list=old_list[:]
    
for n in range(12, len(s)-1):#Need the -1, else s[key] will go out of range (it will +1).
    current_product=1
    key+=1                   
    current_numbers.remove(current_numbers[0])
    current_numbers.append(s[key])
    #But you can't just divide the total by the value of the value being removed, nor can you just multiply it by the upcoming value. Otherwise you either divide by 0, or you can simply have 0 as the result once you've hit 0 a single time in the series.
    for item in current_numbers:
        current_product=current_product*int(item)
    if current_product>highest_product:
        highest_product=current_product
        highest_product_nums=list(current_numbers)
    
    print highest_product_nums #Is this a bug? wth? How can the highest_product be working, not changing, but the highest_product_nums change every time when they are on the same logic gate?
    print highest_product
        
print highest_product
print highest_product_nums
    
    
#Strange, this gives the right answer for the product, but the highest_numbers that it displays are wrong: they are just the last 13 numbers of the string.
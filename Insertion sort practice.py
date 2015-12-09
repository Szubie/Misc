#Coding insertion sort by memory.

def insert(x):
    """where x is a list of numbers, sort this list into ascending order"""
    #First, need to iterate over the length of the list, looking at each item.
    for num in range(1, len(x)):
            
    #To check each item, we need to hold the value of the item we are looking at. Save it. Every time.
        key=x[num]
        prev=num-1 #Checking the previous numbers.
    
    #We compare this value to each of the preceding numbers to find out where it fits. 
        while x[prev]>key and prev>=0: #Checking if the number is bigger. Also, making sure we don't go out of bounds of the list.
    #As we go, we keep shifting the index of each other number up by one to make room.
              
            x[prev+1]=x[prev] #Shift every item up one (don't worry, key saves the number "erased")
            prev-=1 #Keep moving backwards in the list to compare all items.
            
    #Then we insert it
        x[prev+1]=key
        #Insert it above the item that the above loop terminated on (since that means that the number ISN'T bigger than the key anymore)
        
a=[5, 2, 4, 6, 1, 3]
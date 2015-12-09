#Object oriented implementation, reusable.
#Reminding self how to implement classes: first define class name, that it's an object (or another class if you want to use inheritance).

class toDoList(object):
    def __init__(self):
        #Start by defining what is inside the class. In this case, an empty list (which we can add to or take away from later).
        self.list=[]
        self.categories=[]
        self.dict={}
        #Adding an empty dictionary to hold categories. The idea is to bind the string (as the key) to a list of items.
    def addItem(self, item):
        self.list.append(item)
        #will append "item" to end of the "list" found within "self". (append, inbuilt python method for lists.)
    def deleteItem(self, item):
        try:
            self.list.remove(item)
        except:
            return "No such item exists in the list!"
        #.remove is another inbuilt Python method for lists).
    def viewList(self):
        #self is still necessary here, as we are working within the class. So it knows where this is taking place.
        
        #return self.list
        
        #above works, returns a list though, all on the same line, brackets and quotes  included. Below will print out the text on different lines, without any quotation marks.
        for item in self.list:
            print item
        return None
    def modifyItem(self ,item):
        """takes a string input, if that string is in list, allow modification to that item?"""
        #We need to find the item though, in order to be able to alter it? And then bind the number of the item in that list.
        tracker=0
        length=len(self.list)
        while tracker<length:
            if self.list[tracker]==item:
                #Once found, promt the user to type what they want to replace the item with
                x=raw_input("What would you like this item to read as instead?  \n")
                self.list[tracker]=x
                return self.list
            else:
                #Otherwise, tracker increases (remember this, otherwise it won't move towards termination).
                tracker+=1
        return "The item you searched for was not in the list."
    
    def categoriseItem(self, item, category):
        """takes two arguments, the item, and the category (must be a string). Checks to see if item is in list: if not, throw an error. Then, checks to see if category exists in list yet: if not, adds it. Then, adds the two to dictionary
           The key is the category, which will return the item. Hopefully we can go through the dictionary and return all the values associated with a certain key."""
        if item in self.list:
            if str(category) not in self.categories:
                self.categories.append(category)
                self.dict={category: [item]}  
            else:
                self.dict[category].append(item) 
            print '"',str(item),'"',"added to the",str(category),"category." #It is now a part of ", x, "categories." How would you implement this? Have to have something that counts up. Additionally, how would you remove items from categories?
            return None
        else:
            return "The item could not be found within the list."
            
    def viewCategory(self, category):
        """returns a list of all things associated with that category"""
        try:
            print "---", category , "---" "\n", "\n", 
            for item in self.dict[category]:
                print item   
        except:
            print "No such category exists."
    def viewCategories(self):
        """returns a list of all the current categories in existance"""
        return self.categories
    
    def removeFromCategory(self, item, category):
        if item in self.dict[category]:
            #del self.dict[category]
            #This seems to delete both key and entry...
            self.dict[category].remove(item)
            
            
            #The above doesn't really work, it deletes everything, leaving the key to the dictionary with only a None value, not even an empty list (thus cannot append things to it later).
            
            
            #Now it wipes the list clean: if updating an item in list, any other item in the list will be lost. How can this be fixed?
            #You used the .remove() method for lists earlier in this very task! It seems perfectly suited for this situation.
            
            
            
            #This works, however, it also shifts the item that is updated to the end of the queue...Can you change this?
            #The result obtained from viewCategory is in the opposite order compared to the one obtained from viewList().
            
        else:            
            return "Either the item or the category does not exist"
            #There must be a way of discovering where exactly the error is: but how? Try and except?
            
            
    def updateItem(self, item, replacement):
        """takes two inputs, the item you want to change, and the thing that you want to change it into. Removes the old name, and replaces it with the new one."""
        n=0
        no=0
        while n<len(self.list):
            if self.list[n]==item:
                self.list[n]=replacement
                print "The item has now changed from",item,"to: ",replacement
                #Now has to search categories to change them? Find and replace. The below failed to do this. That's because it first checks for item in list: but the item in list has already been replaced.
                for c in self.categories:
                    if item in self.dict[c]:
                        #self.removeFromCategory(item, c)
                        #self.categoriseItem(replacement, c)
                        #The above "works", removes and replaces.
                        #self.dict[c]=replacement. Whoops, that didn't work.
                        while no<len(self.dict[c]):
                            if self.dict[c][no]==item:
                                self.dict[c][no]=replacement
                                break
                            else:
                                no+=1
                return None
            else:
                n+=1        
        else:
            print "No such item found."
            return None
    #The above works, however, it does not update the titles kept in categories.


#How would you make the program "retain state" despite shutting the computer down? This seems trickiest of all.
        
        
                
    #def categoriseItem(self, item, category):
    #    """takes two arguments, the item, and the category. Checks to see if item is in list: if not, throw an error. Then, checks to see if category exists in list yet: if not, adds it. Then, adds the two to dictionary
    #       The key is the category, which will return the item. Hopefully we can go through the dictionary and return all the values associated with a certain key."""
    #    if str(category) not in self.categories:
    #        self.categories.append(category)
    #    self.dict={category: item}
    #    #The above overrides the previous bindings for the dictionary. Start from scratch each time. Not reusable.
        
    
    
#    def categoriseItem(self, item, category):
#        #First, check to see if the category already exists.
#        if str(category) in self.categories:
#            #if it does, simply append the item to the list
#            self.createCategory(category).append(item)
#        else:
#            #otherwise, create the category as a list with item in it
#            self.category=category
#            self.c=self.createCategory(category)
#            self.c=[item]
            
            
            
    #Having huge trouble making it create a binding that actually uses the word input as category, rather than category itself...Won't accept str(category) as a binding to function call apparently. can't assign value to function call/
    #Problem side-stepped by using a different method to solve the problem: is there really no way to do this, though?





#def categoriseItem(self, item, category):
            #First, check to see if the category already exists in the dictionary. 
            #Problem with below approach? What if the value you want to check is in categories is there, but is not actually a category, but part of a list? Adding .keys() to check only the keys.
#        if category in self.categories.keys():
                #If it does, we just want to add the new item to the already existing list that is paired with the key in the dictionary.
                #you can't use lists AS KEYS within dictionaries because they are mutable: they can be changed. Can you use them as the value associated with a key though...? NOPE. "unhashable type: list"
#            self.categories.category.append(item)
#        else:
#                #If the category does not yet exist, we want to create it, using the category as a key, and pairing it with a list which contains the item.
#            self.categories+={category, item}        
#    def categoriseItem(self, item, category):
        #Need to design something that will attach categories to items...Also needs to be able to attach many categories to one item. (Dictionaries create only pairs?)
        
        #Going to try to create lists, with the first element of the list being the category title.
        
        #Sort of annoying that I can't call it with .(whatever category is), but only .c ... wonder if this is a serious issue? Yes it is, we are not creating multiple different lists for different categories here, only 1 big one.
#        c=category
        #Using "try" and then the route to take is error is encountered.
        #Try calling c, see if the list is already there. If not, create it.
#        try:
#            self.c
#        except:
#            self.c=[]
        
        #self.category[0]=c
        #Above is out of range: the list is empty after all! Instead, use append.
#            self.c.append(c)
        #However, using append means that if we call this method multiple times, there will be multiple useless category items in the list...Additionally, creating a new list every time in the method makes it impossible to reuse?
        
#        self.c.append(item)

        
        
todo1 = toDoList()
todo1.addItem("Take a shower.")
todo1.addItem("Go to work.")
todo1.viewList()
todo1.deleteItem("Take a shower.")
todo1.viewList()

todo1.addItem("Go home.")
todo1.categoriseItem("Go home.", "Life")
todo1.categoriseItem("Go to work.", "Life")
todo1.viewCategory("Life")

todo1.updateItem("Go home.", "Shower.")
todo1.viewCategory("Life")
todo1.viewList()


#The person on the website (http://www.reddit.com/r/dailyprogrammer/comments/39ws1x/20150615_challenge_218_easy_todo_list_part_1/) added inspirational quotes from Shia Lebeouff with everything!
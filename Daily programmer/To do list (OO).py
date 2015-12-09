#Object oriented implementation, reusable.
#Reminding self how to implement classes: first define class name, that it's an object (or another class if you want to use inheritance).

class toDoList(object):
    def __init__(self):
        #Start by defining what is inside the class. In this case, an empty list (which we can add to or take away from later).
        self.list=[]
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
        
todo1 = toDoList()
todo1.addItem("Take a shower.")
todo1.addItem("Go to work.")
todo1.viewList()
todo1.deleteItem("Take a shower.")
todo1.viewList()

#The person on the website (http://www.reddit.com/r/dailyprogrammer/comments/39ws1x/20150615_challenge_218_easy_todo_list_part_1/) added inspirational quotes from Shia Lebeouff with everything!
#Classes are a way of building up further layers of abstraction. We don't have to worry about the inner workings of something when we invoke it, just how we can use it.
#Everything is an object, and there are certain ways that we are allowed to manipulate them, by using the methods associated with them.
#For example, using the method ".append" to add something to the end of a list.

#An advantage of object orientated programming is that it is easy to separately test and debug parts of the code as they are all in separate instances and cannot interfere with each other.
#The division between the inner workings of something and the way you interact with it allows the programmer to ignore how something works, and focus instead on its application. The user interface provided tells you how you can interact.

class Coordinate(object):
    #Creates a new class "Coordinate", which is a "subclass" of the "superclass" "object".
    def __init__(self, x, y):
    # The __init__ method is called whenever an object is created. It is short for "initiliazation".
    #With this step we define what is inside the instance created when we make this new class. Must reference self first, which points to the instance location. Two underscores on each side __init__
    #Then, it selects what information to store.
        self.x = x
        self.y = y
    #self.x tells python to go inside of self (the new instance pointed to by self) and then, within that instance, to bind the value of x there.
    #the "." operator is used to access an attribute of an object.
    
    #When accessing attributes for an instance, first it checks the definitions provided within the class, then it refers to the "super-class" and then finally to the global environment.
    #Thus, if there was no __init__  function defined within the class, Python would have then searched for an __init__ function within the superclass of "object", and then finally, (if there was not one in the super-class), it would look in the global environment.
    #This is true for methods, and also for values! E.g. searching for a binding for "x".
    
    
    #Data attributes of an instances are often called "instance variables". There are two instance variables in this class (self.x, self.y).
    
c = Coordinate(3,4)
origin = Coordinate(0,0)
#The above are defined in the global environment.
# c is bound to an instance of Coordinate, which has the values in brackets bound to x and y. (self is not necessary to reproduce when feeding information into the new frame, Python does it automatically).

#origin also calls Coordinate, and thus it also creates a new frame, separately. A new instance. No confusion possible.
print c.x, origin.x

#This will print "3 0". It prints the value of x found inside c (which is 3), and then the one found inside origin (which is 0).


#You can even access the __init__ method through "c" if you wanted to, as it has access to the same chain.
#THIS BREAKS THINGS A BIT, but it's interesting to see what will happen.
#c.__init__(5, 6)
#binds the values of x and y within c to new values (in this version of Python anyway, sometimes it might create a new version with these new figures, it depends)
#Now, if you call for c.x, it will return "5", rather than "3".
#Bear in mind, this means that you have overwritten the old value of x within c that was provided within the global environment and thus can break things! 


#It is common for the parameters of __init__ to have the same names as the attributes. The statement
#
#        self.hour = hour
#
#stores the value of the parameter hour as an attribute of self. 


class Address(object):
    def __init__(self, number, streetName):
        self.number = number
        # Line 1: Creating a number attribute
        self.streetName = streetName
        # Line 2: Creating a streetName attribute  
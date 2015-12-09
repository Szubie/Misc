class Coordinate(object):

    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
        
c = Coordinate(3,4)
origin = Coordinate(0,0)

#interestingly, asking for "print c" does not return anything very useful: instead it tells you the type of the object and its location in memory.
#print c
#<__main__.Coordinate object at 0x0000000009840470>
#also says that it was was an instance that came under the global enviroment (__main__.Coordinate)

#The way to get around this is to define another special method (as designated by the double underscores surrounding it?) within the class: def __str__(self)

#We are overriding the underlying __str__ method that is within the superclass "object" with this __str__ method that is defined within the class.


#If we ask for the type of "c" with ">>> print type(c)" we get:
#<class '__main__.Coordinate'>

#Tells us that is is a class first, then the class definition of which it is an instance. A class bound in the global environment (under __main__.) and that its name is "Coordinate".
#Thus, it tells us that "c" is an instance of the class "Coordinate", which makes sense.

#This makes sense. If we ask for ">>> print Coordinate, type(Coordinate)" we get:
#<class '__main__.Coordinate'> <type 'type'>

#says it is a class under main called Coordinate, and that its type is a version of a "type".



#A built-in function provided to us by Python: "isinstance()" (is (in) instance) will check if an object is a Coordinate.
# >>> print isinstance(c, Coordinate)
#returns "True".


#So far we have been looking at how to override existing base methods, those marked by the double underbars on each side (__str__ ,  __init__ )
#We can also make our own brand new methods.
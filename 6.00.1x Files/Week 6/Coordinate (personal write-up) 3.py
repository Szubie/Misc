class Coordinate(object):

    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
    #our new attribute defined below, novel, not overriding a base method.
    def distance(self, other):
        return math.sqrt(sq(self.x - other.x) + sq(self.y - other.y))
    #The above assumes that we have loaded the math module into our session of Python. Designed to calculate the distance between two points. (Simply uses pythagorus theorem)
    #Points to self first, and then another argument "other". 
    
    #To use this: (?)
    #c.distance(origin)
    
    #We can invoke the method of Coordinate through "c", which is an instance of Coordinate with some values supplied. This is how we can compare or combine two different sets of values with a method that is defined within the class.
    
c = Coordinate(3,4)
origin = Coordinate(0,0)

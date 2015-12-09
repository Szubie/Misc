class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    #Add an __eq__ method that returns True if the Coordinates refer to the same point on the plane.
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    #c = Coordinate(0,0)
    #origin = Coordinate(0,0)

    #With the above values, c.__eq__(origin) is True.
    
    def __repr__(self):
        return str("Coordinate(" + str(self.getX()) + ", " + str(self.getY()) + ")")
    #Above is written to return the code that it runs on?
    #Define __repr__, a special method that returns a string that looks like a valid Python expression that could be used to recreate an object with the same value. In other words, eval(repr(c)) == c given the definition of __eq__ from part 1.

    #It does actually work. However, calling c.__repr__ returns only: <bound method Coordinate.__repr__ of Coordinate(0, 0)>
    # To utilise repr you must write: >>> print repr(c)
    # returns: Coordinate(0, 0)


c = Coordinate(0,0)
origin = Coordinate(0,0)

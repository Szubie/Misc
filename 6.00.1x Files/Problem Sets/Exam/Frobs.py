# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
    
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """  
    name = atMe.myName()
    name2 = newFrob.myName()
    before = atMe.getBefore()
    after = atMe.getAfter()
    if name == name2:
        if before == None:
            newFrob.setAfter(atMe)
            atMe.setBefore(newFrob)
        elif after == None:
            newFrob.setBefore(atMe)
            atMe.setAfter(newFrob)
        else:
            newFrob.setBefore(atMe.getBefore())
            atMe.getBefore().setAfter(newFrob)
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
    if name>name2:
        if before == None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        elif before.myName()<name2:
            newFrob.setBefore(before)
            #sketchy below
            before.setAfter(newFrob)
            newFrob.setAfter(atMe)
            atMe.setBefore(newFrob)
        elif before.myName() >name2:
            return insert(before, newFrob)
        elif before.myName() == name2:
            atMe.setBefore(newFrob)
            newFrob.setBefore(before)
            before.setAfter(newFrob)
            newFrob.setAfter(atMe)
        #return insert(after, name2)
        #name.setBefore(name2)
    if name2>name:
        if after == None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        elif after.myName()<name2:            
            return insert(after, newFrob)
        elif after.myName() >name2:
            newFrob.setAfter(after)
            #sketchy below
            after.setBefore(newFrob)
            newFrob.setBefore(atMe)
            atMe.setAfter(newFrob)
        elif after.myName() == name2:
            atMe.setAfter(newFrob)
            newFrob.setAfter(after)
            after.setBefore(newFrob)
            newFrob.setBefore(atMe)
        #return insert(before, name2)
        #name2.setBefore(name). This stuff didn't work, it wasn't actually linking INSTANCES of the class together, just strings of their names.
    
def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    #Must be done recursively
    if start.getBefore() == None:
        return start
    return findFront(start.getBefore())
                        
#Test suite below:

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')


insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)

findFront(martha)
#insert(eric, Frob('martha'))

###

#insert(eric, Frob("eric"))
#insert(eric, Frob("chris"))
#insert(eric, Frob("john"))
#insert(eric, Frob("john"))
#insert(eric, Frob("chris"))
#insert(eric, Frob("eric"))
#insert(eric, Frob("john"))
#insert(eric, Frob("chris"))

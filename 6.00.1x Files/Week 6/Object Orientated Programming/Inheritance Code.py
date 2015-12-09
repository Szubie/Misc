import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
        #String split looks very cool and potentially useful.

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's ame is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    # __lt__ refers to the method that python calls when the "<" symbol is used. firstElement.__lt__(secondElement)
    #Thus, by defining our own __lt__ function we can determine what exactly happens when we use the "<" symbol.

    def __str__(self):
        """return self's name"""
        return self.name

# me = Person("William Eric Grimson")
# print me
# foo = 'William Eric Grimson'
# foo.split(' ')
# foo.split(' ')[-1]
# me.getLastName()
#
# me.setBirthday(1,2,1927)
# me.getAge()
#
# her = Person("Cher")
# her.getLastName()
# plist = [me, her]
# for p in plist: print p
# plist.sort()
# for p in plist: print p
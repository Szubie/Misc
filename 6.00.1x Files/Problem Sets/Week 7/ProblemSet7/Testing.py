class NewsStory(object):
    def __init__(self, Guid, Title, Subject, Summary, Link):
        #have to remember the __init__ method (function?), and that it must first refer to "self"
        self.Guid = Guid
        self.Title = Title
        self.Subject = Subject
        self.Summary = Summary
        self.Link = Link
    
    def getGuid(self):
        return self.Guid
    
    def getTitle(self):
        return self.Title
        
    def getSubject(self):
        return self.Subject
        
    def getSummary(self):
        return self.Summary
        
    def getLink(self):
        return self.Link

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# WordTrigger
class WordTrigger(Trigger):
    #WordTrigger is an abstract class: has 3 other classes that inherit from it.
    def __init__(self, myWord):
        """takes in one argument, word, a string"""
        self.myWord = myWord
    def isWordIn(self, text):
        """takes one string argument, text. Returns True if word is in text, False otherwise. Method is not case-sensitive."""
        temp = text
        temp2 = ""
        temp = temp.lower()
        for c in temp:
            if c in """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""":
                c = " "
            temp2 += c
        temp2 = temp2.split()


        if self.myWord.lower() in temp2:
            return True
        else:
            return False

class SummaryTrigger(WordTrigger):
    def evaluate(self, text):
        temp = text.getSummary()
        return self.isWordIn(temp)

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, aTrigger):
        """Takes a Trigger as an argument, and gives the reverse result. Method to use is: notTrigger.evaluate(x)"""
        self.aTrigger = aTrigger
    def evaluate(self, text):
        temp = self.aTrigger
        temp = temp.evaluate(text)
        if temp == True:
            return False
        else:
            return True

koala     = NewsStory('', '', '', 'Koala bears are soft and cuddly', '')
s2  = SummaryTrigger('soft')

n = NotTrigger(s2)
n.evaluate(koala)
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
class PhraseTrigger(Trigger):
    def __init__(self, Phrase):
        self.Phrase = Phrase
    def evaluate(self, text):
        text = text
        myTitle = text.getTitle()
        mySummary = text.getSummary()
        mySubject = text.getSubject()
        if self.Phrase in myTitle:
            return True
        if self.Phrase in mySummary:
            return True
        if self.Phrase in mySubject:
            return True
        else:
            return False
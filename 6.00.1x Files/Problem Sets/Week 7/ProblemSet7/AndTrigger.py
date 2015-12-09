class AndTrigger (Trigger):
    """This trigger should take two triggers as arguments to its constructor, and should fire on a news story only if both of the inputted triggers would fire on that item."""
    def __init__(self, aTrigger, bTrigger):
        self.aTrigger = aTrigger
        self.bTrigger = bTrigger
    def evaluate(self, text):
        temp = self.aTrigger
        temp = temp.evaluate(text)
        temp2 = self.bTrigger
        temp2 = temp2.evaluate(text)
        if temp and temp2 == True:
            return True
        else:
            return False
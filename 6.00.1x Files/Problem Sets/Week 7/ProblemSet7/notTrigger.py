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
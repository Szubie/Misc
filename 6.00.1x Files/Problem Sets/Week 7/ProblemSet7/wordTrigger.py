class WordTrigger(object):
    #WordTrigger is an abstract class: has 3 other classes that inherit from it.
    def __init__(self, word):
        """takes in one argument, word, a string"""
        self.word = word
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


        if self.word in temp2:
            return True
        else:
            return False
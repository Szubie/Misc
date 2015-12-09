# 6.00.1x Problem Set 7
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 7

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# NewsStory

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

#======================
# Part 2
# Triggers
#======================

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

# TitleTrigger
class TitleTrigger(WordTrigger):
    def evaluate(self, text):
        temp = text.getTitle()
        return self.isWordIn(temp)
        #YOU MUST "RETURN" A RESULT IN A FUNCTION OR YOU WILL ONLY GET A "NONE".
        
# SubjectTrigger
class SubjectTrigger(WordTrigger):
    def evaluate(self, text):
        temp = text.getSubject()
        return self.isWordIn(temp)

# SummaryTrigger
class SummaryTrigger(WordTrigger):
    def evaluate(self, text):
        temp = text.getSummary()
        return self.isWordIn(temp)

# Composite Triggers
# Problems 6-8

# NotTrigger
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
        
# AndTrigger
class AndTrigger(Trigger):
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
            
# OrTrigger
class OrTrigger(Trigger):
    """This trigger should take two triggers as arguments to its constructor, and should fire on a news story only if both of the inputted triggers would fire on that item."""
    def __init__(self, aTrigger, bTrigger):
        self.aTrigger = aTrigger
        self.bTrigger = bTrigger
    def evaluate(self, text):
        temp = self.aTrigger
        temp = temp.evaluate(text)
        temp2 = self.bTrigger
        temp2 = temp2.evaluate(text)
        if temp or temp2 == True:
            return True
        else:
            return False

# Phrase Trigger
# Question 9

# PhraseTrigger
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

#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    relevantStories = []
    for s in stories:
        for t in triggerlist:
            result = t.evaluate(s)
            if result == True:
                if s not in relevantStories:
                    relevantStories.append(s)
    return relevantStories
            

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    str2 = " "
    if triggerType == "TITLE":
        TriggerType = TitleTrigger
    if triggerType == "SUBJECT":
        TriggerType = SubjectTrigger
    if triggerType == "SUMMARY":
        TriggerType = SummaryTrigger
    if triggerType == "PHRASE":
        TriggerType = PhraseTrigger
    if triggerType == "NOT":
        TriggerType = NotTrigger
        triggerMap[name] = TriggerType(triggerMap[params[0]])
        #Have to return the Trigger itself, not the string name. Same with below.
        return triggerMap[name]
    if triggerType == "AND":
        TriggerType = AndTrigger
        triggerMap[name] = TriggerType(triggerMap[params[0]] , triggerMap[params[1]])
        return triggerMap[name]
    if triggerType == "OR":
        TriggerType = OrTrigger
        triggerMap[name] = TriggerType(triggerMap[params[0]] , triggerMap[params[1]])
        return triggerMap[name]
    triggerMap[name] = TriggerType(str2.join(params))
    return triggerMap[name]


def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        triggerlist = readTriggerConfig("C:/Users/Benjy/Dropbox/Python/6.00.1x Files/Problem Sets/Week 7/ProblemSet7/triggers.txt")

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()


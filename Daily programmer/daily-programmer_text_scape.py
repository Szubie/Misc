import praw
r = praw.Reddit(user_agent='PyBot 0.1')
subreddit = r.get_subreddit("dailyprogrammer")
for submission in subreddit.get_hot(limit = 750):
print "Title: ", submission.title.encode('utf-8')
print "Text: ", submission.selftext.encode('utf-8')
print    "**************************************************************************************************************************\n"

"""This is the code someone used to grab all the "Daily Programming" challenges from the sub-reddit."""
""" Made available on GitHub as well: https://github.com/TheEd1tor/dp_easy/blob/master/NewEasy.txt """
import string
PATH_TO_FILE = 'words.txt'

def loadWords():
	inFile = open("C:/Users/Benjy/Documents/Computer Science/loadWords", 'r', 0)
	line = inFile.readline()
	wordlist = string.split(line)
	print "  ", len(wordlist), "words loaded."
	return wordlist

loadWords()

 #Uncomment the following function if you want to try the code template
def loadWords2():
 	try:
 		inFile = open(PATH_TO_FILE, 'r', 0)
 	except IOError:
 	    #IOError is Input/Output error.
 	    #Only want an exception for this tpye of error, not all errors! So it is better to specify the kind of error you are handling.  
 		print "The wordlist doesn't exist; using some fruits for now"
 		return ['apple', 'orange', 'pear', 'lime', 'lemon', 'grape', 'pineapple']
 	line = inFile.readline()
 	wordlist = string.split(line)
 	#wordlist = string.split(line, ",")
 	#or:
 	#wordlist = line.split(",")
 	print "  ", len(wordlist), "words loaded."
 	return wordlist
PATH_TO_FILE = 'words2.txt'
loadWords2()
PATH_TO_FILE = 'doesntExist.txt'
loadWords2()

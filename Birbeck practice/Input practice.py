#Code is run through a "compiler", software which checks that the syntax is correct. When all syntax is correct, the program will successfully compile. Now you have an executable version of the program.


#Input=>Output


#print "Please enter a word:"
#word=raw_input()
#print "The word was: ", word

#Works, spaces around though.



#word=raw_input("Please enter a word: ")
#print "The word was: ", word

#works better.


#word1=raw_input("Please enter a word: ")
#word2=raw_input("Please enter another word: ")
#print word2, word1

#Above is easier, takes two different inputs. How to do it with only one input?

#wordList=[]
#words=raw_input("Please enter two words: ")
#wordList=words.strip().split()
#print wordList[1],',', wordList[0]
#wordList[1]=wordList[1].join(",")

#print wordList[1],wordList[1].join(","), wordList[0]
#Above works, no punctuation stripped though, and no comma atm.

#How to join comma to the end of the word?

#wordList[1]=wordList[1]+","
#(adding strings together"



wordList=[]
#INITIALISING wordList. Assigning it to nothing. Will later overwrite to give it a real value.
words=raw_input("Please enter two words: ")
wordList=words.strip().split()
print wordList[1]
print wordList[0]
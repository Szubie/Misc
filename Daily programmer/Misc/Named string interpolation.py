names = ["Ben", "Tom", "Charlie", "Eve", "David", "Michelle", "Kong"]

new_message = '''

This is a new message to %s. %s cannot make it to work today. %s has a cold so %s is now in charge and %s has decided that %s is staying home. 

''' % (names[1], names[4], names[5], names[6],names[0], names[3])

#Try this:

#"%(name)s , %(name)s" % { "name": "foobar" }

#Edit: sorry I didn't really answered your question correctly, but using a dictrionnary/map will solve your issue, you can now write:

#This a new message to %(to)s. %(from)s connot make it to work today. %(from)s has a cold so %(in_charge)s is now in charge...

#and you just have to provide a map with the relevant keys filled accordingly...

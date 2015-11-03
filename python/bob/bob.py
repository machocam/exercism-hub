#
# Skeleton file for the Python "Bob" exercise.
#
import re
what = 'WHAT THE HELL WERE YOU THINKING?'
def hey(what):
	what = no_trailing_chars(what)
	if re.search('!$' , what):
		print 'Whoa, chill out!'
	elif re.search('\?$' , what):
		print "Sure."
	elif what == "": 
		print 'Fine. Be that way!'
	else :
		print "Whatever."

def no_trailing_chars(phrase):
	if len(phrase)>1:
		while (phrase[len(phrase)-1] == " "):
			phrase = phrase [:-1]		
	return phrase



	 

  

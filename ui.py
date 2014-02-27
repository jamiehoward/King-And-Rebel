import os

def clear():
	os.system("clear")

def display_menu(title, options, prompt):
	clear()
	if (prompt is None):
		prompt = "Selection: "
	print "════════" + title + "════════"
	i = 1
	for (option in options):
		print "   " + str(i) + ". " + option
		i = i+1
	userInput = raw_input(prompt)
	return userInput
   	


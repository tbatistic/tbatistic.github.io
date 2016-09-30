'''
Project: Story
Name: Tyler Batistic 
	  Therese Do
'''
import time

#Plays a story with a plot twist in each choice.
def story():
	print ("You're walking home from school one day and you get lost in the woods.  Go through:") 
	print ("#1. The sunlit path with birds?") 
	print ("#2. through the darkened path with dead trees?")
	path = input("> ")
	if path == "1":
		print ("You wander farther into the woods and encounter a small cabin.")
		print ("#1. Continue walking the lit path?")
		print ("#2. Enter the cabin?")
		cabin = input("> ")
		if cabin == "1":
			print("You find Slenderman and die. The End...?")
		elif cabin == "2":
			print("You get eaten by the big bad wolf.  The End...?")
		else:
			print ("You get lost forever. The End...?")
	elif path == "2":
		print ("You wander farther into the woods and encounter a small cave.")
		print ("#1. Continue walking the dark path?")
		print ("#2. Enter the cave?")
		cave = input("> ")
		if cave == "2":
			print ("You have tea and cookies with your grandmother. You live happily ever after...?")
		elif cave == "1":
			print ("You find your fairy godmother and your wishes come true!  You live happily ever after...?")
		else:
			print ("You get lost forever.  The End...?")
	else:
		print ("You get lost forever. The End...?")

#True ending
def ending():
	print ("")
	print ("You decide to break out of the narrative and make your own decision. What do you do?")
	choice = input("> ")
	print ("You", choice)
	print ("Thanks for playing!")

story()
time.sleep(.75)
ending()
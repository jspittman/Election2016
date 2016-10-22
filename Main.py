##						##				
##    A fun text based 2016 election game 	##
##    Feel free to customise for yourself!	##
##						##

import time # why you punish me - Hootie

print "//////// ELECTION 2016 //////////\n\n"
time.sleep(1)
print "Where your Vote Matters!\n"
time.sleep(.5)
print "Let's get right to it\n"
time.sleep(.3)
print "Who are you voting for this year?"
print """
Hillary Clinton
Gary Johnson
Donald Trump
Jill Stein
"""

print "Got one in mind?\n"
print "Alright, let's roll\n"


clintonyes	= "Clinton Suxxx"
clintonno	= "Cool, keep researching.  Good luck!"
johnsonyes  	= "Well you are one smart cookie!  Now go smoke a bowl!"
johnsonno	= "Well, better get sure because he's awesome!"
trumpyes 	= "Trump big man"
trumpno  	= "OK, that's probably good.  Who knows what the guy would do."
steinyes 	= "Going green is always good :)"
steinno  	= "That's ok-  Keep on looking."

var = 1

while (var == 1):
	answer = raw_input("Please Select Your Next President:\n\n\t\t1 = Clinton\n\t\t2 = Johnson\n\t\t3 = Trump\n\t\t4 = Stein\n ---> ")
	
	if answer in ("Clinton", "c", "C", "1"):
		print "\nClinton, huh?\n"
		time.sleep(.75)
		answer1 = raw_input("Are you sure?")
		if answer1 in ("Yes", "yes", "Y", "y"):
			print "You can't be serious."
			time.sleep(.75)
			answeremails = raw_input("You -do- remember the emails?")
			if answeremails in ("Yes", "yes", "Y", "y"):
				print "But, but, but"
				time.sleep(.5)
				answer2 = raw_input("Wait, Are You Sure You Don't Want to Reconsider?")
			elif answeremails in ("No", "no", "N", "n"):
					print "Go google the Clinton Email Scandel...then come back :)"
					break
			if answer2 in ("No", "no", "N", "n"):
				print "OK, I'll just put your vote in the round filing cabinet then"
				break
			else:
				print "OK, I'll just put your vote in the round filing cabinet then"
				break
		if answer1 in ("yes", "y"):
			print "Cool!"
			break
		if answer1 in ("No", "no", "n", "naw"):
			print clintonno
			break
		else:
			print "\nThat answer is unacceptable.  You are deplorable.  Try again\n\n"
			time.sleep(.5)
			
	elif answer in ("Johnson", "j", "J", "2"):
		print "\nJohnson, huh?"
		time.sleep(.75)
		answer1 = raw_input("\nAre you sure?")
		if answer1 in ("Yes", "yes", "y"):
			print johnsonyes
			break
		if answer1 in ("No", "no", "n"):
			print johnsonno
			break
		else:
			print "\nAre you high?  Keep trying\n\n"
			time.sleep(.5)

	elif answer in ("Trump", "t", "T", "3"):
		print "\nTrump, huh?"
		time.sleep(.75)
		answer1 = raw_input("Are you sure?")
		if answer1 == "Yes":
			print "Cool!"
			break
		if answer1 == "yes":
			print "Cool!"
			break
		if answer1 == "No":
			print trumpno
			break
		if answer1 == "no":
			print trumpno
			break
		else:
			print "\nHelp Make American Great Again.  Keep trying\n\n"
			time.sleep(.5)
			
			
	elif answer in ("Stein", "s", "S","4"):
		print "\nStein, huh?"
		time.sleep(.75)
		answer1 = raw_input("Are you sure?")
		if answer1 == "Yes":
			print "It's good to be green :)"
			break
		if answer1 == "yes":
			print "It's good to be green :)"
			break
		if answer1 == "y":
			print "It's good to be green :)"
			break
		if answer1 == "No" + "n":
			print steinno
			break
		if answer1 == "no":
			print steinno
			break
		if answer1 == "n":
			print steinno
			break
		else:
			print "\nSwing and a whiff.  Try again\n\n"
			time.sleep(.5)
			
	else :
		print "None of these match!  Common this is important. Try again.\n"
		time.sleep(.5)
		
#	thanks for playing!	#




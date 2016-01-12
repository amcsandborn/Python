##############
# File: ex36.py
# Date: October 9, 2014
# Author: Avery Sandborn
##############

# mode function: asks you what mode you want to play in
def mode():
	print "\nWhat mode do you want to play in?"
	print "\t1) Adventure Mode"
	print "\t2) Hodor Mode"
	choice = raw_input("> ")
	
	# If choice = 1, start game.
	if choice == "1":
		start()
		
	# if choice = 2, run hodor function
	elif choice == "2":
		hodor()
	
	# if user entered incorrect entry, run dead function
	else:
		dead("\nHow are you already dead?")

# Start function starts the game and explains the rules, ask user for input
def start():
	print "\nYou awake in a strange, cold land, with only one lit torch."
	print "There is a spooky forest to the north, and a large wall to the south."
	print "There are dead bodies all around you."
	print "What do you do?"
	print "\t1) Head North into the forest."
	print "\t2) Head South to the wall. Maybe you can find your way to the \n\t   other side."
	print "\t3) Stay put, and burn the bodies. All of them!"
	choice = raw_input("> ")
	
	# If user chose 1, run dead function
	if choice == "1":
		print "\nYou wander around the forest, until you run into a large army of White Walkers."
		dead("\nThey kill you and you turn into a clumsy wight with rotting flesh. You die.")
	
	# If user chose 2, ask for user input
	elif choice == "2":
		print "\nYou wander to the wall and look for an entrance."
		print "All of a sudden, you hear footsteps behind you."
		print "The dead bodies you left behind have awoken, and are hungry for humans."
		print "What do you do?"
		print "\t1) Use your torch as a weapon, and burn every one of them."
		print "\t2) Fight them with your fists. You can take them!"
		choice = raw_input("> ")
		
		# If user chose 1, run the wall function
		if choice == "1":
			print "\nAfter you've burnt all of the bodies, you turn your attention back to the wall."
			wall()
		
		# If user chose 2, run dead function
		elif choice == "2":
			print "\nYou manage to knock out a few zombies with your mad fighting skills."
			print "But there are too many of them, and the ones you knock out"
			print "keep coming back to life."
			print "You die a painful death."
			dead("\nYou've turned into a clumsy wight with rotting flesh. You die.")
		
		# if user chose something else, run dead function
		else:
			dead("\nYou are a hopeless child that doesn't know right from left. You die.")
	
	# if user chose 3, run wall function
	elif choice == "3":
		print "\nAfter you've burnt the bodies, you wander to the wall."
		wall()
	
	# if user chose something else, run dead function
	else:
		dead("\nYou are a hopeless child that doesn't know right from left. You die.")

# hodor function: Hodor Hodor Hodor Hodor.
def hodor():
	print "\nHodor hodor hodor hodor hodor."
	print "Hodor hodor hodor hodor hodor hodor hodor hodor."
	print "Hodor hodor hodor hodor hodor. Hodor hodor, hodor hodor. Hodor!"
	print "Hodor hodor hodor hodor hodor hodor hodor hodor."
	print "Hodor hodor hodor hodor!"
	print "Hodor hodor hodor hodor hodor hodor, hodor."
	print "Hodor, hodor hodor. Hodor."
	print "Hodor hodor hodor hodor?"
	print "\t1) Hodor hodor."
	print "\t2) Hodor hodor hodor."
	choice = raw_input("> ")
	
	if choice == "1" or choice == "2":
		hodor()
	
	else:
		print "\nEverybody loves Hodor!"
		dead("\nBut now I'll allow you to play Adventure Mode.")
		
# Dead function: Tells you why you died, asks if you want to start again
def dead(death):
	print death ; print ""
	print "Do you want to try again?" 
	print "\t1) Yes"
	print "\t2) No"
	choice = raw_input("> ")
	
	# if user wants to start again, run start function
	if choice == "1":
		start()
	
	# if user does NOT want to start again, run the exit function.
	else:
		print "\nGood bye!\n"
		exit(0)

# Mottos function: put house mottos in a list
def mottos():
	motto_list = ["1) As High as Honor","2) Ours is the Fury","3) We Do Not Sow","4) Hear me Roar","5) Unbowed, Unbent, Unbroken","6) Winter is Coming","7) Fire and Blood","8) Family, Duty, Honor","9) Growing Strong"]
	
	# for each motto, print it with a tab
	for i in motto_list:
		print "\t%s" % i
	
# Wall function: asks for user input
def wall():
	print "\nYou find two ice picks on the ground and make your way up the wall."
	print "At the top of the wall, you find Jon Snow."
	print "He asks you what business you have over the wall."
	
	# while loop, run mottos function, and ask user for input
	while True:
		print "What do you say?"
		mottos()
		choice = raw_input("> ")
	
		# If user chose choice 6, break the while loop and go to the twins function
		if choice == "6":
			twins()
			break
	
		# If user chose another option, run the while loop again
		elif choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "7" or choice == "8" or choice == "9":
			print "\nJon Snow denies you access to the South."
			print "You rethink your decision and say something else."
	
		# if user chose something else, run dead function
		else:
			dead("\nYou are a hopeless child that doesn't know right from left. You die.")	

# Twins Function: run mottos function, and ask user for input
def twins():
	print "\nJon Snow allows you to pass the wall after proving your loyalty to House Stark."
	print "However, you have no idea why you said what you said."
	print "Once you're over the wall, and far enough away, you shout:"
	print "\t\"You know nothing, Jon Snow!\""
	print "\nYou make your way south, and find the The Twins in the Riverlands."
	print "A guard stops you from entering the castle."
	print "What do you say?"
	mottos()
	choice = raw_input("> ")
		
	# If the user chose 6, run ask for user input
	if choice == "6":
		print "\nThe guard smirks."
		print "He tells you that there is a wedding, and you're invited."
		print "What do you do?"
		print "\t1) Tell the guard you have no gift, but that you'd love to celebrate \n\t   the happy couple. You go in the castle."
		print "\t2) Run away in fear!"
		choice = raw_input("> ")
			
		# If user chose 1: run dead function
		if choice == "1":
			print "\nYou sit in an open seat in the castle."
			print "\nAfter the wedding, you stuff your face with pigeon pie."
			print "The chamber ensemble begins playing the Rains of Castamere."
			print "The Freys pull out their crossbows and murder every single one of you."
			print "And you didn't even get to lick the frosting off the last lemon cake."
			dead("\nYes now the rains weep o'er his hall, and not a soul to hear. You die.")
			
		# If user chose 2: run dead function
		elif choice == "2":
			print "\nYou try to run away but another guard catches you."
			print "He forces you to take a seat at the wedding."
			print "You shiver with fear as the wedding \"celebration\" begins."
			print "Before you know it, the Freys have murdered every single one of you."
			print "Fortunately, they burn your bodies, and you can rest in peace \nwithout fear of being turned into a clumsy wight with rotting flesh."
			dead("\nDon't you know never to go to weddings? You die.")
			
		# if user chose something else, run dead function			
		else:
			dead("\nYou are a hopeless child that doesn't know right from left. You die.")	
		
	# if user chose 4, 
	elif choice == "4":
		print "\nThe guard pulls a knife out of his pocket and hands it to you and says: \n\t\"A Lannister always pays his debts...\""
		print "\nYou go into the castle."
		print "You sit in the back, waiting for the drama to ensue."
		print "You hear the Rains of Castamere begin to faintly play."
		print "You see some items being thrown accross the room."
		print "It seemed a friendly food fight was starting."
		print "But then some crossbows and daggers come your way."
		print "You run out of the castle without a scratch."
		journey()
		
	# if user chose something else, 
	elif choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "8" or choice == "9":
		print "\nThe guard sighs and says: \n\t\"Scram, peasant... you're not invited."
		print "You shrug and walk away."
		journey()
		
	# if user chose something else, run dead function	
	else:
		dead("\nYou are a hopeless child that doesn't know right from left. You die.")	

# Journey function: ask for user input		
def journey():
	print "\nYou hear fighting ensue as you walk away from the castle, \nand breathe a sign of relief that you are unharmed."
	print "\nAfter a few days hike, you run into a young girl who calls herself Arya."
	print "Do you trust her?"
	print "\t1) Yes, and you decide to travel with her to \n\t   where ever the hell she's going."
	print "\t2) Not sure, so you continue on your journey in hopes of \n\t   finding people who won't kill you."
	print "\t3) Absolutely not, and you decide to throw her off the cliff."
	choice = raw_input("> ")
	
	# If you choose choice 1, run arya function
	if choice == "1":
		print "\nYou and Arya continue walking, when you find a pointy stick."
		print "Arya acts as your dancing teacher for the remainder of the trip."
		print "Remember kids, stick 'em with the pointy end!"
		arya()
		
	# if user chose 2, run the eyrie function
	elif choice == "2":
		print "\nYou part ways with Arya, and she tells you that the Eyrie is not far ahead."
		eyrie()
	
	# if user chose 3, run dead function
	elif choice == "3":
		print "\nShe pulls out Needle and slowly sheathes it into your neck."
		dead("The last thing Arya tells you: \n\t\"Fine little blade; maybe I'll pick my teeth with it.\"")	
	
	# if user chose something else, run dead function
	else: 
		dead("\nYou are a hopeless child that doesn't know right from left. You die.")	

# Arya function: ask for user input
def arya():
	print "\nYou and Arya find a ship captain."
	print "You are low on food and water, and getting a ride on the ship \nseems to be the only way you'll survive."
	print "He tells you that there is no room for you peasants."
	
	# while loop, ask user for input, until they pick right.
	while True:
		print "What do you do?"
		print "\t1) Sneak onto the ship when he's not looking."
		print "\t2) Pull out your pointy stick and demand that he serve you." 
		print "\t3) Make some gibberish words up and \n\t   act like you don't speak his language."
		choice = raw_input("> ")
	
		# If user chose 1 or 2, run dead function
		if choice == "1" or choice == "2":
			print "\nWho do you think you are?"
			print "The ship captain snaps your new stick in half and refuses to help you."
			print "You and Arya brainstorm ways to get on that ship."
	
		# if user chose 3, run essos function
		elif choice == "3":
			print "\nSome how, some way, the words that came out of your mouth \nmade the ship captain happy and bow down to you."
			print "Who knew some made up words like \"Valar Morghulis\" would be so powerful?"
			essos()
			break
			
		# if user chose something else, run dead function	
		else: 
			dead("\nYou are a hopeless child that doesn't know right from left. You die.")	

# eyrie function: ask for user input
def eyrie():
	print "\nYou reach the Eyrie where Tyrion is on Trial."
	print "Lysa Tully asks you if you will volunteer for the imp in his trial by combat."
	print "What do you do?"
	print "\t1) Volunteer for Tyrion."
	print "\t2) Let Tyrion fight for himself."
	choice = raw_input("> ")
	
	# if user chose 1, run tyrion function.
	if choice == "1":
		print "\nYou fight for Tyrion, and win!"
		print "You and Tyrion are let free, and Tyrion gives you some gold. He says:"
		print "\t\"A Lannister always pays his debts.\""
		print "\nAfter a few days, you and Tyrion have arrived in King's Landing."
		kingslanding()
	
	# if user chose 2, run dead function
	elif choice == "2":
		print "\nTyrion fights and loses, getting thrown out the moon door."
		print "You feel terrible for the little guy!"
		print "You walk up to Lysa Tully and slap her in the face."
		print "Lysa slowly moves toward you, and then kicks you out the moon door."
		dead("\nRobin claps for making you \"fly\". You die.")
	
	# if user chose something else, run dead function	
	else:
		dead("\nYou are a hopeless child that doesn't know right from left. You die.")	

# essos function: ask for user input
def essos():
	print "\nThe ship takes you accross the Narrow Sea."
	print "After the ship is docked, Arya continues on to Braavos."
	print "You decide to explore this new land on your own."
	print "\nYou run into a man named Jorah Mormont."
	print "Jorah tells you a woman broke his heart."
	print "How do you respond?"
	print "\t1) Everyone saw that coming."
	print "\t2) God, Jorah, get it together." 
	print "\t3) Welcome to Dumpsville, Population: You."
	print "\t4) Nice guys always finish last."
	print "\t5) Wait, so... I've heard a lot about this Daario Naharis guy.."
	print "\t6) LOL YOU GOT FRIEND-ZONED!"	
	choice = raw_input("> ")
	
	print "\nJorah sheds a tear. Poor Jorah."
	print "He shamefully points you the way to the city of Meereen."
	meereen()

# meereen function, ask for user input
def meereen():
	print "\nIn Meereen, Missandei introduces you to the Khaleesi."
	print "She says you are in the presence of:"
	print "\t\"Daenerys Stormborn of the House Targaryen, the First of Her Name, \n\t the Unburnt, Queen of Meereen, Queen of the Andals and the Rhoynar \n\t and the First Men, Khaleesi of the Great Grass Sea, Breaker of \n\t Chains, and Mother of Dragons.\""
	print "\nYou are nervous and star-struck."
	print "She asks you why you are here and what you want."
	print "What do you say?"
	print "\t1) Khaleesi, you are the Moon of my Life."
	print "\t2) I saw a dragon on my way here."
	print "\t3) I'm Team Stannis!"
	print "\t4) Try this vintage wine that I brought you! \n\t   Have a sip. No, really, take a sip!!"
	choice = raw_input("> ")
	
	# if choice is 3 or 4, run dead function.
	if choice == "3" or choice == "4":
		print "\nDaenerys shoots up from her chair and shouts:"
		print "\t\"Kill this traitor!\""
		dead("\nYou are taken away from Khaleesi, and locked in a vault left to die. You die.")	
	
	# if choice is 1, run dead function.
	elif choice == "1":
		print "\nDaenerys walks over to you. She examines you and asks if you really \nare Khal Drogo reincarnated as an ugly peasant."
		print "What do you say?"
		print "\t1) Why, Yes I am."
		print "\t2) No I am not, but I want to be your sun and stars."
		choice = raw_input("> ")
		
		print "\nDaenerys declares you the same fate of the traitor Jorah."
		print "She demands you leave the city immediately."
		print "You leave and wander around the Red Sea until you die of starvation."
		dead("\nIt's not easy being in love with Daenerys Targaryen")
		
	# if you chose option 2, run the continued function
	elif choice == "2":
		print "\nDaenerys asks you where you saw the dragon, and demands you take her to him."
		dragon()
	
	# else: run the dead function
	else:
		dead("\nYou are a hopeless child that doesn't know right from left. You die.")	

# dragon function: ask user for input
def dragon():
	print "\nYou take Daenerys to the place you last saw the dragon."
	print "But he is nowhere to be seen."
	print "\nAll of a sudden the dragon comes swooping in and grabs you with it's feet."
	print "What do you do?"
	print "\t1) Poke at it with your wooden stick."
	print "\t2) Yell \"Dracarys\" at the beast."
	print "\t3) Climb up the dragon and try to steer him."
	choice = raw_input("> ")
	
	# if user runs choice 1, run dead function
	if choice == "1":
		dead("\nThe dragon becomes angry and eats you. You die.")
	
	# if user runs chice 2, 
	elif choice == "2":
		print "\nThe dragon immediately breathes fire."
		print "He turns all the bystanders into ashes, except of course, \nKhaleesi, who remains unharmed by the flames."
		print "She summons her dragon with her good looks."
		dead("Khaleesi orders the dragon to eat you. You die.")
	
	# if user chose choice 3: run westeros function
	elif choice == "3":
		print "\nYou manage to get the dragon under control."
		print "You scream at Khaleesi below:"
		print "\t\"I am %s, the First of My Name, the Slightly Burnt, \n\tand Ruler of Dragons! Ten Points to Gryffindor!\"" % name
		print "\nYou fly the dragon over the Narrow Sea, back to Westeros."
		print "\nThe dragon drops you off at the entrance to King's Landing."
		kingslanding()
	
	# if user chose something else, run dead function.
	else:
		dead("\nYou are a hopeless child that doesn't know right from left. You die.")	

#kingslanding function: ask user for input
def kingslanding():
	print "\nAt King's Landing, you wander around aimlessly until you ask a guard for help."
	print "The gaurd asks you what business you have here"
	
	# while loop, ask user for input, until they pick right.
	while True:
		print "What do you say?"
		mottos()
		choice = raw_input("> ")
	
		# if the user chose choice 9, run the wedding function.
		if choice == "9":
			print "\nThe guard sends you to Olenna Tyrell."
			wedding()
			break
		
		# if the user chose this choice, execute dead function
		elif choice == "5":
			print "\nThe guard laughs and sends you to go get ready for a fight."
			print "You arrive in a ring, and decide to show off some gymnastic skills."
			dead("The Mountain arrives. You die.")
			
		# if the user chose this choice, execute dead function
		elif choice == "2":
			print "\nThe guard sends you to Blackwater Bay."
			print "You arrive at the bay when suddenly the beach explodes."
			dead("\nYou are burned to death by wildfire. You die.")
		
		# if the user chose this choice, execute dead function
		elif choice == "4":
			print "\nThe guard hands you an invitation and you are sent to Joffrey's wedding."
			print "On your way to Joffrey's wedding, you see Ser Pounce."
			print "You go up to the cat to pet it, but he eats your face off."
			dead("\nHear me Meow.")
			
		# if the user chose this choice, execute dead function
		elif choice == "6":
			print "\nThe guard throws you out of King's Landing."
			print "He declares that Starks are traitors."
			print "You begin walking to Winterfell when a huge blizzard arrives."
			dead("\nWinter has indeed arrived. You die.")
	
		# if the user chose this choice, execute dead function
		elif choice == "7":
			print "\nThe gaurd executes you on the spot."
			print "No one wants a Targayen in King's Landing!"
			print "That's why they've been exiled to Essos!"
			dead("\nYou die.")
			
		# if the user chose this choice, execute dead function
		elif choice == "1" or choice == "3" or choice == "8":
			print "\nThe guard has no idea what mottos those words belong to."
			print "Obviously those houses aren't important."
			print "He tells you to pick a new motto."
		
		# if the user chose incorrectly: run dead function
		else:
			dead("\nYou are a hopeless child that doesn't know right from left. You die.")	

def wedding():
	print "\nOlenna sees you're on her side, and gives you liquid posion."
	print "She tells you that you must pour the poison Joffrey's drink at the wedding."
	print "You agree."
	print "\nAt the wedding, you slip the poison into Joffrey's cup."
	print "You then get a brilliant idea."
	print "You add the poison to every guest's cup."
	print "Every. Single. Person. At. The. Wedding. Is. Poisoned."
	print "\nCongratulations! You win! You've killed everyone in King's Landing."
	print "You have the Iron Throne."
	exit(0)
	
# Run the Start Function
print "\nWelcome to the Game of Thrones."
print "\nYou play or you die."
print "\nEnter your Name:"
name = raw_input("> ")
mode()


print ""

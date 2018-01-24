# Choose your own adventure with a different starting point every time
# Text based adventure game
#Opposite of traditional game; upside down flowchart
# Uses code branches

# Test out every branch

def failed_parachute():
	print("Your parachute fails! Good luck!")

def cursed_mountain():
	print("You land on the mountain, known as CURSED MOUNTAIN")

def water():
	print("You make a rough landing in the water! You put on your flotation vest and wait for rescue.")

def curl():
	print("Good thinking! Your plane crashes softly. You are safe, but in an unknown area.")

def valley():
	print("You safely land in the middle of the sheep herd.")

def sheep_ride():
	print("The trusty sheep takes you to the nearest town. You are safe!")

def sheep_herder():
	print("You become a successful sheep herder and make millions of dollars.")

def bad_wizard():
	print("The object captures you and throws you into a cursed stew with creepy eyeballs and chicken legs.")

def good_wizard():
	print("A wizard comes from the object with a large coconut and a shield potion for you.")
	print("In a booming voice, the magical wizard explains, " + "Welcome to Cursed Mountain!!! " + " I suggest you explore this magical monstrosity!")

def answer_ab():
	print("Please type 'A' or 'B'")

def demise():
	print("You end your tumble at the end of the slope.")
	print("You have reached your breaking point.")
	input("\n\npress the enter key to exit.")

def jagged_rock():
	print("you manage to suddenly stop your flight by clutching the jagged rock.")
	print("You realize your hands and arms are very slimy.")
	print("but... why?")
	print("You spot an opening in the ground next to the rock")
	print("The hole is just big enough for you to crawl through")

def spikey_tree():
	print("You barely hang on to a spiky tree")
	print("OUCH! The tree is too spiky. You must let go of your grip and you continue your tumultuous tumble down the treacherous slope")

def snail_demise():
	print("Draco spits out an acidic goo that covers you")
	print("You are unable to move and are stuck on this rock, hearing Draco's tales of his snail trails, until the end of your days")


print("You take your trusty propeller plane out for a joy ride. Suddenly, the plane's propeller stops working and you are hurtling towards the ground! You quickly spot a parachute next to you. What do you do? ")

print("When making decisions, please type your answer as an uppercase letter.")

while True:
    choice = input("A) Quickly put on the parachute, B) Try to steer the plane towards the nearest body of water, or C) Curl up into a ball ")

    if choice == "A":
    	# First branch of story
    	print("You jump out of the plane! You pull the string to open up the parachute. To your right, you see a mansion on top of a mysterious mountain. To your left, you see a sheep herd in the valley. What do you do? ")
    	choice = input("A) Steer right or B) Steer left ")
    	if choice == "A":
    		cursed_mountain()
    		print("You see an object in the distance.")
    		choice = input("A) Go to object? or B) Hike towards the mansion ")

    		if choice == "A":
    			print("You are weary from the excitement and your health is low from the landing.")
    			good_wizard()
    			choice = input("Explore CURSED MOUNTAIN? 'Y' or 'N' ")
    			if choice == 'Y':
    				print("You begin your exploration of Wizard Mountain.")
    				print("You are a little dizzy and sick from your landing.")
    				print("You spot a bottle of opened motion-sickness meds curiously lying on a rock to your left.")
    				choice = input("ingest the contents of the motion-sickness bottle? 'Y' or 'N' ")
    				if choice == 'Y':
    					print("Bad move? Yes!")
    					print("The contents of the bottle was not what it said it was!")
    					print("You begin to feel even more woozy and disoriented.")
    					print("You see a light at the corner of your eye and a fuzzy dark figure appear to your left.")
    					choice = input("A) Go towards the light, or B) Ask the fuzzy dark figure for help ")
    					if choice == 'A':
    						print("You head towards the light")
    						print("Uh Oh, the light source was the horizon of a steep hill!")
    						choice = input("You begin tumbling towards certain death.. Is this your demise? 'Y' or 'N' ")

    						if choice == 'Y':
    							demise()

    						elif choice =='N':
    							print("You are a fighter!")
    							print("Though, your ungraceful tumble down the steep slope past spiky trees and jagged rocks promises certain death")
    							choice = input("A) Grab hold of a passing spikey tree, or B) Clutch a jagged rock? ")

    							if choice == 'A':
    								spikey_tree()
    								demise()
    							elif choice == 'B':
    								jagged_rock()
    								choice = input("A) Take a closer look at the rock, or B) Travel down the hole ")
    								if choice == 'A':
    									print("Gross!")
    									print("The rock is full of slimy snails")
    									print("You hear a tiny voice coming from one of these slimy snails")
    									choice = input("Listen to the talkative snail? 'Y' or 'N' ")
    									if choice == 'Y':
    										print("The snail tells you tales of wonder about CURSED MOUNTAIN")
    										print("This is a place of treasure far as the eye can see, good wizards, bad wizards, and a terrible silicon breathing dragon")
    										print("The snail tells you its name, 'Draco' ")
    										print("Draco: What is your name?")
    										name = input()
    										print("Draco: " + name + " You seem a bit battered, to say the least ")
    										print("So, " + name)
    										choice = input(" Do you need my help? 'Y' or 'N' ")
    										if choice == 'Y':
    											print("Draco: Next to this rock is a hole. I suggest you head down it")
    											print("I think you'll find what your plane has brought you here for")
    										elif choice == 'N':
    											snail_demise()


    								elif choice == 'B':
    									print("you crawl through the hole")
    									print("After a few minutes of shuffling down the hole, you plumet and land with a splash into an underground lake.")


    					elif choice == 'B':
    						bad_wizard()




    		else:
    			bad_wizard()


    	elif choice == "B":
    		valley()
    		choice = input("A) Ride a sheep to the nearest town or B) Become a sheep herder")
    		if choice == "A":
    			sheep_ride()

    		elif choice == "B":
    			sheep_herder()

    	else:
    		failed_parachute()

    elif choice == "B":
    	# Second branch of the story
    	water()

    elif choice == "C":
    	# Third branch of the story
    	curl()

    question = input("Do you want to try again? y or n")
    if question == 'n':
        break


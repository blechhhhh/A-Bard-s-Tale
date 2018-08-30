import random
import time
import pygame

sword = 0
hp = 20
gold = 0
healthPotion = 0
look1 = 0

'''
def dropItem():
'''

easy_m = ['rat', 'slime', 'bat', 'kobold']
medium_m = ['skeleton', 'wolf', 'bandit', 'goblin']
hard_m = ['dragon', 'giant', 'wizard', 'flumph']

def easy_m_encounter():
	global hp
	emhp = random.randint(2,4)
	rata = " bit you."
	slimea = " tackled you."
	bata = " scratched you."
	kobolda = " poked you with a spear."
	monster = random.choice(easy_m)
	print(bcolors.orange + "A " + monster + " has appeared!" + bcolors.ENDC)
	if monster == "rat":
		monstera = rata
	elif monster == "slime":
		monstera = slimea
	elif monster == "bat":
		monstera = bata
	elif monster == "kobold":
		monstera = kobolda
	while emhp > 0:
		if hp > 0:
			print("What do you want to do? Attack(1) or run away(2).")
			peae = input("Please Choose One: ")
			accuracy = random.randint(0,100)
			maccuracy = random.randint(0,100) 
			if peae == "1":
				if accuracy <= 30:
					print(bcolors.orange + "You swing and miss." + bcolors.ENDC)
				elif accuracy >=31:
					print(bcolors.green + "You swing at the " + monster + " with a sword!" + bcolors.ENDC)
					sdmg = random.randint(1,4)
					emhp = emhp - sdmg
					if emhp > 0:
						print(bcolors.yellow + monster + " hp: " + str(emhp) + bcolors.ENDC)
					elif emhp <= 0:
						print(bcolors.green + "The " + monster + " has died." + bcolors.ENDC)
			elif peae == "2":
				escprob = random.randint(0,100)
				if escprob <= 30:
					print(bcolors.green + "You successfully ran away!" + bcolors.ENDC)
					return False
				elif escprob >= 31:
					print(bcolors.orange + "You did not successfully run away!" + bcolors.ENDC)
			else:
				print("Please choose either 1 or 2")
			if emhp > 0:	
				if maccuracy <= 30:
					print(bcolors.yellow + "The " + monster + " missed." + bcolors.ENDC)
				elif maccuracy >= 31:	
					print(bcolors.orange + "The " + monster + str(monstera) + bcolors.ENDC)
					mdmg = random.randint(1,2)
					hp = hp - mdmg
					if hp > 0:
						if hp >= 13:	
							print(bcolors.green + "HP: " + str(hp) + bcolors.ENDC)
						elif hp >= 6:
							print(bcolors.yellow + "HP: " + str(hp) + bcolors.ENDC)
						else:
							print(bcolors.orange + "HP: " + str(hp) + bcolors.ENDC)
					elif hp >= 0:
						print(bcolors.orange + "HP: 0" + bcolors.ENDC)
		elif hp <= 0:
			return False
	if hp <= 0:
		print(bcolor.orange + "Game Over" + bcolor.ENDC)

def med_m_encounter():
	global hp
	mmhp = random.randint(4,8)
	skeletona = " swung a sword at you."
	wolfa = " bit you."
	bandita = " attacked you with a dagger."
	goblina = " bit you."
	monster = random.choice(medium_m)
	print(bcolors.orange + "A " + monster + " has appeared!" + bcolors.ENDC)
	if monster == "skeleton":
		monstera = skeletona
	elif monster == "wolf":
		monstera = wolfa
	elif monster == "bandit":
		monstera = bandita
	elif monster == "goblin":
		monstera = goblina
	while mmhp > 0:
		if hp > 0:
			print("What do you want to do? Attack(1) or run away(2).")
			peam = input("Please Choose One: ")
			accuracy = random.randint(0,100)
			maccuracy = random.randint(0,100) 
			if peam == "1":
				if accuracy <= 30:
					print(bcolors.orange + "You swing and miss." + bcolors.ENDC)
				elif accuracy >=31:
					print(bcolors.green + "You swing at the " + monster + " with a sword!" + bcolors.ENDC)
					sdmg = random.randint(1,4)
					mmhp = mmhp - sdmg
					if mmhp > 0:
						print(bcolors.yellow + monster + " hp: " + str(mmhp) + bcolors.ENDC)
					elif mmhp <= 0:
						print(bcolors.green + "The " + monster + " has died." + bcolors.ENDC)
			elif peam == "2":
				escprob = random.randint(0,100)
				if escprob <= 30:
					print(bcolors.green + "You successfully ran away!" + bcolors.ENDC)
					return False
				elif escprob >= 31:
					print(bcolors.orange + "You did not successfully run away!" + bcolors.ENDC)
			else:
				print("Please choose either 1 or 2")
			if mmhp > 0:	
				if maccuracy <= 30:
					print(bcolors.yellow + "The " + monster + " missed." + bcolors.ENDC)
				elif maccuracy >= 31:	
					print(bcolors.orange + "The " + monster + str(monstera) + bcolors.ENDC)
					mdmg = random.randint(1,2)
					hp = hp - mdmg
					if hp > 0:
						if hp >= 13:	
							print(bcolors.green + "HP: " + str(hp) + bcolors.ENDC)
						elif hp >= 6:
							print(bcolors.yellow + "HP: " + str(hp) + bcolors.ENDC)
						else:
							print(bcolors.orange + "HP: " + str(hp) + bcolors.ENDC)
					elif hp >= 0:
						print(bcolors.orange + "HP: 0" + bcolors.ENDC)
		elif hp <= 0:
			return False
	if hp <= 0:
		print(bcolor.orange + "Game Over" + bcolor.ENDC)

def hard_m_encounter():
	global hp
	hmhp = random.randint(4,8)
	global hp
	hmdh = random.randint(4,8)
	dragona = " shot flames at you."
	gianta = " swung a club at you."
	wizarda = " shot you with a spell."
	flumpha = " flung you."
	monster = random.choice(hard_m)
	print(bcolors.orange + "A " + monster + " has appeared!" + bcolors.ENDC)
	if monster == "dragon":
		monstera = dragona
	elif monster == "giant":
		monstera = gianta
	elif monster == "wizard":
		monstera = wizarda
	elif monster == "flumph":
		monstera = flumpha
	while hmhp > 0:
		if hp > 0:
			print("What do you want to do? Attack(1) or run away(2)?")
			peah = input("Please Choose One: ")
			accuracy = random.randint(0,100)
			maccuracy = random.randint(0,100) 
			if peah == "1":
				if accuracy <= 30:
					print(bcolors.orange + "You swing and miss." + bcolors.ENDC)
				elif accuracy >=31:
					print(bcolors.green + "You swing at the " + monster + " with a sword!" + bcolors.ENDC)
					sdmg = random.randint(1,4)
					hmhp = hmhp - sdmg
					if hmhp > 0:
						print(bcolors.yellow + monster + " hp: " + str(hmhp) + bcolors.ENDC)
					elif hmhp <= 0:
						print(bcolors.green + "The " + monster + " has died." + bcolors.ENDC)
			elif peah == "2":
				escprob = random.randint(0,100)
				if escprob <= 30:
					print(bcolors.green + "You successfully ran away!" + bcolors.ENDC)
					return False
				elif escprob >= 31:
					print(bcolors.orange + "You did not successfully run away!" + bcolors.ENDC)
			else:
				print("Please choose either 1 or 2")
			if hmhp > 0:	
				if maccuracy <= 30:
					print(bcolors.yellow + "The " + monster + " missed." + bcolors.ENDC)
				elif maccuracy >= 31:	
					print(bcolors.orange + "The " + monster + str(monstera) + bcolors.ENDC)
					mdmg = random.randint(1,2)
					hp = hp - mdmg
					if hp > 0:
						if hp >= 13:	
							print(bcolors.green + "HP: " + str(hp) + bcolors.ENDC)
						elif hp >= 6:
							print(bcolors.yellow + "HP: " + str(hp) + bcolors.ENDC)
						else:
							print(bcolors.orange + "HP: " + str(hp) + bcolors.ENDC)
					elif hp >= 0:
						print(bcolors.orange + "HP: 0" + bcolors.ENDC)
		elif hp <= 0:
			return False
	if hp <= 0:
		print(bcolor.orange + "Game Over" + bcolor.ENDC)

def intro():
	print("Hello " + name + " and welcome to whatever the heck this is going to be called.")
	time.sleep(2)
	print("You wake up in a strange place not knowing how you got there.")
	time.sleep(2)
	print("You look around and see that you are in a small cave surrounded by \nsmall piles of bones.")
	time.sleep(2)
	print("You see that there is an exit across the cave with light pouring in.")
	time.sleep(2)
	print("You notice a sword near one of the piles of bones and pick it up.")
	time.sleep(2)
	global sword
	sword = sword + 1
	print(bcolors.green + "You have obtained a sword :)" + bcolors.ENDC)
	time.sleep(2)
def choice1():
	global look1
	print("Would you like to head out the entrance or be THat person and spend \nan hour scouring over the whole cave to make sure you didnt miss anything")
	choice = input("Leave(1), or Look around(2): ")
	if choice == "1":
		print("You head outside into a dense forest.")
		time.sleep(2)
		encounter1()
	elif choice == "2":
		if look1 == 0:
			print(bcolors.blue + "You don't find anything, get on with it." + bcolors.ENDC)
			look1 = look1 + 1
			time.sleep(2)
			choice1()
		elif look1 == 1:
			print(bcolors.blue + "stop" + bcolors.ENDC)
			time.sleep(2)
			look1 = look1 + 1
			choice1()
		elif look1 == 2:
			print(bcolors.blue + "Really just stop." + bcolors.ENDC)
			look1 = look1 + 1
			choice1()
		elif look1 == 3:
			print(bcolors.blue + "I said stop looking you soggy piece of bread." + bcolors.ENDC)
			look1 = look1 + 1
			choice1()
		elif look1 == 4:
			print(bcolors.blue + "Please just move on." + bcolors.ENDC)
			look1 = look1 + 1
			choice1()
		else:
			print(bcolors.blue + "..." + bcolors.ENDC)
			choice1()
	else:
		print("Please choose either 1 or 2")
		choice1()
def encounter1():
	print("You hear something amongst the trees near you.")
	time.sleep(2)
	print("The sound almost seems as though it is getting closer.")
	time.sleep(2)
	easy_m_encounter()
def realization():
	skip = input("skip realization(1) continue(2)")
	if skip == "1":
		return
	else:
		print("continue")
	print("You start getting homesick and want to return to your family and frien... \nlmao jk scrap that home is boring as heck")
	time.sleep(1)
	print("You start off on the search of the time of your life!")
	time.sleep(1)
	print("You find a random, narrow path and start following it.")
	print(".") 
	time.sleep(2) 
	print(".") 
	time.sleep(2) 
	print(".")
	time.sleep(1)
	print("You realize you haven't encountered something in a while and you're \nfinally starting to relax.")
	time.sleep(1)
	print(".")
	time.sleep(1)
	easy_m_encounter();
def discovery():
	time.sleep(1)
	print("After that encounter you are slightly shook however you continue on.")
	time.sleep(1)
	print("You keep heading down the path for a little bit longer.")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print("In the distance you see a wall.")
	time.sleep(1)
	print("As you approach the wall you hear a booming voice.")
	time.sleep(1)
	print(bcolors.blue + '"Who are you and what is your business here?"' + bcolors.ENDC)
	time.sleep(1)
	print("I am " + name + ", I wish to eat and get a good nights rest.")
	time.sleep(1)
	print(bcolors.blue + '"LMAO who names their kid ' + name + ' ?"' + bcolors.ENDC)
	time.sleep(1)
	print(bcolors.blue + '"Aight come in I guess."' + bcolors.ENDC)
	time.sleep(1)
	print("The doors open, and you walk in.")
	time.sleep(1)
def town1():
	print("You ask the guard where an inn is.")
	time.sleep(1)
	print("He tells you to head down Main Street, take a left at the your mom \nand then it should be on the right.")
	time.sleep(1)
	print("So you head down Main Street which is very lively keeping an eye \nout for your mom.")
	time.sleep(1)
	print("You find a building with a sign that says your mom and take a left there.")
	time.sleep(1)
	print("You turn the corner and see a very nice looking inn which is called \nToblerone Inn.")
	time.sleep(1)
	print("As you walk towards the inn you realize you have no money.")
	time.sleep(1)
	print("You enter Toblerone Inn and head over to the check-in person and tell \nthem about your situation.")
	time.sleep(1)
	print("They introduce themselves as Alvera the Owner and say that they'll let \nyou stay on one condition.")
	time.sleep(1)
	print(bcolors.blue + "Before I let you stay here free of charge you must challenge \nthe bard in a lute duel and emerge victorious." + bcolors.ENDC)
	sleepChoice()
def sleepChoice():
	print("Do you accept this challenge(1) or will you leave an find someplace else \nto spend the night(2)?")
	choice2 = input("Please choose one: ")
	if choice2 == "1":
		duel()
	elif choice2 == "2":
		theStreets()
	else:
		print("Please choose either 1 or 2")
		sleepChoice()
def duel():
	print(bcolors.blue + '"Alright, it\'s time to dd-dd-dd-d-d-d-d-dd-d-d-duel. \nHowever before we do that we must flip a coin to decide who goes first."' + bcolors.ENDC)
	choice = input("Heads(1) or Tails(2)")
	coinOutcome = random.randint(1,2)
	if coinOutcome == choice:
		print(bcolors.blue + "Don't let me down." + bcolors.ENDC)
		print("All of a sudden the knowledge of how to play the lute comes to you from nowhere.")
		print("Strangely however you only know how to play Toccatta and fugue in D minor(1), The \nCup Song(2) ,and Stairway to Heaven(3).")
		songChoice = input("Which song would you like to start out with? 1, 2 or 3: ")




def theStreets():
	print(":(")



class bcolors:
    pink = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    orange = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.pink = ''
        self.blue = ''
        self.green = ''
        self.yellow = ''
        self.orange = ''
        self.ENDC = ''
        
print(bcolors.yellow + "welcome to"                          + bcolors.ENDC)
print(bcolors.yellow + " _________________________________________________________ " + bcolors.ENDC)
print(bcolors.yellow + "|" + bcolors.ENDC + "      .      .--.              . .      .---.    .       " + bcolors.yellow + "|" + bcolors.ENDC)
print(bcolors.yellow + "|" + bcolors.ENDC + "     / \     |   )             | |        |      |       " + bcolors.yellow + "|" + bcolors.ENDC)
print(bcolors.yellow + "|" + bcolors.ENDC + "    /___\    |--:  .-.  .--..-.|  .--.    | .-.  | .-.   " + bcolors.yellow + "|" + bcolors.ENDC)
print(bcolors.yellow + "|" + bcolors.ENDC + "   /     \   |   )(   ) |  (   |  `--.    |(   ) |(.-'   " + bcolors.yellow + "|" + bcolors.ENDC)
print(bcolors.yellow + "|" + bcolors.ENDC + "  '       `  '--'  `-'`-'   `-'`- `--'    ' `-'`-`-`--'  " + bcolors.yellow + "|" + bcolors.ENDC)
print(bcolors.yellow + " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ " + bcolors.ENDC)
print("What is your name?")
name = input("Name: ")
intro()
choice1()
realization()
discovery()
town1()

# Basic-Text-Space-Game
# Based on a board game I used to play 25+ years ago called Space Crusade
# It is a work in progress

from sys import exit, argv
from collections import deque
from os.path import exists

script, x, y, z = args

 
def dreadnought2():
	
	global squad
	
	print "You enter the bridge. You hear a whirl of hydraulics and scatter."
	print "A hail of cannon rains down on your position of cover."
	print "A dreadnought stands on the centre of the bridge.\n"
	print "1. Organise an assault?"
	print "2. Distract and setup cannon?"
	print "3. Head back to the corridor and regroup?"
	
	choice = raw_input("> ")
	
	if choice == "1":
		if len(squad) > 1:
			y = squad[0]
			print "\nThe %s is obliterated!" % y
			squad.remove(y)
			print squad
			print "Make another call Commander!\n"
			dreadnought2()
		else:	
			dead("You die a glorious death!!")
	elif choice == "2":
		print "You setup the cannon and it destroys the Dreadnought! VICTORY!!"
		exit(0)
	else:
		dead("You are hunted down and killed like dogs!")

def dreadnought1():
	print "\nYou enter the room and here a whirl of hydraulics!"
	dead("Your team is obliterated by a dreadnought!")

def laser_cannon():
	global squad
	
	print "You scan for life. Nothing."
	print "You check round the corner and detect a laser cannon!\n"
	print "1. Blow the cannon up using ordinance?"
	print "2. Create a diversion and disable the cannon?"
	print "3. Charge the cannon and take it out the old fashioned way?"
	
	choice = raw_input()
	# Need the cannon to destroy boss. Need cannon variable.....???
	# Or do it with an alternative function!!! :) Maybe...??
	if choice == "1":
		print "Your team blows the cannon up!\n"
		#The explosion alerts the dreadnought to your presence == DEATH!!!!
		dreadnought1()
	elif choice == "2":
		print "Your team disables the cannon."
		print "You take the cannon with you.\n"
		dreadnought2()
	elif choice == "3":
		if len(squad) == 1:
			dead("Suicide!")
		elif len(squad) >= 2:
			y = squad[0]
			print "The %s is killed in a hail of laser fire!" % y
			print "You retreat to your start position.\n"
			squad.remove(y)
			print squad
			print "Make another call!\n"
			laser_cannon()
		else:
			dead("Charging the cannon was a bad idea!")
	else:
		dead("Charging the cannon was a bad idea!")

def mech_ambush():
	global squad
		
	print "You round the corner and walk straight into"
	print "a Mechanoid unit who are waiting in ambush for you!\n"
	
	if len(squad) <= 1:
		dead("Suicide has arrived!")
	
	y = squad[0]
	print "%s is killed instantly!" % y
	squad.remove(y)
	
	if len(squad) >= 1:
		print squad
	else:
		dead("Suicide has arrived!")
		
	print "Next decision Commander?"
	print "1. Retreat and regroup?"
	print "2. Attempt to take the unit?\n"
	
	choice = raw_input("> ")
	
	if choice == "1":
		corridor2()
	elif choice == "2":
		dead("Suicide has arrived!")
	else:
		dead("Your hesitation has gotten you terminated!")
	
def corridor2():
	print "Your squad heads down the corridor. You come to a junction."
	print "Will your team go left or right?\n"
	
	choice = raw_input("> ")
	
	if choice == "left":
		mech_ambush()
	elif choice == "right":
		laser_cannon()
	else:
		dead("Your hesitation has cost your life!")

def safe_room1a():
	print "You open the door and find 2 Orcs hacking at a wall safe."
	print "You surprise them and kill them before they can reach their weapons."
	print "The safe is open, the codes to destroy the ship are within."
	print "Do you....\n"
	print "1. Grab the codes and destroy the ship?"
	print "2. Scan for more traps?"
	print "3. Leave the codes in situ?"
	
	choice = raw_input()
	
	if choice == "1":
		dead("You grab the codes and set off a booby trap!")
	elif choice == "2":
		print "You pick up a booby trap and disarm it. You take the destruct codes.\n"
		corridor2()
	else:
		dead("You inexplicably leave the codes! You are relieved of duty!")	

def corridor1b():
	print "Back in the corridor you have a door opposite" 
	print "the corridor to the right leading further into the ship"
	print "What will you do?\n"
	print "1. Open the door?"
	print "2. Push on down the corridor?"
		
	choice = raw_input("> ")
	
	if choice == "1":
		safe_room1a()
	elif choice == "2":
		print "You push on down the corridor."
		print "The door behind you explodes and 2 Orcs emerge, guns blazing!"
		print "You make for the end of the corridor. As you approach a dreadnought blocks the way!"
		dead("You are cut down in a hail of cannon fire!")
	else:
		dead("Your confused commands have compromised the mission!")

def prisoners():

	global squad
	
	print "You enter the room to see 2 prisoners in a cell."
	print "They are bearly conscious."
	print "Do you....\n"
	print "1. Rush over to free them?"
	print "2. Survey the room?"
	print "3. Return to free them later after the ship is liberated?"
	# do I create another function to kill them for this mistake later?
	booby_trap_set = True
	#Need to figure how to communicate state of booby trap between functions....Global var again?
	choice = raw_input()
	
	if choice == "1" or not booby_trap_set:
		dead("You walk straight into a booby trap")
	elif choice == "2" or not booby_trap_set:
		print "You employ caution and find a trap."
		# Here you need to ascertain if Tech is still in team.
		# If he is ok, if not penalty incurred to whoever disarms it (RNG)
		booby_trap_set = False
		print "You leave your medic with the casualties and vow vengence!"
		global squad
		squad.remove("Medic")
		print squad
		corridor1b()
	elif choice == "3":
		print "They are beaten but alive. You push onwards leaving a guard behind.\n"
		y = squad[0]
		squad.remove(y)
		print squad
		corridor1b()
	else:
		dead("You have made a critical error commander!")
		
def safe_room1():
	print "The door opens and you find 2 Orcs!"
	print "They open fire and a hail of cannon swamps you."
	# Random squad member hit. RNG to determine????
	print "The Sniper gets a hole blown in his chest!\n"
	global squad
	squad.remove("Sniper")
	print squad
	print "You retreat back to the corridor and seal the door.\n"
	corridor1a()

def corridor1a():
	print "There is a door to the left and right."
	print "Which do you take?\n"
	
	choice = raw_input()
	
	if choice == "left":
		safe_room1()
	elif choice == "right":
		prisoners()
	else:
		corridor1a()

def corridor1():
	print "You take cover with your men."
	print "Your scout reports 2 Goblins ahead."
	print "Will you?...\n"
	print "1. Charge them down in a hail of fire?"
	print "2. Lob a photon grenade?"
	print "3. Utilise the platoon sniper?"
		
	choice = raw_input("> ")
	
	if choice == "1":
		dead("You charge straight into a booby trap!")
	elif choice == "2":
		print "The grenade is faulty and detonates in your Tech's hand.\n"
		global squad
		squad.remove("Tech")
		print "Make another call!"
		
		choice = raw_input("> ")
		
		if choice == "1":
			dead("You charge straight into a booby trap!")
		elif choice == "3":
			print "The sniper takes out the Goblin scum.\n"
			corridor1a()
		else:
			dead("Your instructions are unclear in battle.")
				
	elif choice == "3":
		print "The sniper takes out the Goblin scum.\n"
		corridor1a()
	else:
		dead("Your instructions are unclear in battle!")
				
def dead(why):
	print why, "Congratulations, you are dead!"
	exit(0)

def start():
	print "You approach the airlock of the rusting hulk."
	print "You fire up your weapon systems."
	print "The door opens to a hail of cannon fire."
	print "Will you? :\n"
	print "1. Stand and return fire?"
	print "2. Move to cover?"
	print "3. Send in your men first?"
	
	global squad
	squad = ["Scout", "Tech", "Medic", "Sniper", "Commander"]
	print squad

	choice = raw_input("> ")
	
	if choice == "1":
		dead("You are cut down in laser fire.")
	elif choice == "2":
		corridor1()
	elif choice == "3":
		dead("Your men abandon you as a coward!")
	else:
		dead("Your instructions are unclear in battle!")
		
start()

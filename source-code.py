from sys import exit, argv
from collections import deque
from os.path import exists
import random

script, x, y, z = args

def dreadnought2():
	
	global squad
	
	print "You enter the bridge. You hear a whirl of hydraulics and scatter."
	
	print "You roll 2D6 to see if anyone is engulfed in the hail of cannon fire."
	print "7+ means squad gets safely to cover."
	print "6 or less means 1 fatality.\n"
		
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	print d1, d2
	result = d1 + d2
	print "You roll a %d\n" % result
		
	if result > 6:
		print "All squad members make it to cover safely.\n"
	elif result <= 6:	
		x = len(squad) - 1
		fatal = squad[random.randint(0, x)]
		if fatal == "Commander":
			dead("You die in glorious conflict!")
		else:
			print "You make it to cover. You squad checks in. The %s is dead.\n" % fatal
			squad.remove(fatal)
			print squad
	else:
		dead("Death has caught up with you Commander!")
	
	print "A hail of cannon rains down on your position of cover."
	print "A dreadnought stands on the centre of the bridge.\n"
	print "What is the next move Commander?\n"
	print "1. Organise an assault?"
	print "2. Distract and setup cannon?"
	print "3. Head back to the corridor and regroup?\n"
	
	print "Roll 9 or higher to register damage on a Dreadnought......\n"
	
	choice = raw_input("> ")
	
	if choice == "1":
		dread = 5
		
		while dread and squad > 0:
			d1 = random.randint(1, 6)
			d2 = random.randint(1, 6)
			print d1, d2
			result = d1 + d2
			print "You roll a %d\n" % result
				
			if result > 8:
				print "You have damaged the Dreadnought!\n"
				dread -= 1
			elif result <= 8:
				print "One of your squad was hit!"
				x = len(squad)-1
				fatal = squad[random.randint(0, x)]
					
				if fatal == "Commander":
					dead("You die in glorious conflict!")
				elif squad > 0:
					print "The %s is dead.\n" % fatal
					squad.remove(fatal)
					print squad
				else:
					dead("You have been annihilated!")
			else:
				dead("You have been annihilated")
		print "You setup the cannon and it destroys the Dreadnought! VICTORY!!"
		print squad
		exit(0)
				
	elif choice == "2":
		if len(squad) > 1:
			y = squad[0]
			print "\nThe %s is obliterated in setting a diversion." % y
			print "She died a glorious death!\n"
			squad.remove(y)
			print squad
			print "The Cannon is in place...You fire it up!"
			print "The Cannon is powerful so only needs a roll of 7+ to hit.\n"

			dread = 5
			cannon = 3
		
			while dread and cannon > 0:
				d1 = random.randint(1, 6)
				d2 = random.randint(1, 6)
				print d1, d2
				result = d1 + d2
				print "Cannon rolls a %d" % result
				
				if result > 6:
					print "You have damaged the Dreadnought!\n"
					dread -= 1
				elif result <= 6:
					print "The cannon was hit!\n"
					cannon -= 1
				else:
					dead("The cannon blows you up!")
				
			if dread == 0:
				print "The cannon destroys the Dreadnought! VICTORY!!"
				print "The following will become immortal Commander!"
				print squad
				exit(0)
			elif cannon == 0:
				print "You must face the Dreadnought...\n"
				
				while dread and squad > 0:
					d1 = random.randint(1, 6)
					d2 = random.randint(1, 6)
					print d1, d2
					result = d1 + d2
					print "You roll a %d\n" % result
				
					if result > 8:
						print "A Mech has been slain!\n"
						dread -= 1
					elif result <= 8:
						print "One of your squad was hit!"
						x = len(squad) - 1
						fatal = squad[random.randint(0, x)]
					
						if fatal == "Commander":
							dead("You die in glorious conflict!")
						elif squad > 1:
							print "The %s is dead.\n" % fatal
							squad.remove(fatal)
							print squad
						else:
							dead("You have been annihilated!")
					else:
						dead("You have been annihilated")
						
				print "The cannon destroys the Dreadnought! VICTORY!!"
				print "The following will become immortal Commander!"
				print squad
				exit(0)
		else:	
			dead("You die a glorious death!!")
	
	
	elif choice == "3":
		print "The Dreadnought has the advantage and you are supressed with laser fire."
		print "You resolve to retreat..."
		print "You roll 2D6."
		print "7+ means squad gets safely to cover."
		print "6 or less means 1 fatality.\n"
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		print d1, d2
		result = d1 + d2
		print "You roll a %d\n" % result
		
		if result > 6:
			print "All squad members make it to cover safely."
			dreadnought2()
		elif result <= 6:
			x = len(squad) - 1
			fatal = squad[random.randint(0, x)]
			if fatal == "Commander":
				dead("You die in glorious conflict!")
			else:
				print "You make it to cover. You squad checks in. The %s is dead.\n" % fatal
				squad.remove(fatal)
				print squad
				dreadnought2()
		else:
			dead("You are hacked down in gunfire!")
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
	
	choice = raw_input("> ")
	
	if choice == "1":
		print "You blow the cannon up!\n"
		dreadnought1()
	elif choice == "2":
		print "You resolve to divert and conquer the cannon."
		print "You roll 2D6."
		print "7+ means squad achieves objective unscathed."
		print "6 or less means 1 fatality.\n"
		
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		print d1, d2
		result = d1 + d2
		print "You roll a %d\n" % result
		
		if result > 6:
			print "All squad members are safe and accounted for."
			print "You disable the cannon."
			print "You take the cannon with you.\n"
			dreadnought2()
	
		elif result <= 6:	
			x = len(squad) - 1
			fatal = squad[random.randint(0, x)]
			if fatal == "Commander":
				dead("You die in glorious conflict!")
			else:
				print "You recover the cannon. You squad checks in. The %s is dead.\n" % fatal
				squad.remove(fatal)
				print squad
				print "You disable the cannon and take it with you.\n"
				dreadnought2()
		else:
			dead("You die via some unknown and unspeakable means.")
		
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
	print "Next decision Commander?"
	print "1. Retreat and move to cover?"
	print "2. Attempt to take the unit?\n"
	
	choice = raw_input("> ")
	
	if choice == "1":
		print "The Mechs have the advantage and you are supressed with laser fire."
		print "You resolve to move to cover."
		print "You roll 2D6."
		print "7+ means squad gets safely to cover."
		print "6 or less means 1 fatality.\n"
		
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		print d1, d2
		result = d1 + d2
		print "You roll a %d\n" % result
		
		if result > 6:
			print "All squad members make it to cover safely."
			print "Make the call to exterminate this scum!"
			choice = raw_input("> ")
			
			if choice == "2":
				print "Your team takes position and aims for the shot."
				print "You realsise there are 4 Mechs!"
				print "Roll 8 or higher to register a kill.\n"
			
				mechs = 4
			
				while mechs and squad > 0:
					d1 = random.randint(1, 6)
					d2 = random.randint(1, 6)
					print d1, d2
					result = d1 + d2
					print "You roll a %d\n" % result
				
					if result > 7:
						print "A Mech has been slain!\n"
						mechs -= 1
					elif result <= 7:
						print "One of your squad was hit!"
						x = len(squad)-1
						fatal = squad[random.randint(0, x)]
					
						if fatal == "Commander":
							dead("You die in glorious conflict!")
						elif squad > 0:
							print "The %s is dead.\n" % fatal
							squad.remove(fatal)
							print squad
						else:
							dead("You have been annihilated!")
					else:
						dead("You have been annihilated")
				print "The squad takes out the Mechanoid scum.\n"
				print squad
				laser_cannon()	
			
		elif result <= 6:	
			x = len(squad) - 1
			fatal = squad[random.randint(0, x)]
			if fatal == "Commander":
				dead("You die in glorious conflict!")
			else:
				print "You make it to cover. You squad checks in. The %s is dead.\n" % fatal
				squad.remove(fatal)
				print squad
				print "Make the call to exterminate this scum!"
				choice = raw_input("> ")
				
				if choice == "2":
					print "Your team takes position and aims for the shot."
					print "You realsise there are 4 Mechs!"
					print "Roll 8 or higher to register a kill.\n"
			
					mechs = 4
			
					while mechs and squad > 0:
						d1 = random.randint(1, 6)
						d2 = random.randint(1, 6)
						print d1, d2
						result = d1 + d2
						print "You roll a %d\n" % result
				
						if result > 7:
							print "A Mech has been slain!\n"
							mechs -= 1
						elif result <= 7:
							print "One of your squad was hit!"
							x = len(squad)-1
							fatal = squad[random.randint(0, x)]
					
							if fatal == "Commander":
								dead("You die in glorious conflict!")
							elif squad > 0:
								print "The %s is dead.\n" % fatal
								squad.remove(fatal)
								print squad
							else:
								dead("You have been annihilated!")
						else:
							dead("You have been annihilated")
					print "The squad takes out the Mechanoid scum.\n"
					print squad
					laser_cannon()
	
	elif choice == "2":
		print "Your team takes position and aims for the shot."
		print "You realsise there are 4 Mechs!"
		print "Roll 8 or higher to register a kill.\n"
			
		mechs = 4
			
		while mechs and squad > 0:
			d1 = random.randint(1, 6)
			d2 = random.randint(1, 6)
			print d1, d2
			result = d1 + d2
			print "You roll a %d\n" % result
				
			if result > 7:
				print "A Mech has been slain!\n"
				mechs -= 1
			elif result <= 7:
				print "One of your squad was hit!"
				x = len(squad)-1
				fatal = squad[random.randint(0, x)]
					
				if fatal == "Commander":
					dead("You die in glorious conflict!")
				elif squad > 0:
					print "The %s is dead.\n" % fatal
					squad.remove(fatal)
					print squad
				else:
					dead("You have been anihilated!")
						
		print "The squad takes out the Mechanoid scum.\n"
		print squad
		laser_cannon()
			
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
	print "\nBack in the corridor you have a door opposite and" 
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
	print "They are beaten, tortured and broken but alive."
	print "Do you....\n"
	print "1. Rush over to free them?"
	print "2. Survey the room?"
	print "3. Return to free them later after the ship is liberated?\n"
	booby_trap_set = True
	
	choice = raw_input("> ")
	
	if choice == "1" or not booby_trap_set:
		x = len(squad) - 1
		fatal = squad[random.randint(0, x)]
		print "Your rashness has set off a booby trap!"
		
		if fatal == "Commander":
			dead("You sleep with the fishes!")
		elif x > 0:
			print "The %s is killed by the trap..." % fatal
			squad.remove(fatal)
			print squad
			booby_trap_set = False
			print "Make another choice."
			
			choice == raw_input("> ")
			
			if choice == "2" or not booby_trap_set:
				print "You employ caution and find a trap."
				booby_trap_set = False
				x = len(squad)
				if x > 1:
					guard = squad[0]
					print "You leave your %s with the casualties and vow vengence!" % guard
					squad.remove(guard)
					print squad				
					corridor1b()
				else:
					dead("You flee like the coward you are!")
					
			elif choice == "3" or not booby_trap_set:
				print "The prisoners are beaten but alive. You push onwards leaving a guard behind.\n"
				y = squad[0]
				squad.remove(y)
				print squad
				corridor1b()
			else:
				dead("You are consumed by fear...")
			
	elif choice == "2" or not booby_trap_set:
		print "You employ caution and find another booby trap."
		booby_trap_set = False
		
		x = len(squad)
		
		if x > 1:		
			guard = squad[0]
			print "You leave your %s with the casualties and vow vengence!" % guard
			squad.remove(guard)
			print squad
			corridor1b()
		else:
			dead("You are suffering from space sickness and cower in a corner...")
	
	elif choice == "3" or not booby_trap_set:
		
		x = len(squad)
		
		if x > 1:		
			guard = squad[0]
			print "You leave your %s with the casualties and vow vengence!" % guard
			squad.remove(guard)
			print squad
			corridor1b()
	else:
		dead("You have made a critical error commander!")
		
def safe_room1():
	print "The door opens and you find 2 Orcs!"
	print "They open fire and a hail of cannon swamps you."
	
	global squad
	x = len(squad)-1
	fatal = squad[random.randint(0, x)]
		
	if fatal == "Commander":
		dead("You are ended!")
	elif x > 0:
		print "The %s gets a hole blown in his chest!\n" % fatal
		squad.remove(fatal)
		print squad
	else:
		dead("You are wasted!")

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
	
	global squad
	
	print "You take cover with your men."
	print "Your team reports 2 Goblins ahead."
	print "Will you?...\n"
	print "1. Charge them down in a hail of fire?"
	print "2. Lob a photon grenade?"
	print "3. Utilise the platoon attack formation?"
		
	choice = raw_input("> ")
	
	if choice == "1":
		dead("You charge straight into a booby trap!")
	
	elif choice == "2":
		x = len(squad) - 1
		fatal = squad[random.randint(0, x)]
		
		if fatal == "Commander":
			dead("The grenade blows up in your face!")
		else:
			print "The grenade is faulty and detonates in your %s's hand.\n" % fatal
			squad.remove(fatal)
			print squad
			print "Make another call!\n"
		
			choice = raw_input("> ")
		
			if choice == "1":
				dead("You charge straight into a booby trap!")
			elif choice == "3":
				print "Your team takes position and aims for a shot."
				print "Roll 5 or higher to register a kill.\n"
			
				goblin = 2
			
				while goblin and squad > 0:
					d1 = random.randint(1, 6)
					d2 = random.randint(1, 6)
					print d1, d2
					result = d1 + d2
					print "You roll a %d\n" % result
				
					if result > 4:
						print "A goblin has been slain!\n"
						goblin -= 1
					elif result <= 4:
						print "One of your squad was hit!"
						x = len(squad)-1
						fatal = squad[random.randint(0, x)]
					
						if fatal == "Commander":
							dead("You die in glorious conflict!")
						elif squad > 0:
							print "The %s is dead.\n" % fatal
							squad.remove(fatal)
							print squad
						else:
							dead("You have been anihilated!")
						
				print "The squad takes out the Goblin scum.\n"
				print squad
				corridor1a()
			else:
				dead("Your instructions are unclear in battle.")
				
	elif choice == "3":
		print "Your team takes position and aims for a shot."
		print "Roll 5 or higher to register a kill.\n"
			
		goblin = 2
			
		while goblin and squad > 0:
			d1 = random.randint(1, 6)
			d2 = random.randint(1, 6)
			print d1, d2
			result = d1 + d2
			print "You roll a %d\n" % result
				
			if result > 4:
				print "A goblin has been slain!\n"
				goblin -= 1
			elif result <= 4:
				print "One of your squad was hit!"
				x = len(squad)-1
				fatal = squad[random.randint(0, x)]
					
				if fatal == "Commander":
					dead("You die in glorious conflict!")
				elif squad > 0:
					print "The %s is dead.\n" % fatal
					squad.remove(fatal)
					print squad
				else:
					dead("You have been anihilated!")
						
		print "The squad takes out the Goblin scum.\n"
		print squad
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
	print "3. Send in your men first?\n"
	
	global squad
	squad = ["Scout", "Tech", "Medic", "Sniper", "Commander"]
	print squad

	choice = raw_input("> ")
	
	if choice == "1":
		print "The Goblins have the advantage and you are supressed with laser fire."
		print "You resolve to move to cover."
		print "You roll 2D6."
		print "7+ means squad gets safely to cover."
		print "6 or less means 1 fatality.\n"
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		print d1, d2
		result = d1 + d2
		print "You roll a %d\n" % result
		
		if result > 6:
			print "All squad members make it to cover safely."
			corridor1()
		elif result <= 6:	
			fatal = squad[random.randint(0, 4)]
			if fatal == "Commander":
				dead("You die in glorious conflict!")
			else:
				print "You make it to cover. You squad checks in. The %s is dead.\n" % fatal
				squad.remove(fatal)
				print squad
				corridor1()
		else:
			dead("You are hacked down in gunfire!")
				
	elif choice == "2":
		corridor1()
	elif choice == "3":
		dead("Your men abandon you as a coward!")
	else:
		dead("Your instructions are unclear in battle!")
		
start()


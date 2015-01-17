#dicerolls.py
#contains functions for rolling dice and making dice pools

import random
from player import *

def makepool (die_tier, die_amt):
	pool = []
	for n in range(die_amt):
		pool.append(rolldx(die_tier))
	pool.sort()
	return pool
#makepool() takes in dice size and number of dice
#returns array of rolled dice
	
def rolldx (x):
	return random.randint(1, x)
#rolldx() takes in a die to roll
#returns rolled die
	
def pool_separate(dice_pool):
	current_tier = 1
	current_pool = []
	pool_of_pools = []
	for num in dice_pool:
		if(num == current_tier):
			current_pool.append(num)
		else:
			pool_of_pools.append(current_pool)
			current_tier = num
			current_pool = []
			current_pool.append(num)
	pool_of_pools.append(current_pool)
	return pool_of_pools
#pool_seperate() takes in array of dice
#returns array of individual matched dice
	
def pooling (die_tier, die_amt):
	return pool_separate(makepool(die_tier, die_amt))
#pooling() takes in dice tier and dice number
#returns results of pool_seperate() on inputs

def startPooling(entity):
	user_pool_choice = raw_input("choose your pool d6, d8, d10, or d12: ")
	
	if(user_pool_choice == "6"):
		return pooling(6, (entity.getChi()/6))
		
	elif(user_pool_choice == "8"):
                return pooling(8, (entity.getChi()/8))

	elif(user_pool_choice == "10"):
                return pooling(10, (entity.getChi()/10))

	elif(user_pool_choice == "12"):
                return pooling(12, (entity.getChi()/12))

	else:
		print "That is not a dice tier please select again"
		return startPooling(entity)
#startPooling()
#returns the results of pooling which is a sorted array of dice

def channel():
	return

def prep():
	return

def bend():
	return

def fight():
       encounter = makeEncounter()
       while (combat == 1):
              attack, defense = [], []
              dice = startPooling()
	      setAttack(dice, attack, defense)
	      selectTargets()
              combat = resolution()

class Skill():
       def __init__(name):
              self.name = name
              active = true

       def getAPcost():
              return 0

       def isPrep():
              return false
       
       def isChannel():
              return false

       def isBending():
              return false

       def refresh():
              active = true
       def isActive():
              return active

       def doSkillStuff(encounter):
              return false

class HealingSkill(Skill):
       def getAPcost():
              return 1
       def isPrep():
              return true;
       def doSkillStuff(encounter):
              currentHP = encounter.getPlayer.getHP
              encounter.getPlayer.setHP(currentHP + 1)
              return true


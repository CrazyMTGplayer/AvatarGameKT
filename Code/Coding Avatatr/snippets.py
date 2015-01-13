def makepool (die_tier, die_amt):
	pool = []
	for n in range(die_amt):
		pool.append(rolldx(die_tier))
	pool.sort()
	return pool
	
def rolldx (x):
	return random.randint(1, x)
	
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
	
def pooling (die_tier, die_amt):
	return pool_separate(makepool(die_tier, die_amt))

def d6pool():
       return pooling(6,8)
def d8pool():
       return pooling(8,6)

def d10pool():
       return pooling(10,5)
def d12pool():
       return pooling(12,4)
	
def startPooling():
	user_pool_choice = raw_input("choose your pool d6, d8, d10, or d12:")
	
	if(user_pool_choice == "6"):
		return d6pool()
		
	elif(user_pool_choice == "8"):
		return d8pool()
	elif(user_pool_choice == "10"):
		return d10pool()
	elif(user_pool_choice == "12"):
		return d12pool()
	else:
		print "stahp"
		return None

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

class Player():
       def __init__(ele, sty, stats):
              self.element = ele
              self.style = sty
              self.stat = stats
              self.maxHp = 40
              self.chi = 50
              self.ability_p = 0
              self.combo_p = 0
              self.skills = []
              self.hp = 50

       def setFightSkills(skill_list):
              self.skills = skill_list

       def getFightSkills():
              return skills

       def setAP(ap):
              self.ability_p = ap

       def getAP():
              return ap

       def setCP(cp):
              self.combo_p = cp

       def getCP():
              return cp
       
       def resetHP():
              self.hp = self.maxHp
              
       def getHP():
              return self.hp
       
       def setHP(newHP)
              self.hp = newHP


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
       def isActive:
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

class monster():
	def __init__(maxAttack, maxDefense, maxSpeed):
		self.maxAttack = maxAttack
		self.maxDefense = maxDefense
		self.maxSpeed = maxSpeed
		self.currentAttack = 0
		self.currentDefense = 0
		self.currentSpeed = 0
		self.currentActivation = 0
		self.active = false

	def getActivationLimit():
		return 15
	
	def rollStats():
		self.currentAttack = rolldx(maxAttack)
		self.currentDefense = rolldx(maxDefense)
		self.currentSpeed = rolldx(maxSpeed)
		self.currentActivation = currentActivation + currentSpeed
		active = checkActivation()
	def isActive():
		return active
	def checkActivation():
		if(currentActivation >= getActivationLimit):
			currentActivation = 0
			return true
		else:
			return false

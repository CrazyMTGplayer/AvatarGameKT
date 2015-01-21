#player.py
#holds player parent class and eventual bending children

class Player():
       def __init__(self, ele, sty, stats, name):
              self.element = ele
              self.style = sty
              self.stat = stats
              self.name = name
              self.maxHp = 40
              self.chi = 50
              self.ability_p = 0
              self.combo_p = 0
              self.skills = []
              self.hp = self.resetHP

       def setFightSkills(self, skill_list):
              self.skills = skill_list

       def getFightSkills(self):
              return skills

       def setAP(self, ap):
              self.ability_p = ap

       def getAP(self):
              return ap

       def setChi(self, upgrade):
              self.chi += upgrade

       def getChi(self):
              return self.chi

       def setCP(self, cp):
              self.combo_p = cp

       def getCP(self):
              return cp

       def resetHP(self):
              self.hp = self.maxHp

       def getHP(self):
              return self.hp

       def setHP(self, newHP):
              self.hp = newHP

       def getName(self):
              return self.name

def makePlayer():
	user_element = raw_input("choose (1)airbender, (2)firebender, (3)waterbender, (4)earthbender: ")

	if (user_element == "1" or user_element == "airbender" or user_element =="air"):
		name = raw_input ("Name of player: ")
		return Player("air", 1, [2,3,1,2], name)
	elif (user_element == "2" or user_element == "firebender" or user_element =="fire"):
		name = raw_input ("Name of player: ")
		return Player("air", 1, [2,2,3,1], name)
	elif (user_element == "3" or user_element == "waterbender" or user_element =="water"):
		name = raw_input ("Name of player: ")
		return Player("air", 1, [1,2,2,3], name)
	elif (user_element == "4" or user_element == "earthbender" or user_element =="earth"):
		name = raw_input ("Name of player: ")
		return Player("air", 1, [3,1,2,2], name)
	else:
		print "Please try again!"
		return makePlayer()

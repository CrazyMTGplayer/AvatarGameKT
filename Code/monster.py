#monster.py
#holds monster parent class that will allow for monster generation

from dicerolls import *

class Monster():
    def __init__(self, maxAttack, maxDefense, maxSpeed, maxHP):
        self.maxAttack = maxAttack
        self.maxDefense = maxDefense
        self.maxSpeed = maxSpeed
        #max of the dice used for monster rolls
        self.currentAttack = 0 
        self.currentDefense = 0 
        self.currentSpeed = 0 
        self.currentActivation = 0 
        #initializes base monster
        self.active = False
        #cannot act until set
        self.hp = maxHP

    def getActivationLimit(self):
        return 15
    #getActivationLimit() set to 15 for now
    #is used as threshold for enemy attacking
    
    def rollStats(self):
        self.setAtk(rolldx(self.maxAttack))
        self.setDef(rolldx(self.maxDefense))
        self.setSpd(rolldx(self.maxSpeed))
        #roll atk/def values for combat
        self.setCurrentActivation(self.getCurrentActivation() +self.getSpd())
        active = self.checkActivation()
        #builds up activation over combat calls
        #if activation is true then monster 
        #will be able to attack on a given round
    #rollStats() rolls monster stats during combat

    def getAtk(self):
        return self.currentAttack
    def setAtk(self, newAtk):
        self.currentAttack = newAtk
    #get and set Atk()

    def getDef(self):
        return self.currentDefense
    def setDef(self, newDef):
        self.currentDefense = newDef
    #get and set Def()

    def getSpd(self):
        return self.currentSpeed
    def setSpd(self, newSpd):
        self.currentSpeed = newSpd
    #get and set Spd()

    def getActive(self):
        return self.active
    #getActive()

    def setActive(self, newActive):
        self.active = newActive
    #setActive()

    def getCurrentActivation(self):
        return self.currentActivation
    #getCurrentActivation

    def setCurrentActivation(self, newActive):
        self.currentActivation = newActive

    def zeroCurrentActivation(self):
        self.currentActivation = 0
    #zeroCurrentActivation()

    def checkActivation(self):
        if(self.getCurrentActivation >= self.getActivationLimit):
            self.zeroCurrentActivation()
            return True
        else:
            return False
    #checkActivation()

def makeMonster(attack, defense, speed, hp):
    monster = Monster(attack, defense, speed, hp)
    monster.rollStats()
    return monster

#monster.py
#holds monster parent class that will allow for monster generation

from dicerolls import *

class Monster():
  def __init__(self, maxAttack, maxDefense, maxSpeed):
    self.maxAttack = maxAttack
    self.maxDefense = maxDefense
    self.maxSpeed = maxSpeed
    self.currentAttack = 0 
    self.currentDefense = 0 
    self.currentSpeed = 0 
    self.currentActivation = 0 
    self.active = False
    self.hp = 40

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
                        return True
                else:
                        return False


#player.py
#holds player parent class and eventual bending children

class Player():
       def __init__(self, ele, sty, stats):
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

       def setChi(upgrade):
              self.chi += upgrade

       def getChi(self):
              return self.chi

       def setCP(cp):
              self.combo_p = cp

       def getCP():
              return cp

       def resetHP():
              self.hp = self.maxHp

       def getHP():
              return self.hp

       def setHP(newHP):
              self.hp = newHP


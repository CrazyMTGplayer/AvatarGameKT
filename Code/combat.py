#combat.py
#holds combat function and all the phases of combat

from dicerolls import *
from player import *
from monster import *

def combat(player):
#main game loop
  monster = makeMonster(2, 2, 2, 20)#makes dummy monster to pull health from

  p2 = (2,2,2,2)#locked set for monster for testing
  p1hp,p2hp = (player.maxHp, monster.hp)#pull data from player/monster
  hp = [p1hp,p2hp]#needs edit for multiple monsters
  comboPoints = [0,0]#combo points for groups of mobs is probably ok

  #this section should be the start of an encounter class.
  #encounter class will generate monsters based on input difficulty
  #then pull data from player class for the fight
  #then allow for skill selection from the player

  while True:
  #start of an encounter
    #print "inside encounter"
    if(p1hp <= (comboPoints[1] * 2)):
        print player.getName() + " loses"
	return
    if(p2hp <= (comboPoints[0] * 2)):
        print player.getName() + " wins"
	return

    if(p1hp <= 0):
      print player.getName() + " loses"
      return
    if(p2hp <= 0):
      print player.getName() + " wins"
      return

    p1 = bendingPhase(player) 
    print "p1",p1
    print "p2",p2
    #currently p1/p2 are just sets of dice

    [cp,hp,ap] = resolutionPhase(p1,p2, p1hp, p2hp)
    comboPoints = map(lambda x,y:x+y,comboPoints,cp)

    p1hp,p2hp = hp[0],hp[1]
    print "cp:"+str(comboPoints),"hp:"+str(hp), "ap:"+str(ap)

    #print "end of encounter"
    #general flow of an encounter without skills
#combat() does things with combat

def choosePair(pairs):
  for i,pair in enumerate(pairs):
    i += 1
    print i, pair
  choice = int(raw_input("choose your die: "))
  return pairs[choice - 1]
#choosePair allows you to select the dice you want to use
#probably should be in player class to allow for different benders?
#are other bender types going to inherit from an overal palyer class?
#need to decide how different types are handled.
#player -> elements? or players with many functions.

def chooseAtkDef(rolls):
  attack = 0;
  defense = 0;
  for num in rolls:
    print num,
    choice = raw_input("(atk/def)? ")
    if choice == "atk":
      attack += num
    elif choice == "def":
      defense += num
  return (attack, defense)
#chooseAtkDef()
#also a player function that will allow you to select differently
#probably good idea to have parent player and children that inherit functions

def bendingPhase(player):
  pairs = startPooling(player)
  chosen = choosePair(pairs)
  print "you chose", chosen
  (attack, defense) = chooseAtkDef(chosen)
  set_ = chosen[0]
  #return atk,def, the num of your set, num elements in your set
  return (attack, defense, set_, len(chosen))
#bendingPhase() takes in entity (player or monster)
#allows player to choose their atk and def sets
#returns attack total, defense total, avg of set, and magnitude of set

def resolutionPhase(p1,p2,p1hp,p2hp):
  p1atk, p1def, p1set, p1len = p1
  p2atk, p2def, p2set, p2len = p2
  #dmg taken
  p1dmg = p2atk - p1def
  p2dmg = p1atk - p2def
  if p1dmg < 0:
    p1dmg = 0
  if p2dmg < 0:
    p2dmg = 0
  print "dmg:",p1dmg, p2dmg
  p1hp -= p1dmg
  p2hp -= p2dmg
  hp = (p1hp,p2hp)
  #action points based on dmg dealt - opponent's # of  matching die
  p1ap = p2dmg - p2set
  p2ap = p1dmg - p1set
  if p1ap < 0:
    p1ap = 0
  if p2ap < 0:
    p2ap = 0
  print "ap",p1ap,p2ap
  ap = p1ap,p2ap

  #combo points based on # of matching die
  if p1len > p2len:#player one gets a combo point
    combo = [1,0]
  elif p1len < p2len:#player two gets a combo point
    combo = [0,1]
  else:
    combo = [0,0]#no combo points awarded

  #return updated combo, hp, and ap
  return combo, hp, ap
#resolutionPhase() takes care of resolution phase
#damage calculation, action point assignment, combo point assignment
#POINT only works for one on one. Rules still don't support multiple target

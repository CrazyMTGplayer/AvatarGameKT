from snippets import *

def main():
#main game loop
  player = Player(0,0,0)
  monster = Monster(0,0,0)

  p2 = (2,2,2,2)
  p1hp,p2hp = (player.maxHp, monster.hp)
  hp = [p1hp,p2hp]
  comboPoints = [0,0]
  while True:
#start of an encounter
    if(p1hp <= 0):
      print "player 2 wins"
      return
    if(p2hp <= 0):
      print "player 1 wins"
      return
    p1 = bendingPhase()
    print "p1",p1
    print "p2",p2
    [cp,hp,ap] = resolutionPhase(p1,p2, p1hp, p2hp)
    comboPoints = map(lambda x,y:x+y,comboPoints,cp)
    p1hp,p2hp = hp[0],hp[1]
    print "cp:"+str(comboPoints),"hp:"+str(hp), "ap:"+str(ap)
#end of an encounter

def choosePair(pairs):
  for i,pair in enumerate(pairs):
    i += 1
    print i, pair
  choice = int(raw_input("choose your die: "))
  return pairs[choice - 1]

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

def bendingPhase():
  pairs = startPooling()
  chosen = choosePair(pairs)
  print "you chose", chosen
  (attack, defense) = chooseAtkDef(chosen)
  set_ = chosen[0]
#return atk,def, the num of your set, num elements in your set
  return (attack, defense, set_, len(chosen))


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
  if p1len > p2len:
    combo = [1,0]
  elif p1len < p2len:
    combo = [0,1]
  else:
    combo = [0,0]
#return updated combo, hp, and ap
  return combo, hp, ap

if __name__ == "__main__":
  main()

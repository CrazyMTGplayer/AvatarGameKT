from snippets import *

def main():
#main game loop
  while True:
    bendingPhase()
    resolutionPhase()

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
  print "atk:"+str(attack),"def:"+str(defense)


def resolutionPhase():
  pass
    


if __name__ == "__main__":
  main()

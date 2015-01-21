#combat.py
#holds combat function and all the phases of combat

from dicerolls import *
from player import *
from monster import *

def combat(player):
#main game loop
    monsters = makeMob(3)#makes mob of input size for fight
    p2 = (2,2,2,2)#locked set for monster for testing
    monsterHP = []
    pcHP = (player.getHP())
    for i in monsters:
        monsterHP.append(i.getHP())
    #grabs HP for combat math
#debugstatement    print monsterHP

    comboPoints = [0,0]#zeros out both sides combo points

    #this section should be the start of an encounter class.
    #encounter class will generate monsters based on input difficulty
    #then pull data from player class for the fight
    #then allow for skill selection from the player

    while True:
    #start of an encounter
        #print "inside encounter"i
        enemyHP = mobHealth(monsterHP)
        if(pcHP <= (comboPoints[1] * 2)):
            print player.getName() + " loses"
            return

        if(enemyHP <= (comboPoints[0] * 2)):
            print player.getName() + " wins"
            return
#not sure how players combo points allow them to win with multiple enemies

        if(pcHP <= 0):
            print player.getName() + " loses"
            return

#        total = reduce(lambda x,y: x+y, monsterHP)
#        print total
#creates total of monster health for combat math

        if(enemyHP <= 0):
            print player.getName() + " wins"
            return

        player = bendingPhase(player) 
        print "player",player
        print "p2",p2
        #currently player/p2 are just sets of dice

        [cp,hp,ap] = resolutionPhase(player,p2, pcHP, p2hp)
        comboPoints = map(lambda x,y:x+y,comboPoints,cp)

        pcHP,p2hp = hp[0],hp[1]
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

def resolutionPhase(player,p2,pcHP,p2hp):
    playeratk, playerdef, playerset, playerlen = player
    p2atk, p2def, p2set, p2len = p2
    #dmg taken
    playerdmg = p2atk - playerdef
    p2dmg = playeratk - p2def
    if playerdmg < 0:
        playerdmg = 0
    if p2dmg < 0:
        p2dmg = 0
    print "dmg:",playerdmg, p2dmg
    pcHP -= playerdmg
    p2hp -= p2dmg
    hp = (pcHP,p2hp)
    #action points based on dmg dealt - opponent's # of    matching die
    playerap = p2dmg - p2set
    p2ap = playerdmg - playerset
    if playerap < 0:
        playerap = 0
    if p2ap < 0:
        p2ap = 0
    print "ap",playerap,p2ap
    ap = playerap,p2ap

    #combo points based on # of matching die
    if playerlen > p2len:#player one gets a combo point
        combo = [1,0]
    elif playerlen < p2len:#player two gets a combo point
        combo = [0,1]
    else:
        combo = [0,0]#no combo points awarded

    #return updated combo, hp, and ap
    return combo, hp, ap
#resolutionPhase() takes care of resolution phase
#damage calculation, action point assignment, combo point assignment
#POINT only works for one on one. Rules still don't support multiple target

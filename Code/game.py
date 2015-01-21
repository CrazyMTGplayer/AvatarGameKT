#game.py
#main function that calls everything for running

from player import *
from newcombat import combat

if __name__ == "__main__":
  player = makePlayer()
  combat(player)

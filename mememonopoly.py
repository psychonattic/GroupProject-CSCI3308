import random, sys, pygame, time, copy
from pygame.locals import *
from player import Player
from gameboard import *
from Space import *



myplayer = Player(1,1,1)
print myplayer.money

thisspace = GoSpace("go","./images/go","gospace")
thisspace.display()

def main():
	board = GameBoard(600,20) #boardsize, fps 
	board.startScreen()
	while True:
		if board.run() == False:
			break
		board.fpsClock.tick(board.Framepersecond) #limits how fast the screen can updat by framepersecond

		

main()

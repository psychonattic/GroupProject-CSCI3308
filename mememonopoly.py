import random, sys, pygame, time, copy
from pygame.locals import *
from player import Player

Framepersecond = 20 #frames per second
boardsize = 600 #height and width of the board
cornersize = 2*(boardsize/11) #height and width of corner board pieces
edgewidth = (boardsize/11) #width of non-corner board pieces
edgeheight = 2*(boardsize/11) #height of non-corner board pieces

player1 = Player(0,0,0)
print player1.money


def main():
	pygame.init() #initializes the board
	fpsClock = pygame.time.Clock() #keeps track of how fast the screen is updating
	DISPLAY = pygame.display.set_mode((boardsize, boardsize))
	pygame.display.set_caption('Meme Monopoly') 
	#boardImage = pygame.image.load('monopoly.png')
	#boardgamebg = pygame.image.load('monopoly.png')

	while (True):
		for event in pygame.event.get():
			if (event.type == QUIT):
				pygame.quit()
				sys.exit()


		pygame.display.update()
		fpsClock.tick(Framepersecond) #limits how fast the screen can update by framepersecond

main()
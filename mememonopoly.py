import random, sys, pygame, time, copy
from pygame.locals import *
from player import Player

Framepersecond = 20 #frames per second
boardsize = 600 #height and width of the board
cornersize = 2*(boardsize/11) #height and width of corner board pieces
edgewidth = (boardsize/11) #width of non-corner board pieces
edgeheight = 2*(boardsize/11) #height of non-corner board pieces
BLACK      = (  0,   0,   0)
WHITE      = (255, 255, 255)
GREEN      = (  0, 155,   0)
TEXTCOLOR = BLACK
BGCOLOR = GREEN

player1 = Player(0,0,0)
print player1.money


def main():
	global DISPLAY
	pygame.init() #initializes the board
	fpsClock = pygame.time.Clock() #keeps track of how fast the screen is updating
	DISPLAY = pygame.display.set_mode((boardsize, boardsize))
	DISPLAY.fill(WHITE)
	pygame.display.set_caption('Meme Monopoly') 
	
    #newGameRect = newGameSurf.get_rect()
	#boardImage = pygame.image.load('monopoly.png')
	#boardgamebg = pygame.image.load('monopoly.png')
	startScreen()
	while True:
		run()


		pygame.display.update()
		fpsClock.tick(Framepersecond) #limits how fast the screen can updat by framepersecond

def startScreen():
	STARTFONT = pygame.font.Font('freesansbold.ttf', 32)
	newGameSurf = STARTFONT.render('New Game', True, TEXTCOLOR, BGCOLOR)
	newGameRect = newGameSurf.get_rect()
	newGameRect.center = (int(boardsize / 2), int(boardsize / 2))
	DISPLAY.blit(newGameSurf,newGameRect)
	pygame.display.update()
	while True:
		DISPLAY.blit(newGameSurf,newGameRect)
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				if newGameRect.collidepoint((mousex, mousey)):
					print "collided"
					return False
					break
					#NOTCOLLIDED = False
				#return False
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

	#DISPLAY.blit(newGameSurf,newGameRect)
           





def run():
	#print "running main game loop"
	#startScreen()
	GAMEFONT = pygame.font.Font('freesansbold.ttf', 32)
	beginSurf = GAMEFONT.render('Mod Monopoly', True, TEXTCOLOR, BGCOLOR)
	beginGameRect = beginSurf.get_rect()
	beginGameRect.center = (int(boardsize / 2), int(boardsize / 2))
	DISPLAY.blit(beginSurf,beginGameRect)
	
		

main()
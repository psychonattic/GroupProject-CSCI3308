import random, sys, pygame, time, copy
from pygame.locals import *
from player import Player

Framepersecond = 20 #frames per second
boardsize = 700 #height and width of the board
cornersize = 2*(boardsize/11) #height and width of corner board pieces
edgewidth = (boardsize/11) #width of non-corner board pieces
edgeheight = 2*(boardsize/11) #height of non-corner board pieces
BLACK      = (  0,   0,   0)
WHITE      = (255, 255, 255)
GREEN      = (  0, 155,   0)
TEXTCOLOR = WHITE
BGCOLOR = BLACK

#player1 = Player(0,0,0)
#print player1.money


def main():
	global DISPLAY, GAMEFONT, fpsClock
	pygame.init() #initializes the board
	fpsClock = pygame.time.Clock() #keeps track of how fast the screen is updating
	GAMEFONT = pygame.font.Font('freesansbold.ttf', 32)
	DISPLAY = pygame.display.set_mode((boardsize, boardsize))
	DISPLAY.fill(BLACK)
	pygame.display.set_caption('Mod Monopoly') 
	#boardImage = pygame.image.load('monopoly.png')
	#boardgamebg = pygame.image.load('monopoly.png')
	startScreen()
	while True:
		if run() == False:
			break
		fpsClock.tick(Framepersecond) #limits how fast the screen can updat by framepersecond


def startScreen():
	STARTFONT = pygame.font.Font('freesansbold.ttf', 25)
	newGameStart = STARTFONT.render('Start', True, TEXTCOLOR, BGCOLOR)
	newGameRect = newGameStart.get_rect()
	newGameRect.center = (int(boardsize / 4), (boardsize-(newGameRect.height)))
	newGameExit = STARTFONT.render('Exit', True, TEXTCOLOR, BGCOLOR)
	newGameExitRect = newGameExit.get_rect()
	newGameExitRect.center = (int(3*(boardsize / 4)), (boardsize-(newGameRect.height)))
	text1 = "Welcome to Mod-opoly!"
	text2 = "Click 'Start' to continue or 'Exit' to quit"
	screen_text1 = STARTFONT.render(text1, True, WHITE)
	screen_text2 = STARTFONT.render(text2, True, WHITE)
	while True:
		DISPLAY.blit(screen_text1, [boardsize/4,boardsize/4])
		DISPLAY.blit(screen_text2, [boardsize/8,boardsize/2])
		DISPLAY.blit(newGameStart,newGameRect)
		DISPLAY.blit(newGameExit,newGameExitRect)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				if newGameRect.collidepoint((mousex, mousey)):
					print "collided"
					DISPLAY.fill(BLACK)
					return False
				elif newGameExitRect.collidepoint((mousex,mousey)):
					print "exit"
					sys.exit()

			

def run(): #main game loop - currently just has a quit button
	beginSurf = GAMEFONT.render('Quit', True, TEXTCOLOR, BGCOLOR)
	beginGameRect = beginSurf.get_rect()
	beginGameRect.center = (int(boardsize / 2), boardsize-(beginGameRect.height))
	DISPLAY.blit(beginSurf,beginGameRect)
	pygame.display.update()
	fpsClock.tick(Framepersecond)
	for event in pygame.event.get():
			if event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				if beginGameRect.collidepoint((mousex, mousey)):
					return False

	
		

main()
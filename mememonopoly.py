import random, sys, pygame, time, copy
from pygame.locals import *
from player import Player
from gameboard import *

# Framepersecond = 20 #frames per second
# boardsize = 700 #height and width of the board
# cornersize = 2*(boardsize/11) #height and width of corner board pieces
# edgewidth = (boardsize/11) #width of non-corner board pieces
# edgeheight = 2*(boardsize/11) #height of non-corner board pieces
# BLACK      = (  0,   0,   0) 
# WHITE      = (255, 255, 255)
# GREEN      = (  0, 155,   0)
# TEXTCOLOR = WHITE
# BGCOLOR = BLACK

#player1 = Player(0,0,0)
#print player1.money


def main():
	board = GameBoard(700,20)
	#boardImage = pygame.image.load('monopoly.png')
	#boardgamebg = pygame.image.load('monopoly.png')
	board.startScreen()
	while True:
		if board.run() == False:
			break
		board.fpsClock.tick(board.Framepersecond) #limits how fast the screen can updat by framepersecond


# def startScreen():
# 	global DISPLAY, GAMEFONT, fpsClock
# 	pygame.init() #initializes the board
# 	fpsClock = pygame.time.Clock() #keeps track of how fast the screen is updating
# 	GAMEFONT = pygame.font.Font('freesansbold.ttf', 32)
# 	DISPLAY = pygame.display.set_mode((boardsize, boardsize))
# 	DISPLAY.fill(BLACK)
# 	pygame.display.set_caption('Mod Monopoly') 
# 	STARTFONT = pygame.font.Font('freesansbold.ttf', 25)  #font for start screen
# 	newGameStart = STARTFONT.render('Start', True, TEXTCOLOR, BGCOLOR) #renders start button
# 	newGameRect = newGameStart.get_rect() #gets the rect value of start button
# 	newGameRect.center = (int(boardsize / 4), (boardsize-(newGameRect.height))) #places start button on botton of the screen
# 	newGameExit = STARTFONT.render('Exit', True, TEXTCOLOR, BGCOLOR) #renders exit button
# 	newGameExitRect = newGameExit.get_rect() #gets the exit button rect value
# 	newGameExitRect.center = (int(3*(boardsize / 4)), (boardsize-(newGameRect.height))) #puts exit button on bottom of the screen
# 	text1 = "Welcome to Mod-opoly!" #welcome message
# 	text2 = "Click 'Start' to continue or 'Exit' to quit" #instructions message
# 	screen_text1 = STARTFONT.render(text1, True, WHITE) #renders welcome message
# 	screen_text2 = STARTFONT.render(text2, True, WHITE) #render instruction message
# 	while True:
# 		DISPLAY.blit(screen_text1, [boardsize/4,boardsize/4]) #displays welcome message
# 		DISPLAY.blit(screen_text2, [boardsize/8,boardsize/2]) #displays instruction message
# 		DISPLAY.blit(newGameStart,newGameRect) #display start button
# 		DISPLAY.blit(newGameExit,newGameExitRect) #display exit button
# 		pygame.display.update() #updates the screen
# 		for event in pygame.event.get():
# 			if event.type == MOUSEBUTTONUP:  #checks for mouse click
# 				mousex, mousey = event.pos #gets coordinates of mouse click
# 				if newGameRect.collidepoint((mousex, mousey)): #checks if mouse click is in start button
# 					print "collided"
# 					DISPLAY.fill(BLACK) #resets the screen
# 					return False #exits start screen
# 				elif newGameExitRect.collidepoint((mousex,mousey)): #checks if mouse click is in exit button
# 					print "exit"
# 					sys.exit() #exits the game

			



	
		

main()
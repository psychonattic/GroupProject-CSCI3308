import random, sys, pygame, time, copy
from pygame.locals import *
class GameBoard:

	def __init__(self, boardsize,Framepersecond):
		pygame.init()
		self.boardsize = boardsize
		self.Framepersecond = Framepersecond
		self.DISPLAY = pygame.display.set_mode((boardsize, boardsize))
		self.GAMEFONT = pygame.font.Font('freesansbold.ttf', 32)
		self.fpsClock = pygame.time.Clock()
		self.cornersize = 1.5*(boardsize/12) #height and width of corner board pieces
		self.edgewidth = (boardsize/12) #width of non-corner board pieces
		self.edgeheight = 1.5*(boardsize/12) #height of non-corner board pieces
		self.board =pygame.image.load("Game Images/basicboard.jpg")
		self.corner_top_left = pygame.image.load("Game Images/corner_top_left.jpg")
		self.corner_top_right = pygame.image.load("Game Images/corner_top_right.jpg")
		self.corner_bottom_left = pygame.image.load("Game Images/corner_bottom_left.jpg")
		self.corner_bottom_right = pygame.image.load("Game Images/corner_bottom_right.jpg")	
		self.top = pygame.image.load("Game Images/top.jpg")	

	global BLACK, WHITE, GREEN, RED, TEXTCOLOR, BGCOLOR
	BLACK = (  0,   0,   0) 
	WHITE = (255, 255, 255)
	GREEN = (  0, 155,   0)
	RED =   (255,   0,   0)
	TEXTCOLOR = WHITE
	BGCOLOR = BLACK


	def run(self): #main game loop - currently just has a quit button
		beginSurf = self.GAMEFONT.render('Quit', True, TEXTCOLOR, BGCOLOR) #renderes quit button
		beginGameRect = beginSurf.get_rect() #gets rect value of quit button
		beginGameRect.center = (int(self.boardsize / 2), self.boardsize/2) #centers quit button
		self.drawBoard()
		self.DISPLAY.blit(beginSurf,beginGameRect) #displays quit button		self.drawBoard()
		pygame.display.update() #updates the screen
		self.fpsClock.tick(self.Framepersecond)
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONUP: #checks for mouse click
				mousex, mousey = event.pos #saves x,y values of mouse click
				if beginGameRect.collidepoint((mousex, mousey)): #checks if mouse click is in quit button
					self.startScreen() #quits the run loop


	def startScreen(self):
		self.DISPLAY.fill(BLACK)
		pygame.display.set_caption('Mod Monopoly') 
		STARTFONT = pygame.font.Font('freesansbold.ttf', 25)  #font for start screen
		newGameStart = STARTFONT.render('Start', True, TEXTCOLOR, BGCOLOR) #renders start button
		newGameRect = newGameStart.get_rect() #gets the rect value of start button
		newGameRect.center = (int(self.boardsize / 4), (self.boardsize-(newGameRect.height))) #places start button on botton of the screen
		newGameExit = STARTFONT.render('Exit', True, TEXTCOLOR, BGCOLOR) #renders exit button
		newGameExitRect = newGameExit.get_rect() #gets the exit button rect value
		newGameExitRect.center = (int(3*(self.boardsize / 4)), (self.boardsize-(newGameRect.height))) #puts exit button on bottom of the screen
		text1 = "Welcome to Mod-opoly!" #welcome message
		text2 = "Click 'Start' to continue or 'Exit' to quit" #instructions message
		screen_text1 = STARTFONT.render(text1, True, WHITE) #renders welcome message
		screen_text2 = STARTFONT.render(text2, True, WHITE) #render instruction message
		while True:
			self.DISPLAY.blit(screen_text1, [self.boardsize/4,self.boardsize/4]) #displays welcome message
			self.DISPLAY.blit(screen_text2, [self.boardsize/8,self.boardsize/2]) #displays instruction message
			self.DISPLAY.blit(newGameStart,newGameRect) #display start button
			self.DISPLAY.blit(newGameExit,newGameExitRect) #display exit button
			pygame.display.update() #updates the screen
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONUP:  #checks for mouse click
					mousex, mousey = event.pos #gets coordinates of mouse click
					if newGameRect.collidepoint((mousex, mousey)): #checks if mouse click is in start button
						print "collided"
						self.DISPLAY.fill(BLACK) #resets the screen
						return False #exits start screen
					elif newGameExitRect.collidepoint((mousex,mousey)): #checks if mouse click is in exit button
						print "exit"
						sys.exit() #exits the game

	def drawBoard(self):
		endpoint = self.boardsize-self.cornersize #marks where to stop loop
	#	self.DISPLAY.blit(self.board,(0,0)) 
		pygame.draw.rect(self.DISPLAY,GREEN,(0,endpoint,self.cornersize,self.cornersize),1) #draws bottom left corner
	#	self.DISPLAY.blit(self.corner_bottom_left,(0,endpoint))
		pygame.draw.rect(self.DISPLAY,GREEN,(endpoint,0,self.cornersize,self.cornersize),1) #draws top right corner
	#	self.DISPLAY.blit(self.corner_top_right,(endpoint,0))
		pygame.draw.rect(self.DISPLAY,GREEN,(endpoint,endpoint,self.cornersize,self.cornersize),1) #draws bottom right corner
	#	self.DISPLAY.blit(self.corner_bottom_right,(endpoint,endpoint))
		pygame.draw.rect(self.DISPLAY,GREEN,(0,0,self.cornersize,self.cornersize),1) #draws top left corner
	#	self.DISPLAY.blit(self.corner_top_left,(0,0))
		self.DISPLAY.blit(self.top,(self.cornersize,0))
		x = self.cornersize
		while x<(endpoint):
			pygame.draw.rect(self.DISPLAY,RED,(x,0,self.edgewidth,self.edgeheight),1) #draw rects between corners top
			x+=self.edgewidth
		xbottom = self.cornersize
		while xbottom < endpoint :
			pygame.draw.rect(self.DISPLAY,RED,(xbottom,endpoint,self.edgewidth,self.edgeheight),1) #draw rects between corners bottom
			xbottom+= self.edgewidth
		y = self.cornersize
		while y <(endpoint):
			pygame.draw.rect(self.DISPLAY,RED,(0,y,self.edgeheight,self.edgewidth),1) #draw rects between corners left
			y += self.edgewidth
		yright = self.cornersize
		while yright < endpoint :
			pygame.draw.rect(self.DISPLAY,RED,(endpoint,yright,self.edgeheight,self.edgewidth),1) #draw rects between corners right
			yright += self.edgewidth
		return 0

import random, sys, pygame, time, copy
from pygame.locals import *
from Space import *

class GameBoard:

	def __init__(self, boardsize,Framepersecond,spaces):
		pygame.init()
		self.boardsize = boardsize
		self.Framepersecond = Framepersecond
		self.spaces = spaces
		self.DISPLAY = pygame.display.set_mode((boardsize, boardsize),RESIZABLE)
		self.GAMEFONT = pygame.font.Font('freesansbold.ttf', 20)
		self.fpsClock = pygame.time.Clock()
		self.cornersize = 1.5*(boardsize/12.0) #height and width of corner board pieces
		self.edgewidth = 1.0*(boardsize/12.0) #width of non-corner board pieces
		self.edgeheight = 1.5*(boardsize/12.0) #height of non-corner board pieces
		

	global BLACK, WHITE, GREEN, RED, TEXTCOLOR, BGCOLOR
	BLACK = (  0,   0,   0) 
	WHITE = (255, 255, 255)
	GREEN = (  0, 155,   0)
	RED = (255,0,0)
	TEXTCOLOR = WHITE
	BGCOLOR = BLACK


	def run(self): #main game loop - currently just has a quit button
		#self.DISPLAY = pygame.display.set_mode((self.boardsize, self.boardsize),RESIZABLE)
		pygame.display.set_caption('Mod-opoly')
		beginSurf = self.GAMEFONT.render('Options', True, TEXTCOLOR, BGCOLOR) #renderes options button
		optionRect = beginSurf.get_rect() #gets rect value of options button
		optionRect.bottomright = (self.boardsize-self.cornersize, self.boardsize-self.cornersize) #puts options button in corner
		self.DISPLAY.blit(beginSurf,optionRect) #displays options button
		self.drawBoard()
		pygame.display.update() #updates the screen
		self.fpsClock.tick(self.Framepersecond)
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN: #checks for mouse click
				mousex, mousey = event.pos #saves x,y values of mouse click
				if optionRect.collidepoint((mousex, mousey)): #checks if mouse click is in options button
					self.optionScreen() #quits the run loop
				print self.getProperty(mousex,mousey)
                                if self.getProperty(mousex,mousey) > -1 and self.getProperty(mousex,mousey) < 40:
					self.spaces[self.getProperty(mousex,mousey)].display(self.boardsize,self.DISPLAY)
					#self.run()
				
			if (event.type == VIDEORESIZE): #ALL OF THIS DEALS WITH RESIZING ISSUES
				self.DISPLAY = pygame.display.set_mode((event.w,event.w),RESIZABLE)
				self.boardsize = event.w
				self.cornersize = 1.5*(self.boardsize/12.0) #height and width of corner board pieces
				self.edgewidth = 1.0*(self.boardsize/12.0) #width of non-corner board pieces
				self.edgeheight = 1.5*(self.boardsize/12.0) #height of non-corner board pieces
				fsize = int(self.boardsize*.04)
				self.GAMEFONT = pygame.font.Font('freesansbold.ttf', fsize)
				self.run()
			if(event.type == QUIT):
				sys.exit()

		
	def optionScreen(self):
		while True:
			self.DISPLAY.fill(BLACK)
			pygame.display.set_caption('Options')
			fontsize = int(self.boardsize*.04)
			STARTFONT = pygame.font.Font('freesansbold.ttf', fontsize)  #font for start screen

			optionsGame = STARTFONT.render('Options',True,TEXTCOLOR,BGCOLOR) #renders quit button
			optionGameRect = optionsGame.get_rect()
			optionGameRect.center = (int(self.boardsize / 2), (0+(optionGameRect.height)))

			quitGame = STARTFONT.render('Quit Game',True,TEXTCOLOR,BGCOLOR) #renders quit button
			quitGameRect = quitGame.get_rect()
			quitGameRect.center = (int(3*(self.boardsize / 4)), (self.boardsize/2-(quitGameRect.height)))

			returnGame = STARTFONT.render('Return to Game',True,TEXTCOLOR,BGCOLOR) #renders quit button
			returnGameRect = returnGame.get_rect()
			returnGameRect.center = (int(self.boardsize / 4), (self.boardsize/2-(returnGameRect.height)))
			#quitGameRect.center(0,0)
			#quitGameRect.center(int(self.boardsize/2),int(self.boardsize/2))
			self.DISPLAY.blit(optionsGame,optionGameRect)
			self.DISPLAY.blit(returnGame,returnGameRect)
			self.DISPLAY.blit(quitGame,quitGameRect) #display start button
			pygame.display.update() #updates the screen
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONUP:  #checks for mouse click
					mousex, mousey = event.pos #gets coordinates of mouse click
					if returnGameRect.collidepoint((mousex, mousey)): #checks if mouse click is in start button
						self.DISPLAY.fill(BLACK) #resets the screen
						return False #exits start screen
					if quitGameRect.collidepoint((mousex, mousey)): #checks if mouse click is in start button
						sys.exit()
				if (event.type == VIDEORESIZE): #ALL OF THIS DEALS WITH RESIZING ISSUES
					self.DISPLAY = pygame.display.set_mode((event.w,event.w),RESIZABLE)
					self.boardsize = event.w
					self.cornersize = 1.5*(self.boardsize/12.0) #height and width of corner board pieces
					self.edgewidth = 1.0*(self.boardsize/12.0) #width of non-corner board pieces
					self.edgeheight = 1.5*(self.boardsize/12.0) #height of non-corner board pieces
				if(event.type == QUIT):
					sys.exit()


	def startScreen(self):
		while True:
			self.DISPLAY.fill(BLACK)
			pygame.display.set_caption('Mod Monopoly') 
			fontsize = int(self.boardsize*.04)
			STARTFONT = pygame.font.Font('freesansbold.ttf', fontsize)  #font for start screen
			newGameStart = STARTFONT.render('Start', True, TEXTCOLOR, BGCOLOR) #renders start button
			newGameRect = newGameStart.get_rect() #gets the rect value of start button
			newGameRect.center = (int(3*(self.boardsize / 4)), (self.boardsize-(newGameRect.height))) #places start button on botton of the screen
			newGameExit = STARTFONT.render('Exit', True, TEXTCOLOR, BGCOLOR) #renders exit button
			newGameExitRect = newGameExit.get_rect() #gets the exit button rect value
			newGameExitRect.center = (int(self.boardsize / 4), (self.boardsize-(newGameRect.height))) #puts exit button on bottom of the screen
			text1 = "Welcome to Mod-opoly!" #welcome message
			text2 = "Click 'Start' to continue or 'Exit' to quit" #instructions message
			screen_text1 = STARTFONT.render(text1, True, WHITE) #renders welcome message
			screen_text2 = STARTFONT.render(text2, True, WHITE) #render instruction message
			self.DISPLAY.blit(screen_text1, [self.boardsize/4,self.boardsize/4]) #displays welcome message
			self.DISPLAY.blit(screen_text2, [self.boardsize/8,self.boardsize/2]) #displays instruction message
			self.DISPLAY.blit(newGameStart,newGameRect) #display start button
			self.DISPLAY.blit(newGameExit,newGameExitRect) #display exit button
			pygame.display.update() #updates the screen
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONUP:  #checks for mouse click
					mousex, mousey = event.pos #gets coordinates of mouse click
					if newGameRect.collidepoint((mousex, mousey)): #checks if mouse click is in start button
						print "start"
						self.DISPLAY.fill(BLACK) #resets the screen
						return False #exits start screen
					elif newGameExitRect.collidepoint((mousex,mousey)): #checks if mouse click is in exit button
						print "exit"
						sys.exit() #exits the game
				if (event.type == VIDEORESIZE): #ALL OF THIS DEALS WITH RESIZING ISSUES
					self.DISPLAY = pygame.display.set_mode((event.w,event.w),RESIZABLE)
					self.boardsize = event.w
					self.cornersize = 1.5*(self.boardsize/12.0) #height and width of corner board pieces
					self.edgewidth = 1.0*(self.boardsize/12.0) #width of non-corner board pieces
					self.edgeheight = 1.5*(self.boardsize/12.0) #height of non-corner board pieces
				if(event.type == QUIT):
					sys.exit()
					

	def drawBoard(self): #DRAWS THE BOARD EVERY TURN	
		ximage = int(self.edgewidth)
		yimage = int(self.edgeheight)
		endpoint = long(self.boardsize-self.cornersize)
                blitdest = [(endpoint,endpoint),(0,endpoint),(0,0),(endpoint,0)] #Array for blit destinations
                
                #Displays each corner piece
                for i in range(0,4):
                    corner = pygame.image.load(self.spaces[i*10].picture).convert() #Convert image to new pixel format
                    corner = pygame.transform.scale(corner,(yimage,yimage)) #Scale image
                    self.DISPLAY.blit(corner,blitdest[i]) #Display corner piece at blit destination
                    pygame.draw.rect(self.DISPLAY,BLACK,(blitdest[i][0],blitdest[i][1],self.cornersize,self.cornersize),2)
                
                #Displays each non-corner piece
                spacepos = long(endpoint-self.edgewidth) #start to the left of "Go" for bottom row
                for i in range(1,10)+range(11,20)+range(21,30)+range(31,40): #Skip edges
                    if i == 11:
                        #Start above Jail for left column
                        spacepos = long(endpoint-self.edgewidth)
                    elif i == 21 or i == 31:
                        #Start at the top corners for the other two sides
                        spacepos = long(self.cornersize)

                    image = pygame.image.load(self.spaces[i].picture).convert()
                    if i > 0 and i < 10:
                        image = pygame.transform.scale(image, (ximage, yimage)) #Scale by x, y for rows
                        self.DISPLAY.blit(image,(spacepos,endpoint))
                        pygame.draw.rect(self.DISPLAY,BLACK,(spacepos,endpoint,self.edgewidth,self.edgeheight),2)
                        spacepos -= self.edgewidth #Go from right to left by subtracting
                    elif i > 10 and i < 20:
                        image = pygame.transform.scale(image, (yimage, ximage)) #Scale by y, x for cols
                        self.DISPLAY.blit(image,(0,spacepos))
                        pygame.draw.rect(self.DISPLAY,BLACK,(0,spacepos,self.edgeheight,self.edgewidth),2)
                        spacepos -= self.edgewidth #Go from bottom to top
                    elif i > 20 and i < 30:
                        image = pygame.transform.scale(image, (ximage, yimage))
                        self.DISPLAY.blit(image, (spacepos,0))
                        pygame.draw.rect(self.DISPLAY,BLACK,(spacepos,0,self.edgewidth,self.edgeheight),2)
                        spacepos += self.edgewidth #Go from left to right
                    elif i > 30 and i <40:
                        image = pygame.transform.scale(image, (yimage, ximage))
                        self.DISPLAY.blit(image,(endpoint,spacepos))
                        pygame.draw.rect(self.DISPLAY,BLACK,(endpoint,spacepos,self.edgeheight,self.edgewidth),2)
                        spacepos += self.edgewidth #Go from top to bottom
                return 0


	def getProperty(self,mousex,mousey):  #Given a mouse position on the board, this will return the number of the property or -1 if not clicking on any property

		if(mousex<self.boardsize-(.3*self.cornersize) and mousex>self.boardsize-self.cornersize and mousey<self.boardsize-(.3*self.cornersize) and mousey>self.boardsize-self.cornersize):  #bottom 1
			return 0
		if(mousex<self.boardsize-self.cornersize and mousex>self.boardsize-self.cornersize-self.edgewidth and mousey<self.boardsize and mousey>self.boardsize-self.cornersize): #bottom 2
			return 1
		if(mousex<self.boardsize-self.cornersize-self.edgewidth and mousex>self.boardsize-self.cornersize-(2*self.edgewidth) and mousey<self.boardsize and mousey>self.boardsize-self.cornersize): #bottom 3
			return 2
		if(mousex<self.boardsize-self.cornersize-(2*self.edgewidth) and mousex>self.boardsize-self.cornersize-(3*self.edgewidth) and mousey<self.boardsize and mousey>self.boardsize-self.cornersize): #bottom 4
			return 3
		if(mousex<self.boardsize-self.cornersize-(3*self.edgewidth) and mousex>self.boardsize-self.cornersize-(4*self.edgewidth) and mousey<self.boardsize and mousey>self.boardsize-self.cornersize): #bottom 5
			return 4
		if(mousex<self.boardsize-self.cornersize-(4*self.edgewidth) and mousex>self.boardsize-self.cornersize-(5*self.edgewidth) and mousey<self.boardsize and mousey>self.boardsize-self.cornersize): #bottom 6
			return 5
		if(mousex<self.boardsize-self.cornersize-(5*self.edgewidth) and mousex>self.boardsize-self.cornersize-(6*self.edgewidth) and mousey<self.boardsize and mousey>self.boardsize-self.cornersize): #bottom 7
			return 6
		if(mousex<self.boardsize-self.cornersize-(6*self.edgewidth) and mousex>self.boardsize-self.cornersize-(7*self.edgewidth) and mousey<self.boardsize and mousey>self.boardsize-self.cornersize): #bottom 8
			return 7
		if(mousex<self.boardsize-self.cornersize-(7*self.edgewidth) and mousex>self.boardsize-self.cornersize-(8*self.edgewidth) and mousey<self.boardsize and mousey>self.boardsize-self.cornersize): #bottom 9
			return 8
		if(mousex<self.boardsize-self.cornersize-(8*self.edgewidth) and mousex>self.boardsize-self.cornersize-(9*self.edgewidth) and mousey<self.boardsize and mousey>self.boardsize-self.cornersize): #bottom 10
			return 9
		if(mousex<self.boardsize-self.cornersize-(9*self.edgewidth) and mousex>0 and mousey<self.boardsize and mousey>self.boardsize-self.cornersize): #bottom 11
			return 10

		if(mousex>0 and mousex < self.cornersize and mousey<self.boardsize-self.cornersize and mousey>self.boardsize-self.cornersize-self.edgewidth):
			return 11
		if(mousex>0 and mousex < self.cornersize and mousey<self.boardsize-self.cornersize-self.edgewidth and mousey>self.boardsize-self.cornersize-(2*self.edgewidth)):
			return 12
		if(mousex>0 and mousex < self.cornersize and mousey<self.boardsize-self.cornersize-(2*self.edgewidth) and mousey>self.boardsize-self.cornersize-(3*self.edgewidth)):
			return 13
		if(mousex>0 and mousex < self.cornersize and mousey<self.boardsize-self.cornersize-(3*self.edgewidth) and mousey>self.boardsize-self.cornersize-(4*self.edgewidth)):
			return 14
		if(mousex>0 and mousex < self.cornersize and mousey<self.boardsize-self.cornersize-(4*self.edgewidth) and mousey>self.boardsize-self.cornersize-(5*self.edgewidth)):
			return 15
		if(mousex>0 and mousex < self.cornersize and mousey<self.boardsize-self.cornersize-(5*self.edgewidth) and mousey>self.boardsize-self.cornersize-(6*self.edgewidth)):
			return 16
		if(mousex>0 and mousex < self.cornersize and mousey<self.boardsize-self.cornersize-(6*self.edgewidth) and mousey>self.boardsize-self.cornersize-(7*self.edgewidth)):
			return 17
		if(mousex>0 and mousex < self.cornersize and mousey<self.boardsize-self.cornersize-(7*self.edgewidth) and mousey>self.boardsize-self.cornersize-(8*self.edgewidth)):
			return 18
		if(mousex>0 and mousex < self.cornersize and mousey<self.boardsize-self.cornersize-(8*self.edgewidth) and mousey>self.boardsize-self.cornersize-(9*self.edgewidth)):
			return 19

		if(mousex>0 and mousex <self.cornersize and mousey>0 and mousey<self.cornersize): #top 2
			return 20
		if(mousex>self.cornersize and mousex <self.cornersize+self.edgewidth and mousey>0 and mousey<self.cornersize): #top 2
			return 21
		if(mousex>self.cornersize+self.edgewidth and mousex <self.cornersize+(2*self.edgewidth) and mousey>0 and mousey<self.cornersize): #top 3
			return 22
		if(mousex>self.cornersize+(2*self.edgewidth) and mousex <self.cornersize+(3*self.edgewidth) and mousey>0 and mousey<self.cornersize): #top 4
			return 23
		if(mousex>self.cornersize+(3*self.edgewidth) and mousex <self.cornersize+(4*self.edgewidth) and mousey>0 and mousey<self.cornersize): #top 5
			return 24
		if(mousex>self.cornersize+(4*self.edgewidth) and mousex <self.cornersize+(5*self.edgewidth) and mousey>0 and mousey<self.cornersize): #top 6
			return 25
		if(mousex>self.cornersize+(5*self.edgewidth) and mousex <self.cornersize+(6*self.edgewidth) and mousey>0 and mousey<self.cornersize): #top 7
			return 26
		if(mousex>self.cornersize+(6*self.edgewidth) and mousex <self.cornersize+(7*self.edgewidth) and mousey>0 and mousey<self.cornersize): #top 8
			return 27
		if(mousex>self.cornersize+(7*self.edgewidth) and mousex <self.cornersize+(8*self.edgewidth) and mousey>0 and mousey<self.cornersize): #top 9
			return 28
		if(mousex>self.cornersize+(8*self.edgewidth) and mousex <self.cornersize+(9*self.edgewidth) and mousey>0 and mousey<self.cornersize): #top 10
			return 29
		if(mousex>self.cornersize+(9*self.edgewidth) and mousex <self.boardsize and mousey>0 and mousey<self.cornersize): #top 10
			return 30

		if(mousex<self.boardsize and mousex >self.boardsize-self.cornersize and mousey>self.cornersize and mousey < self.cornersize + self.edgewidth):
			return 31
		if(mousex<self.boardsize and mousex >self.boardsize-self.cornersize and mousey>self.cornersize+self.edgewidth and mousey < self.cornersize + (2*self.edgewidth)):
			return 32
		if(mousex<self.boardsize and mousex >self.boardsize-self.cornersize and mousey>self.cornersize+(2*self.edgewidth) and mousey < self.cornersize + (3*self.edgewidth)):
			return 33
		if(mousex<self.boardsize and mousex >self.boardsize-self.cornersize and mousey>self.cornersize+(3*self.edgewidth) and mousey < self.cornersize + (4*self.edgewidth)):
			return 34
		if(mousex<self.boardsize and mousex >self.boardsize-self.cornersize and mousey>self.cornersize+(4*self.edgewidth) and mousey < self.cornersize + (5*self.edgewidth)):
			return 35
		if(mousex<self.boardsize and mousex >self.boardsize-self.cornersize and mousey>self.cornersize+(5*self.edgewidth) and mousey < self.cornersize + (6*self.edgewidth)):
			return 36
		if(mousex<self.boardsize and mousex >self.boardsize-self.cornersize and mousey>self.cornersize+(6*self.edgewidth) and mousey < self.cornersize + (7*self.edgewidth)):
			return 37
		if(mousex<self.boardsize and mousex >self.boardsize-self.cornersize and mousey>self.cornersize+(7*self.edgewidth) and mousey < self.cornersize + (8*self.edgewidth)):
			return 38
		if(mousex<self.boardsize and mousex >self.boardsize-self.cornersize and mousey>self.cornersize+(8*self.edgewidth) and mousey < self.cornersize + (9*self.edgewidth)):
			return 39
		return -1


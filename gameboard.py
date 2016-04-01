import random, sys, pygame, time, copy
from pygame.locals import *
from dice import *
class GameBoard:


	def __init__(self, boardsize,Framepersecond):
		pygame.init()
		self.boardsize = boardsize
		self.Framepersecond = Framepersecond
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
		pygame.display.set_caption('Mod-opoly')
		beginSurf = self.GAMEFONT.render('Options', True, TEXTCOLOR, BGCOLOR) #renderes options button
		optionRect = beginSurf.get_rect() #gets rect value of options button
		optionRect.bottomright = (self.boardsize-self.cornersize, self.boardsize-self.cornersize) #puts options button in corner
		self.DISPLAY.blit(beginSurf,optionRect) #displays options button
		self.drawBoard()
		pygame.display.update() #updates the screen
		self.fpsClock.tick(self.Framepersecond)
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONUP: #checks for mouse click
				mousex, mousey = event.pos #saves x,y values of mouse click
				if optionRect.collidepoint((mousex, mousey)): #checks if mouse click is in options button
					self.optionScreen() #quits the run loop
				print self.getProperty(mousex,mousey)
			if (event.type == VIDEORESIZE): #ALL OF THIS DEALS WITH RESIZING ISSUES
				self.DISPLAY = pygame.display.set_mode((event.w,event.w),RESIZABLE)
				self.boardsize = event.w
				self.cornersize = 1.5*(self.boardsize/12.0) #height and width of corner board pieces
				self.edgewidth = 1.0*(self.boardsize/12.0) #width of non-corner board pieces
				self.edgeheight = 1.5*(self.boardsize/12.0) #height of non-corner board pieces
				fsize = int(self.boardsize*.04)
				self.GAMEFONT = pygame.font.Font('freesansbold.ttf', fsize)
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
			newGameRect.center = (int(self.boardsize / 4), (self.boardsize-(newGameRect.height))) #places start button on botton of the screen
			newGameExit = STARTFONT.render('Exit', True, TEXTCOLOR, BGCOLOR) #renders exit button
			newGameExitRect = newGameExit.get_rect() #gets the exit button rect value
			newGameExitRect.center = (int(3*(self.boardsize / 4)), (self.boardsize-(newGameRect.height))) #puts exit button on bottom of the screen
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
						print "collided"
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
					
	
	



	def drawBoard(self): #DRAWS THE BORD EVERY TURN	
		ximage = int(self.edgewidth)
		yimage = int(self.edgeheight)
		endpoint = long(self.boardsize-self.cornersize)

		
		cbl = pygame.image.load("./images/corner_bottom_left.jpg").convert() #corner bottom left
		cbl = pygame.transform.scale(cbl,(yimage,yimage))
		self.DISPLAY.blit(cbl,(0,endpoint))

		cbr = pygame.image.load("./images/corner_bottom_right.jpg").convert() #corner bottom right
		cbr = pygame.transform.scale(cbr,(yimage,yimage))
		self.DISPLAY.blit(cbr,(endpoint,endpoint))

		ctr = pygame.image.load("./images/corner_top_right.jpg").convert() #corner top right
		ctr = pygame.transform.scale(ctr,(yimage,yimage))
		self.DISPLAY.blit(ctr,(endpoint,0))

		ctl = pygame.image.load("./images/corner_top_left.jpg").convert() #corner bottom left
		ctl = pygame.transform.scale(ctl,(yimage,yimage))
		self.DISPLAY.blit(ctl,(0,0))

		pygame.draw.rect(self.DISPLAY,BLACK,(0,endpoint,self.cornersize,self.cornersize),2)#bottom left
		pygame.draw.rect(self.DISPLAY,BLACK,(endpoint,0,self.cornersize,self.cornersize),2) #top left
		pygame.draw.rect(self.DISPLAY,BLACK,(endpoint,endpoint,self.cornersize,self.cornersize),2)#bottom right
		pygame.draw.rect(self.DISPLAY,BLACK,(0,0,self.cornersize,self.cornersize),2) #top right
		x = long(self.cornersize)
		count=1
		while x<(endpoint) and count<10: #loads the frames and pictures for the top row
			str1 = "./images/top"
			str1 = str1 + str(count) + ".jpg" #creates the right adress for the picture
			image = pygame.image.load(str1).convert()
			image = pygame.transform.scale(image, (ximage,yimage)) #scales the image
			self.DISPLAY.blit(image,(x,0)) #displays the image
			pygame.draw.rect(self.DISPLAY,BLACK,(x,0,self.edgewidth,self.edgeheight),2)
			x+=self.edgewidth
			count+=1
		xbottom = long(self.cornersize)
		count=1
		while xbottom < endpoint and count<10: #loads the frames and pictures for the bottom row
			str2 = "./images/bottom"
			str2 = str2 + str(count) + ".jpg" #creates the right adress for the picture
			image1 = pygame.image.load(str2).convert()
			image1 = pygame.transform.scale(image1, (ximage,yimage)) #scales the image
			self.DISPLAY.blit(image1,(xbottom,endpoint)) #displays the image
			pygame.draw.rect(self.DISPLAY,BLACK,(xbottom,endpoint,self.edgewidth,self.edgeheight),2)
			xbottom+= self.edgewidth
			count+=1
		y = long(self.cornersize)
		count=1
		while y <(endpoint) and count<10: #loads the frames and pictures for the left row
			str3 = "./images/left"
			str3 = str3 + str(count) + ".jpg" #creates the right adress for the picture
			image2 = pygame.image.load(str3).convert()
			image2 = pygame.transform.scale(image2, (yimage,ximage)) #scales the image
			self.DISPLAY.blit(image2,(0,y)) #displays the image
			pygame.draw.rect(self.DISPLAY,BLACK,(0,y,self.edgeheight,self.edgewidth),2)
			y += self.edgewidth
			count+=1
		yright = long(self.cornersize)
		count=1
		while yright < endpoint and count<10: #loads the frames and pictures for the right row
			str4 = "./images/right"
			str4 = str4 + str(count) + ".jpg" #creates the right adress for the picture
			image3 = pygame.image.load(str4).convert()
			image3 = pygame.transform.scale(image3, (yimage,ximage)) #scales the image
			self.DISPLAY.blit(image3,(endpoint,yright)) #displays the image
			pygame.draw.rect(self.DISPLAY,BLACK,(endpoint,yright,self.edgeheight,self.edgewidth),2)
			yright += self.edgewidth
			count+=1
		return 0



	def getProperty(self,mousex,mousey):  #Given a mouse position on the board, this will return the number of the property or -1 if not clicking on any property

		if(mousex<self.boardsize and mousex>self.boardsize-self.cornersize and mousey<self.boardsize and mousey>self.boardsize-self.cornersize):  #bottom 1
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


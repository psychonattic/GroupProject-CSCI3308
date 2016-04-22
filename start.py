import random, sys, pygame, time, copy
from pygame.locals import *
from Space import *
from gameboard import *
from player import *
import itertools
import os

class Start:

	global tokens, BLACK, WHITE, GREEN, RED, GRAY, TEXTCOLOR, BGCOLOR, NUMPLAYERS
	tokens = []
	BLACK = (  0,   0,   0) 
	WHITE = (255, 255, 255)
	GREEN = (  0, 155,   0)
	RED = (255,0,0)
	GRAY = (125, 125, 125)
	TEXTCOLOR = WHITE
	BGCOLOR = BLACK
	NUMPLAYERS = 0

	def __init__(self, boardsize):
		pygame.init()
		self.boardsize = boardsize
		self.DISPLAY = pygame.display.set_mode((boardsize, boardsize),RESIZABLE)
		self.GAMEFONT = pygame.font.Font('freesansbold.ttf', 20)
		self.MDGAMEFONT = pygame.font.Font('freesansbold.ttf', 25)
		self.LGGAMEFONT = pygame.font.Font('freesansbold.ttf', 33)

	def startnew(self):

		starting = True
		isselected = False

		welcome = self.LGGAMEFONT.render('Welcome to Modopoly!', True, TEXTCOLOR, BLACK) 	#renders welcome text
		welcomeRect = welcome.get_rect() 	#gets rect value of welcome text
		welcomeRect.topleft 	#puts welcome text in corner
		self.DISPLAY.blit(welcome,welcomeRect) 	#displays welcome text
		
		selecttxt = self.MDGAMEFONT.render('Select number of players:', True, TEXTCOLOR, BLACK) 	#renders selection text
		selecttxtRect = selecttxt.get_rect() 	#gets rect value of selection text
		selecttxtRect.topleft= ((self.boardsize/12), (self.boardsize/12)) 	#puts selection text in corner
		self.DISPLAY.blit(selecttxt,selecttxtRect) 	#displays selection text

		quitbutton = self.LGGAMEFONT.render(' QUIT ', True, TEXTCOLOR, GRAY) 	#renders quit button
		quitbuttonRect = quitbutton.get_rect() 	#gets rect value of selection text
		quitbuttonRect.bottomleft= (0, self.boardsize) 	#puts selection text in corner
		self.DISPLAY.blit(quitbutton,quitbuttonRect) 	#displays selection text
		
		num2 = self.MDGAMEFONT.render('  2  ', True, TEXTCOLOR, GRAY) 	#renders "2" button
		num2Rect = num2.get_rect() 	#gets rect value of "2" button
		num2Rect.topleft= (1*(self.boardsize/12), 2*(self.boardsize/12)) 	#places "2" button
		self.DISPLAY.blit(num2,num2Rect) 	#displays "2" button

		num3 = self.MDGAMEFONT.render('  3  ', True, TEXTCOLOR, GRAY) 	#renders "3" button
		num3Rect = num3.get_rect() 	#gets rect value of "3" button
		num3Rect.topleft= (2*(self.boardsize/12), 2*(self.boardsize/12)) 	#places "3" button
		self.DISPLAY.blit(num3,num3Rect) 	#displays "3" button

		num4 = self.MDGAMEFONT.render('  4  ', True, TEXTCOLOR, GRAY) 	#renders "4" button
		num4Rect = num4.get_rect() 	#gets rect value of "4" button
		num4Rect.topleft= (3*(self.boardsize/12), 2*(self.boardsize/12)) 	#places "4" button
		self.DISPLAY.blit(num4,num4Rect) 	#displays "4" button

		num5 = self.MDGAMEFONT.render('  5  ', True, TEXTCOLOR, GRAY) 	#renders "5" button
		num5Rect = num5.get_rect() 	#gets rect value of "5" button
		num5Rect.topleft= (4*(self.boardsize/12), 2*(self.boardsize/12)) 	#places "5" button
		self.DISPLAY.blit(num5,num5Rect) 	#displays "5" button

		num6 = self.MDGAMEFONT.render('  6  ', True, TEXTCOLOR, GRAY) 	#renders "6" button
		num6Rect = num6.get_rect() 	#gets rect value of "6" button
		num6Rect.topleft= (5*(self.boardsize/12), 2*(self.boardsize/12)) 	#places "6" button
		self.DISPLAY.blit(num6,num6Rect) 	#displays "6" button

		num7 = self.MDGAMEFONT.render('  7  ', True, TEXTCOLOR, GRAY) 	#renders "7" button
		num7Rect = num7.get_rect() 	#gets rect value of "7" button
		num7Rect.topleft= (6*(self.boardsize/12), 2*(self.boardsize/12)) 	#places "7" button
		self.DISPLAY.blit(num7,num7Rect) 	#displays "7" button

		num8 = self.MDGAMEFONT.render('  8  ', True, TEXTCOLOR, GRAY) 	#renders "8" button
		num8Rect = num8.get_rect() 	#gets rect value of "8" button
		num8Rect.topleft= (7*(self.boardsize/12), 2*(self.boardsize/12)) 	#places "8" button
		self.DISPLAY.blit(num8,num8Rect) 	#displays "8" button

		pygame.display.update()

		while (starting == True):
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONUP:  #checks for mouse click
					mousex, mousey = event.pos #gets coordinates of mouse click		
					if num2Rect.collidepoint((mousex, mousey)): #checks if mouse click is in 2 button
						if (isselected == False):
							self.NUMPLAYERS = 2
							isselected = True
							num2 = self.MDGAMEFONT.render('  2  ', True, BLACK, RED) 	#renders "2" button
							self.DISPLAY.blit(num2,num2Rect) 	#displays "2" button
							pygame.display.update()
							starting = False
					if num3Rect.collidepoint((mousex, mousey)): #checks if mouse click is in 3 button
						if (isselected == False):
							self.NUMPLAYERS = 3
							isselected = True
							num3 = self.MDGAMEFONT.render('  3  ', True, BLACK, RED) 	#renders "3" button
							self.DISPLAY.blit(num3,num3Rect) 	#displays "3" button
							pygame.display.update()
							starting = False
					if num4Rect.collidepoint((mousex, mousey)): #checks if mouse click is in 4 button
						if (isselected == False):
							self.NUMPLAYERS = 4
							isselected = True
							num4 = self.MDGAMEFONT.render('  4  ', True, BLACK, RED) 	#renders "4" button
							self.DISPLAY.blit(num4,num4Rect) 	#displays "4" button
							pygame.display.update()
							starting = False
					if num5Rect.collidepoint((mousex, mousey)): #checks if mouse click is in 5 button
						if (isselected == False):
							self.NUMPLAYERS = 5
							isselected = True
							num5 = self.MDGAMEFONT.render('  5  ', True, BLACK, RED) 	#renders "5" button
							self.DISPLAY.blit(num5,num5Rect) 	#displays "5" button
							pygame.display.update()
							starting = False
					if num6Rect.collidepoint((mousex, mousey)): #checks if mouse click is in6 button
						if (isselected == False):
							self.NUMPLAYERS = 6
							isselected = True
							num6 = self.MDGAMEFONT.render('  6  ', True, BLACK, RED) 	#renders "6" button
							self.DISPLAY.blit(num6,num6Rect) 	#displays "6" button
							pygame.display.update()
							starting = False
					if num7Rect.collidepoint((mousex, mousey)): #checks if mouse click is in 7 button
						if (isselected == False):
							self.NUMPLAYERS = 7
							isselected = True
							num7 = self.MDGAMEFONT.render('  7  ', True, BLACK, RED) 	#renders "7" button
							self.DISPLAY.blit(num7,num7Rect) 	#displays "7" button
							pygame.display.update()
							starting = False
					if num8Rect.collidepoint((mousex, mousey)): #checks if mouse click is in 8 button
						if (isselected == False):
							self.NUMPLAYERS = 8
							isselected = True
							num8 = self.MDGAMEFONT.render('  8  ', True, BLACK, RED) 	#renders "8" button
							self.DISPLAY.blit(num8,num8Rect) 	#displays "8" button
							pygame.display.update()
							starting = False
					if quitbuttonRect.collidepoint((mousex, mousey)): #checks if mouse click is in quit button
						sys.exit()
			
		for i in range(0, 8):
			i_path = "./images/tokens/token"+str(i)+".jpg" 
			if event.type == MOUSEBUTTONUP:  #checks for mouse click
				mousex, mousey = event.pos #gets coordinates of mouse click
			if os.path.exists(i_path):
				tokens.append(i_path)
			else:
			    print "Error loading game piece images. Please reinstall game files."
                            exit(0)
			

		piece0 = pygame.image.load(tokens[0]).convert() #Convert image to new pixel format
		piece0 = pygame.transform.scale(piece0,(self.boardsize/12,self.boardsize/12)) #Scale image
		piece0Rect = piece0.get_rect()
		piece0Rect.topleft= (1*(self.boardsize/12)*1.2,(4*self.boardsize/12))
		self.DISPLAY.blit(piece0,piece0Rect) #Display corner piece at blit destination

		piece1 = pygame.image.load(tokens[1]).convert() #Convert image to new pixel format
		piece1 = pygame.transform.scale(piece1,(self.boardsize/12,self.boardsize/12)) #Scale image
		piece1Rect = piece1.get_rect()
		piece1Rect.topleft= (2*(self.boardsize/12)*1.2,(4*self.boardsize/12))
		self.DISPLAY.blit(piece1,piece1Rect) #Display corner piece at blit destination

		piece2 = pygame.image.load(tokens[2]).convert() #Convert image to new pixel format
		piece2 = pygame.transform.scale(piece2,(self.boardsize/12,self.boardsize/12)) #Scale image
		piece2Rect = piece2.get_rect()
		piece2Rect.topleft= (3*(self.boardsize/12*1.2),(4*self.boardsize/12))
		self.DISPLAY.blit(piece2,piece2Rect) #Display corner piece at blit destination

		piece3 = pygame.image.load(tokens[3]).convert() #Convert image to new pixel format
		piece3 = pygame.transform.scale(piece3,(self.boardsize/12,self.boardsize/12)) #Scale image
		piece3Rect = piece3.get_rect()
		piece3Rect.topleft= (4*(self.boardsize/12)*1.2,(4*self.boardsize/12))
		self.DISPLAY.blit(piece3,piece3Rect) #Display corner piece at blit destination
			
		piece4 = pygame.image.load(tokens[4]).convert() #Convert image to new pixel format
		piece4 = pygame.transform.scale(piece4,(self.boardsize/12,self.boardsize/12)) #Scale image
		piece4Rect = piece4.get_rect()
		piece4Rect.topleft= (5*(self.boardsize/12)*1.2,(4*self.boardsize/12))
		self.DISPLAY.blit(piece4,piece4Rect) #Display corner piece at blit destination
			
		piece5 = pygame.image.load(tokens[5]).convert() #Convert image to new pixel format
		piece5 = pygame.transform.scale(piece5,(self.boardsize/12,self.boardsize/12)) #Scale image
		piece5Rect = piece5.get_rect()
		piece5Rect.topleft= (6*(self.boardsize/12)*1.2,(4*self.boardsize/12))
		self.DISPLAY.blit(piece5,piece5Rect) #Display corner piece at blit destination
			
		piece6 = pygame.image.load(tokens[6]).convert() #Convert image to new pixel format
		piece6 = pygame.transform.scale(piece6,(self.boardsize/12,self.boardsize/12)) #Scale image
		piece6Rect = piece6.get_rect()
		piece6Rect.topleft= (7*(self.boardsize/12)*1.2, (4*self.boardsize/12))
		self.DISPLAY.blit(piece6,piece6Rect) #Display corner piece at blit destination
			
		piece7 = pygame.image.load(tokens[7]).convert() #Convert image to new pixel format
		piece7 = pygame.transform.scale(piece7,(self.boardsize/12,self.boardsize/12)) #Scale image
		piece7Rect = piece7.get_rect()
		piece7Rect.topleft= (8*(self.boardsize/12)*1.2, (4*self.boardsize/12))
		self.DISPLAY.blit(piece7,piece7Rect) #Display corner piece at blit destination

		choosepiece= []
		ispicked = [False]*8
		
		for p in range(0, self.NUMPLAYERS):
			i = p + 1
		
			playertxt = self.MDGAMEFONT.render("Player %s: Select Your Game Piece" % i, True, TEXTCOLOR, BLACK) 	#renders selection text
			playertxtRect = playertxt.get_rect() 	#gets rect value of selection text
			playertxtRect.topleft= ((self.boardsize/12), 3*(self.boardsize/12)) 	#puts selection text in corner
			self.DISPLAY.blit(playertxt,playertxtRect) 	#displays selection text			
			pygame.display.update()
			
			iteration = True
			while (iteration == True):
				for event in pygame.event.get():
					if event.type == MOUSEBUTTONUP:  #checks for mouse click
						mousex, mousey = event.pos #gets coordinates of mouse click

						if (piece0Rect.collidepoint((mousex, mousey)) and (ispicked[0] == False)): #checks if mouse click is in 0 token
							ispicked[0] = True
							choosepiece.append(tokens[0])
							pygame.draw.rect(self.DISPLAY,BLACK,piece0Rect,0)
							iteration = False

						if (piece1Rect.collidepoint((mousex, mousey)) and (ispicked[1] == False)): #checks if mouse click is in 1 token
							ispicked[1] = True
							choosepiece.append(tokens[1])
							pygame.draw.rect(self.DISPLAY,BLACK,piece1Rect,0)
							iteration = False

						if (piece2Rect.collidepoint((mousex, mousey)) and (ispicked[2] == False)): #checks if mouse click is in 2 token
							ispicked[2] = True
							choosepiece.append(tokens[2])
							pygame.draw.rect(self.DISPLAY,BLACK,piece2Rect,0)
							iteration = False

						if (piece3Rect.collidepoint((mousex, mousey)) and (ispicked[3] == False)): #checks if mouse click is in 3 token
							ispicked[3] = True
							choosepiece.append(tokens[3])
							pygame.draw.rect(self.DISPLAY,BLACK,piece3Rect,0)
							iteration = False

						if (piece4Rect.collidepoint((mousex, mousey)) and (ispicked[4] == False)): #checks if mouse click is in 4 token
							ispicked[4] = True
							choosepiece.append(tokens[4])
							pygame.draw.rect(self.DISPLAY,BLACK,piece4Rect,0)
							iteration = False

						if (piece5Rect.collidepoint((mousex, mousey)) and (ispicked[5] == False)): #checks if mouse click is in 5 token
							ispicked[5] = True
							choosepiece.append(tokens[5])
							pygame.draw.rect(self.DISPLAY,BLACK,piece5Rect,0)
							iteration = False

						if (piece6Rect.collidepoint((mousex, mousey)) and (ispicked[6] == False)): #checks if mouse click is in 6 token
							ispicked[6] = True
							choosepiece.append(tokens[6])
							pygame.draw.rect(self.DISPLAY,BLACK,piece6Rect,0)
							iteration = False
							
						if (piece7Rect.collidepoint((mousex, mousey)) and (ispicked[7] == False)): #checks if mouse click is in 7 token
							ispicked[7] = True
							choosepiece.append(tokens[7])
							pygame.draw.rect(self.DISPLAY,BLACK,piece7Rect,0)
							iteration = False

						if quitbuttonRect.collidepoint((mousex, mousey)): #checks if mouse click is in quit button
							sys.exit()
		
		finishtxt = self.MDGAMEFONT.render("You're Ready To Start The Game!", True, TEXTCOLOR, BLACK) 	#renders selection text
		finishtxtRect = finishtxt.get_rect() 	#gets rect value of selection text
		finishtxtRect.topleft= ((self.boardsize/12), 6*(self.boardsize/12)) 	#puts selection text in corner
		self.DISPLAY.blit(finishtxt,finishtxtRect) 	#displays selection text				

		starttxt = self.LGGAMEFONT.render("  START  ", True, TEXTCOLOR, GRAY) 	#renders selection text
		starttxtRect = starttxt.get_rect() 	#gets rect value of selection text
		starttxtRect.topleft= ((self.boardsize/12), 7*(self.boardsize/12)) 	#puts selection text in corner
		self.DISPLAY.blit(starttxt,starttxtRect) 	#displays selection text			

		pygame.display.update()

		started = False;
		while (started == False):
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONUP:  #checks for mouse click
					mousex, mousey = event.pos #gets coordinates of mouse click
					if (starttxtRect.collidepoint((mousex, mousey))): #checks if mouse click is in start button
						print "started!"
						started = True

		# For testing, to ensure the game piece selections are correct		
		#for item in choosepiece:             
  		#	print item

		#return values
		players = []
		for i in range(len(choosepiece)):
			play = Player(1500,choosepiece[i],0)
			players.append(play)
		return players



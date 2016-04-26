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

		welcome = self.LGGAMEFONT.render('Welcome to Modopoly!', True, TEXTCOLOR, BLACK) 	
		welcomeRect = welcome.get_rect() 	
		welcomeRect.topleft 	
		self.DISPLAY.blit(welcome,welcomeRect) 	
		
		selecttxt = self.MDGAMEFONT.render('Select number of players:', True, TEXTCOLOR, BLACK) 	
		selecttxtRect = selecttxt.get_rect() 	
		selecttxtRect.topleft= ((self.boardsize/12), (self.boardsize/12)) 	
		self.DISPLAY.blit(selecttxt,selecttxtRect) 	

		#draws the quit button
		quitbutton = self.LGGAMEFONT.render(' QUIT ', True, TEXTCOLOR, GRAY) 	
		quitbuttonRect = quitbutton.get_rect() 	
		quitbuttonRect.bottomleft= (0, self.boardsize) 	
		self.DISPLAY.blit(quitbutton,quitbuttonRect) 	
		
		#draws the number digits/buttons for each possible number of players (2-8)
		num2 = self.MDGAMEFONT.render('  2  ', True, TEXTCOLOR, GRAY) 	
		num2Rect = num2.get_rect() 	
		num2Rect.topleft= (1*(self.boardsize/12), 2*(self.boardsize/12)) 	
		self.DISPLAY.blit(num2,num2Rect) 	

		num3 = self.MDGAMEFONT.render('  3  ', True, TEXTCOLOR, GRAY) 	
		num3Rect = num3.get_rect() 	
		num3Rect.topleft= (2*(self.boardsize/12), 2*(self.boardsize/12)) 	
		self.DISPLAY.blit(num3,num3Rect) 	

		num4 = self.MDGAMEFONT.render('  4  ', True, TEXTCOLOR, GRAY) 	
		num4Rect = num4.get_rect() 
		num4Rect.topleft= (3*(self.boardsize/12), 2*(self.boardsize/12)) 	
		self.DISPLAY.blit(num4,num4Rect) 	

		num5 = self.MDGAMEFONT.render('  5  ', True, TEXTCOLOR, GRAY) 	
		num5Rect = num5.get_rect() 	
		num5Rect.topleft= (4*(self.boardsize/12), 2*(self.boardsize/12)) 	
		self.DISPLAY.blit(num5,num5Rect) 	

		num6 = self.MDGAMEFONT.render('  6  ', True, TEXTCOLOR, GRAY) 	
		num6Rect = num6.get_rect() 	
		num6Rect.topleft= (5*(self.boardsize/12), 2*(self.boardsize/12)) 	
		self.DISPLAY.blit(num6,num6Rect) 	

		num7 = self.MDGAMEFONT.render('  7  ', True, TEXTCOLOR, GRAY) 	
		num7Rect = num7.get_rect() 
		num7Rect.topleft= (6*(self.boardsize/12), 2*(self.boardsize/12)) 	
		self.DISPLAY.blit(num7,num7Rect) 	

		num8 = self.MDGAMEFONT.render('  8  ', True, TEXTCOLOR, GRAY) 	
		num8Rect = num8.get_rect() 	
		num8Rect.topleft= (7*(self.boardsize/12), 2*(self.boardsize/12)) 	
		self.DISPLAY.blit(num8,num8Rect) 	

		pygame.display.update()

		#Player selects the number of players
		while (starting == True):
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONUP:  
					mousex, mousey = event.pos 		
					if num2Rect.collidepoint((mousex, mousey)): 
						if (isselected == False):
							self.NUMPLAYERS = 2
							isselected = True
							num2 = self.MDGAMEFONT.render('  2  ', True, BLACK, RED) 	
							self.DISPLAY.blit(num2,num2Rect) 	
							pygame.display.update()
							starting = False
					if num3Rect.collidepoint((mousex, mousey)): 
						if (isselected == False):
							self.NUMPLAYERS = 3
							isselected = True
							num3 = self.MDGAMEFONT.render('  3  ', True, BLACK, RED) 	
							self.DISPLAY.blit(num3,num3Rect) 	
							pygame.display.update()
							starting = False
					if num4Rect.collidepoint((mousex, mousey)): 
						if (isselected == False):
							self.NUMPLAYERS = 4
							isselected = True
							num4 = self.MDGAMEFONT.render('  4  ', True, BLACK, RED) 	
							self.DISPLAY.blit(num4,num4Rect) 	
							pygame.display.update()
							starting = False
					if num5Rect.collidepoint((mousex, mousey)): 
						if (isselected == False):
							self.NUMPLAYERS = 5
							isselected = True
							num5 = self.MDGAMEFONT.render('  5  ', True, BLACK, RED) 	
							self.DISPLAY.blit(num5,num5Rect) 	
							pygame.display.update()
							starting = False
					if num6Rect.collidepoint((mousex, mousey)): 
						if (isselected == False):
							self.NUMPLAYERS = 6
							isselected = True
							num6 = self.MDGAMEFONT.render('  6  ', True, BLACK, RED) 	
							self.DISPLAY.blit(num6,num6Rect) 	
							pygame.display.update()
							starting = False
					if num7Rect.collidepoint((mousex, mousey)): 
						if (isselected == False):
							self.NUMPLAYERS = 7
							isselected = True
							num7 = self.MDGAMEFONT.render('  7  ', True, BLACK, RED) 	
							self.DISPLAY.blit(num7,num7Rect) 	
							pygame.display.update()
							starting = False
					if num8Rect.collidepoint((mousex, mousey)): 
						if (isselected == False):
							self.NUMPLAYERS = 8
							isselected = True
							num8 = self.MDGAMEFONT.render('  8  ', True, BLACK, RED) 	
							self.DISPLAY.blit(num8,num8Rect) 	
							pygame.display.update()
							starting = False
					if quitbuttonRect.collidepoint((mousex, mousey)): 
						sys.exit()
		
		#loads in the game pieces	
		for i in range(0, 8):
			i_path = "./images/tokens/token"+str(i)+".jpg" 
			if event.type == MOUSEBUTTONUP:  
				mousex, mousey = event.pos 
			if os.path.exists(i_path):
				tokens.append(i_path)
			else:
			    print "Error loading game piece images. Please reinstall game files."
                            exit(0)
			
		#Display the game pieces so a player can select them
		piece0 = pygame.image.load(tokens[0]).convert() 
		piece0 = pygame.transform.scale(piece0,(self.boardsize/12,self.boardsize/12)) 
		piece0Rect = piece0.get_rect()
		piece0Rect.topleft= (1*(self.boardsize/12)*1.2,(4*self.boardsize/12))
		self.DISPLAY.blit(piece0,piece0Rect) 

		piece1 = pygame.image.load(tokens[1]).convert() 
		piece1 = pygame.transform.scale(piece1,(self.boardsize/12,self.boardsize/12)) 
		piece1Rect = piece1.get_rect()
		piece1Rect.topleft= (2*(self.boardsize/12)*1.2,(4*self.boardsize/12))
		self.DISPLAY.blit(piece1,piece1Rect) 

		piece2 = pygame.image.load(tokens[2]).convert() 
		piece2 = pygame.transform.scale(piece2,(self.boardsize/12,self.boardsize/12))
		piece2Rect = piece2.get_rect()
		piece2Rect.topleft= (3*(self.boardsize/12*1.2),(4*self.boardsize/12))
		self.DISPLAY.blit(piece2,piece2Rect) 

		piece3 = pygame.image.load(tokens[3]).convert() 
		piece3 = pygame.transform.scale(piece3,(self.boardsize/12,self.boardsize/12)) 
		piece3Rect = piece3.get_rect()
		piece3Rect.topleft= (4*(self.boardsize/12)*1.2,(4*self.boardsize/12))
		self.DISPLAY.blit(piece3,piece3Rect) 
			
		piece4 = pygame.image.load(tokens[4]).convert() 
		piece4 = pygame.transform.scale(piece4,(self.boardsize/12,self.boardsize/12)) 
		piece4Rect = piece4.get_rect()
		piece4Rect.topleft= (5*(self.boardsize/12)*1.2,(4*self.boardsize/12))
		self.DISPLAY.blit(piece4,piece4Rect) 
			
		piece5 = pygame.image.load(tokens[5]).convert() 
		piece5 = pygame.transform.scale(piece5,(self.boardsize/12,self.boardsize/12)) 
		piece5Rect = piece5.get_rect()
		piece5Rect.topleft= (6*(self.boardsize/12)*1.2,(4*self.boardsize/12))
		self.DISPLAY.blit(piece5,piece5Rect) 
			
		piece6 = pygame.image.load(tokens[6]).convert() 
		piece6 = pygame.transform.scale(piece6,(self.boardsize/12,self.boardsize/12)) 
		piece6Rect = piece6.get_rect()
		piece6Rect.topleft= (7*(self.boardsize/12)*1.2, (4*self.boardsize/12))
		self.DISPLAY.blit(piece6,piece6Rect) 
			
		piece7 = pygame.image.load(tokens[7]).convert() 
		piece7 = pygame.transform.scale(piece7,(self.boardsize/12,self.boardsize/12))
		piece7Rect = piece7.get_rect()
		piece7Rect.topleft= (8*(self.boardsize/12)*1.2, (4*self.boardsize/12))
		self.DISPLAY.blit(piece7,piece7Rect) 
		
		#initialize the arrary that will store each game piece, with array length == number of players
		#initialize the array showing which pieces have been selected already (starts as all false)
		choosepiece= []
		ispicked = [False]*8
		
		#iterates through each player selecting their game piece
		for p in range(0, self.NUMPLAYERS):
			i = p + 1
		
			playertxt = self.MDGAMEFONT.render("Player %s: Select Your Game Piece" % i, True, TEXTCOLOR, BLACK) 	
			playertxtRect = playertxt.get_rect() 	
			playertxtRect.topleft= ((self.boardsize/12), 3*(self.boardsize/12)) 	
			self.DISPLAY.blit(playertxt,playertxtRect) 				
			pygame.display.update()
			
			iteration = True
			while (iteration == True):
				for event in pygame.event.get():
					if event.type == MOUSEBUTTONUP:  
						mousex, mousey = event.pos 

						if (piece0Rect.collidepoint((mousex, mousey)) and (ispicked[0] == False)): 
							ispicked[0] = True
							choosepiece.append(tokens[0])
							pygame.draw.rect(self.DISPLAY,BLACK,piece0Rect,0)
							iteration = False

						if (piece1Rect.collidepoint((mousex, mousey)) and (ispicked[1] == False)): 
							ispicked[1] = True
							choosepiece.append(tokens[1])
							pygame.draw.rect(self.DISPLAY,BLACK,piece1Rect,0)
							iteration = False

						if (piece2Rect.collidepoint((mousex, mousey)) and (ispicked[2] == False)): 
							ispicked[2] = True
							choosepiece.append(tokens[2])
							pygame.draw.rect(self.DISPLAY,BLACK,piece2Rect,0)
							iteration = False

						if (piece3Rect.collidepoint((mousex, mousey)) and (ispicked[3] == False)): 
							ispicked[3] = True
							choosepiece.append(tokens[3])
							pygame.draw.rect(self.DISPLAY,BLACK,piece3Rect,0)
							iteration = False

						if (piece4Rect.collidepoint((mousex, mousey)) and (ispicked[4] == False)): 
							ispicked[4] = True
							choosepiece.append(tokens[4])
							pygame.draw.rect(self.DISPLAY,BLACK,piece4Rect,0)
							iteration = False

						if (piece5Rect.collidepoint((mousex, mousey)) and (ispicked[5] == False)): 
							ispicked[5] = True
							choosepiece.append(tokens[5])
							pygame.draw.rect(self.DISPLAY,BLACK,piece5Rect,0)
							iteration = False

						if (piece6Rect.collidepoint((mousex, mousey)) and (ispicked[6] == False)): 
							ispicked[6] = True
							choosepiece.append(tokens[6])
							pygame.draw.rect(self.DISPLAY,BLACK,piece6Rect,0)
							iteration = False
							
						if (piece7Rect.collidepoint((mousex, mousey)) and (ispicked[7] == False)): 
							ispicked[7] = True
							choosepiece.append(tokens[7])
							pygame.draw.rect(self.DISPLAY,BLACK,piece7Rect,0)
							iteration = False

						if quitbuttonRect.collidepoint((mousex, mousey)): 
							sys.exit()
		
		#Finished selecting game pieces, the player is now ready to start the game
		finishtxt = self.MDGAMEFONT.render("You're Ready To Start The Game!", True, TEXTCOLOR, BLACK) 	
		finishtxtRect = finishtxt.get_rect() 	
		finishtxtRect.topleft= ((self.boardsize/12), 6*(self.boardsize/12)) 	
		self.DISPLAY.blit(finishtxt,finishtxtRect) 					

		#draws the start button
		starttxt = self.LGGAMEFONT.render("  START  ", True, TEXTCOLOR, GRAY) 	
		starttxtRect = starttxt.get_rect() 	
		starttxtRect.topleft= ((self.boardsize/12), 7*(self.boardsize/12)) 	
		self.DISPLAY.blit(starttxt,starttxtRect) 				

		pygame.display.update()

		#Waits for player to select the start button
		started = False;
		while (started == False):
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONUP:  
					mousex, mousey = event.pos 
					if (starttxtRect.collidepoint((mousex, mousey))): 
						print "started!"
						started = True
					if quitbuttonRect.collidepoint((mousex, mousey)): 
						sys.exit()

		#Builds an array with each player, their starting cash, etc. with length = number of players
		players = []
		for i in range(len(choosepiece)):
			play = Player(1500,choosepiece[i],0, i)
			players.append(play)

		#returns this array to Main
		return players



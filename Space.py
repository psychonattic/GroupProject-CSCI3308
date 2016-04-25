from abc import ABCMeta
import random, sys, pygame, time, copy
from pygame.locals import *
from player import *

class Space:
	 __metaclass__ = ABCMeta

         def __init__(self):
             self.edge1 = 0
             self.edge2 = 0
             self.edge3 = 0
             self.edge4 = 0

	 def display(self):
             return

         def setPos(edge1, edge2, edge3, edge4):
             self.edge1 = edge1
             self.edge2 = edge2
             self.edge3 = edge3
             self.edge4 = edge4

class GoSpace(Space):

	def __init__(self,name,picture,spaceType): 
                Space.__init__(self)
		self.name = name
		self.picture = picture
		self.type = spaceType

	def display(self,boardsize,disp):
		BLACK = (  0,   0,   0) 
		WHITE = (255, 255, 255)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 1.5*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,boardsize-(2*cornersize),boardsize-(2*cornersize))
		pygame.draw.rect(disp,BLACK,rect)
		while True:
			fontsize = int(boardsize*.06)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)  
			name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR) 
			nameRect = name.get_rect() 
			nameRect.center = (int(boardsize / 2), int(boardsize / 3)) 
			disp.blit(name,nameRect)
			fontsize = int(boardsize*.03)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			gotext = DISPLAYFONT.render("Collect $200 when you pass GO.", True, TEXTCOLOR, BGCOLOR)
			gotextRect = gotext.get_rect() 
			gotextRect.center = (int(boardsize / 2), int(boardsize / 2)) 
			disp.blit(gotext,gotextRect)
			fontsize = int(boardsize*.02)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
			returntext = DISPLAYFONT.render("Click anywhere to return.", True, TEXTCOLOR, BGCOLOR)
			returntextRect = returntext.get_rect()
			returntextRect.center = (int(boardsize /2), int(2*(boardsize/3)))
			disp.blit(returntext,returntextRect)

			pygame.display.update()
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONDOWN: 
					disp.fill(BLACK) 
					return False
				if(event.type == QUIT):
					sys.exit()

class PropertySpace(Space):
	def __init__(self,name,picture,spaceType,color,price,rent,housecost): 
                Space.__init__(self)
		self.name = name
		self.picture = picture
		self.type = spaceType
		self.color = color
		self.price = price
		self.rent = rent
		self.mortgage = int(self.price/2)
		self.housecost = housecost
                self.houses = 0
		self.hotels = 0
		self.owner = None

	#Visit function, essentially display but in response to landing on a space
	def visit(self, boardsize, disp, player, money):

		BLACK = (  0,   0,   0) 
		WHITE = (255, 255, 255)
		GREEN = (  0, 155,   0)
		RED = (255,0,0)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 3.4*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,(boardsize-(2*cornersize)),(boardsize-(2*cornersize))/1.5)
		pygame.draw.rect(disp,BLACK,rect)
		
		#If unowned, option to buy or exit
		if(self.owner == None):
			
			while True:
				fontsize = int(boardsize*.05)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)  
				name = DISPLAYFONT.render(str("You Landed On: " + self.name), True, TEXTCOLOR, BGCOLOR) 
				nameRect = name.get_rect() 
				nameRect.center = (int(boardsize / 2), int(2 * boardsize / 10)) 
				disp.blit(name,nameRect)
				fontsize = int(boardsize*.03)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
				propertygroup = DISPLAYFONT.render(str("Color: " + self.color), True, TEXTCOLOR, BGCOLOR)
				propertygroupRect = propertygroup.get_rect() 
				propertygroupRect.center = (int(boardsize / 2), int(3 * boardsize / 10)) 
				disp.blit(propertygroup,propertygroupRect)
				owner = DISPLAYFONT.render(str("Owner: None"), True, TEXTCOLOR, BGCOLOR)
				ownerRect = owner.get_rect()
				ownerRect.center=(int(boardsize / 2), int(4 * boardsize / 10))
				disp.blit(owner,ownerRect)
				rent = DISPLAYFONT.render(str("Rent: $" + str(self.rent)), True, TEXTCOLOR, BGCOLOR)
				rentRect = rent.get_rect()
				rentRect.center = (int(boardsize / 4), int(5 * boardsize / 10))
				disp.blit(rent,rentRect)
				price = DISPLAYFONT.render(str("Price: $" + str(self.price)), True, RED, BGCOLOR)
				priceRect = price.get_rect()
				priceRect.center = (int(boardsize / 2), int(5 * boardsize / 10))
				disp.blit(price, priceRect)
				houses = DISPLAYFONT.render(str("Houses: " + str(self.houses)), True, TEXTCOLOR, BGCOLOR)
				housesRect = houses.get_rect()
				housesRect.center = (int(boardsize / 4), int(6 * boardsize / 10))
				disp.blit(houses,housesRect)
				#Display user's available money
				moneyAv = DISPLAYFONT.render(str("Available Money: $" + str(money)), True, GREEN, BGCOLOR)
				moneyRect = moneyAv.get_rect()
				moneyRect.center = (int(3 * boardsize / 4), int(6 * boardsize /10))
				disp.blit(moneyAv, moneyRect)
				housecost = DISPLAYFONT.render(str("House Cost: $" + str(self.housecost)), True, TEXTCOLOR, BGCOLOR)
				housecostRect = housecost.get_rect()
				housecostRect.center = (int(3 * boardsize / 4), int(5 * boardsize/ 10))
				disp.blit(housecost,housecostRect)
				mortgage = DISPLAYFONT.render(str("Mortgage: $" + str(self.mortgage)), True, TEXTCOLOR, BGCOLOR)
				mortgageRect = mortgage.get_rect()
				mortgageRect.center = (int(boardsize / 2), int(6.6 * boardsize/ 10))
				disp.blit(mortgage,mortgageRect)
				fontsize = int(boardsize*.04)
				
				#Button to allow purchase and exit
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
				buyPropSurf = DISPLAYFONT.render('Buy Property', True, TEXTCOLOR, GREEN) 
				buyPropRect = buyPropSurf.get_rect()
				buyPropRect.center = (int(boardsize / 2), (boardsize/10)*7.5)
				disp.blit(buyPropSurf,buyPropRect)
				
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
				exitSurf = DISPLAYFONT.render('Exit', True, TEXTCOLOR, RED) 
				exitRect = exitSurf.get_rect()
				exitRect.center = (int(boardsize / 2), (boardsize/10)*8.2)
				disp.blit(exitSurf,exitRect)
				#pygame.time.Clock().tick(20)
				pygame.display.update()
				for event in pygame.event.get():
					if(event.type == QUIT):
							sys.exit()
					if event.type == MOUSEBUTTONDOWN: 
						mousex, mousey = event.pos
						#Exit screen
						if exitRect.collidepoint((mousex, mousey)):
							return False
						if buyPropRect.collidepoint((mousex, mousey)): #Buy button is pressed
							if (money >= self.price): #Check for sufficient funds
								self.owner = str("Player " + str(player.name + 1)) #Update ownership
								player.money = money - self.price #update remaining funds
								disp.fill(BLACK) 
								return False
							else: #Case for not enough money
								while True:
									disp.fill(BLACK) 
									fontsize = int(boardsize*.06)
									STARTFONT = pygame.font.Font('freesansbold.ttf', fontsize)  

									insufGame = STARTFONT.render('Insufficient Funds',True,RED,BGCOLOR)
									insufGameRect = insufGame.get_rect()
									insufGameRect.center = (int(boardsize / 2), (0+(insufGameRect.height)))
									disp.blit(insufGame,insufGameRect)
									pygame.display.update() #updates the screen
									time.sleep(1.5)
									return False
		#If property is owned, pay rent
		else:
			while True:
				fontsize = int(boardsize*.05)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)  
				name = DISPLAYFONT.render(str("You Landed On: " + self.name), True, TEXTCOLOR, BGCOLOR) 
				nameRect = name.get_rect() 
				nameRect.center = (int(boardsize / 2), int(2 * boardsize / 10)) 
				disp.blit(name,nameRect)
				fontsize = int(boardsize*.03)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
				
				owner = DISPLAYFONT.render(str("Owner: " + self.owner), True, TEXTCOLOR, BGCOLOR)
				ownerRect = owner.get_rect()
				ownerRect.center=(int(boardsize / 2), int(4 * boardsize / 10))
				disp.blit(owner,ownerRect)
				rent = DISPLAYFONT.render(str("Rent Due: $" + str(self.rent)), True, TEXTCOLOR, BGCOLOR)
				rentRect = rent.get_rect()
				rentRect.center = (int(boardsize / 2), int(5 * boardsize / 10))
				disp.blit(rent,rentRect)
				moneyAv = DISPLAYFONT.render(str("Available Money: $" + str(money)), True, GREEN, BGCOLOR)
				moneyRect = moneyAv.get_rect()
				moneyRect.center = (int(boardsize / 2), int(6 * boardsize /10))
				disp.blit(moneyAv, moneyRect)		
								
				#Button to pay owner of property
				fontsize = int(boardsize*.05)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
				buyPropSurf = DISPLAYFONT.render('Pay', True, TEXTCOLOR, RED) 
				buyPropRect = buyPropSurf.get_rect()
				buyPropRect.center = (int(boardsize / 2), (boardsize/10)*7.5)
				disp.blit(buyPropSurf,buyPropRect)
				
				#pygame.time.Clock().tick(20)
				pygame.display.update()
				for event in pygame.event.get():
					if(event.type == QUIT):
							sys.exit()
					if event.type == MOUSEBUTTONDOWN: 
						mousex, mousey = event.pos
						#Exit screen
						if buyPropRect.collidepoint((mousex, mousey)): #Buy button is pressed
							if (money >= self.rent): #Check for sufficient funds
								player.money = money - self.rent #update remaining funds
								disp.fill(BLACK) 
								return False
							else: #Case for not enough money
								while True:
									disp.fill(BLACK) 
									fontsize = int(boardsize*.06)
									STARTFONT = pygame.font.Font('freesansbold.ttf', fontsize)  

									insufGame = STARTFONT.render('Insufficient Funds',True,RED,BGCOLOR)
									insufGameRect = insufGame.get_rect()
									insufGameRect.center = (int(boardsize / 2), (0+(insufGameRect.height)))
									disp.blit(insufGame,insufGameRect)
									pygame.display.update() #updates the screen
									time.sleep(1.5)
									return False	
										
			
	def display(self,boardsize,disp):
		BLACK = (  0,   0,   0) 
		WHITE = (255, 255, 255)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 1.5*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,boardsize-(2*cornersize),boardsize-(2*cornersize))
		pygame.draw.rect(disp,BLACK,rect)
		if(self.owner == None):
			self.owner = "None"
		while True:
			fontsize = int(boardsize*.05)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)  
			name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR) 
			nameRect = name.get_rect() 
			nameRect.center = (int(boardsize / 2), int(2 * boardsize / 10)) 
			disp.blit(name,nameRect)
			fontsize = int(boardsize*.03)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			propertygroup = DISPLAYFONT.render(str("Color: " + self.color), True, TEXTCOLOR, BGCOLOR)
			propertygroupRect = propertygroup.get_rect() 
			propertygroupRect.center = (int(boardsize / 2), int(3 * boardsize / 10)) 
			disp.blit(propertygroup,propertygroupRect)
			owner = DISPLAYFONT.render(str("Owner: " + self.owner), True, TEXTCOLOR, BGCOLOR)
			ownerRect = owner.get_rect()
			ownerRect.center=(int(boardsize / 2), int(4 * boardsize / 10))
			disp.blit(owner,ownerRect)
			price = DISPLAYFONT.render(str("Price: $" + str(self.price)), True, TEXTCOLOR, BGCOLOR)
			priceRect = price.get_rect()
			priceRect.center = (int(boardsize / 2), int(5 * boardsize / 10))
			disp.blit(price, priceRect)
			rent = DISPLAYFONT.render(str("Rent: $" + str(self.rent)), True, TEXTCOLOR, BGCOLOR)
			rentRect = rent.get_rect()
			rentRect.center = (int(boardsize / 4), int(5 * boardsize / 10))
			disp.blit(rent,rentRect)
			houses = DISPLAYFONT.render(str("Houses: " + str(self.houses)), True, TEXTCOLOR, BGCOLOR)
			housesRect = houses.get_rect()
			housesRect.center = (int(boardsize / 4), int(6 * boardsize / 10))
			disp.blit(houses,housesRect)
			hotels = DISPLAYFONT.render(str("Hotels: " + str(self.hotels)), True, TEXTCOLOR, BGCOLOR)
			hotelsRect = hotels.get_rect()
			hotelsRect.center = (int(3 * boardsize / 4), int(6 * boardsize /10))
			disp.blit(hotels, hotelsRect)
			housecost = DISPLAYFONT.render(str("House Cost: $" + str(self.housecost)), True, TEXTCOLOR, BGCOLOR)
			housecostRect = housecost.get_rect()
			housecostRect.center = (int(3 * boardsize / 4), int(5 * boardsize/ 10))
			disp.blit(housecost,housecostRect)
			mortgage = DISPLAYFONT.render(str("Mortgage: $" + str(self.mortgage)), True, TEXTCOLOR, BGCOLOR)
			mortgageRect = mortgage.get_rect()
			mortgageRect.center = (int(boardsize / 2), int(7 * boardsize/ 10))
			disp.blit(mortgage,mortgageRect)
			fontsize = int(boardsize*.02)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
			returntext = DISPLAYFONT.render("Click anywhere to return.", True, TEXTCOLOR, BGCOLOR)
			returntextRect = returntext.get_rect()
			returntextRect.center = (int(boardsize /2), int(8 * boardsize / 10))
			disp.blit(returntext,returntextRect)
			
			
			
	  		#pygame.time.Clock().tick(20)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONDOWN: 
					disp.fill(BLACK) 
					return False
				if(event.type == QUIT):
					sys.exit()

class RailRoadSpace(Space):
	def __init__(self,name,picture,spaceType,price,rent):
                Space.__init__(self)
		self.name = name
		self.picture = picture
		self.type = spaceType
		self.price = price
		self.rent = rent
		self.mortgage = int(self.price/2)
		self.owner = None
	
	#Visit function, essentially display but in response to landing on a space
	def visit(self, boardsize, disp, player, money):

		BLACK = (  0,   0,   0) 
		WHITE = (255, 255, 255)
		GREEN = (  0, 155,   0)
		RED = (255,0,0)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 3.4*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,(boardsize-(2*cornersize)),(boardsize-(2*cornersize))/1.5)
		pygame.draw.rect(disp,BLACK,rect)
		if(self.owner == None):
			
			while True:
				fontsize = int(boardsize*.06)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
				name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR)
				nameRect = name.get_rect()
				nameRect.center = (int(boardsize / 2), int(2 * boardsize / 10))
				disp.blit(name,nameRect)
				fontsize = int(boardsize*.03)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
				owner = DISPLAYFONT.render(str("Owner: None"), True, TEXTCOLOR, BGCOLOR)
				ownerRect = owner.get_rect()
				ownerRect.center = (int(boardsize / 2), int(3 * boardsize / 10))
				disp.blit(owner,ownerRect)
				price = DISPLAYFONT.render(str("Price: $" + str(self.price)), True, RED, BGCOLOR)
				priceRect = price.get_rect()
				priceRect.center = (int(boardsize / 2), int(4 * boardsize / 10))
				disp.blit(price, priceRect)
				rent = DISPLAYFONT.render(str("Rent: $" + str(self.rent)), True, TEXTCOLOR, BGCOLOR)
				rentRect = rent.get_rect()
				rentRect.center = (int(boardsize / 2), int(5 * boardsize / 10))
				disp.blit(rent,rentRect) 
				mortgage = DISPLAYFONT.render(str("Mortgage: $" + str(self.mortgage)), True, TEXTCOLOR, BGCOLOR)
				mortgageRect = mortgage.get_rect()
				mortgageRect.center = (int(boardsize / 2), int(6 * boardsize/ 10))
				disp.blit(mortgage,mortgageRect)
				fontsize = int(boardsize*.04)
				#Display user's available money
				moneyAv = DISPLAYFONT.render(str("Available Money: $" + str(money)), True, GREEN, BGCOLOR)
				moneyRect = moneyAv.get_rect()
				moneyRect.center = (int(boardsize / 2), int(7 * boardsize /10))
				disp.blit(moneyAv, moneyRect)
				
				#Buttons to buy or exit
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
				buyPropSurf = DISPLAYFONT.render('Buy Railroad?', True, TEXTCOLOR, GREEN) 
				buyPropRect = buyPropSurf.get_rect()
				buyPropRect.center = (int(boardsize / 2), (boardsize/10)*7.8)
				disp.blit(buyPropSurf,buyPropRect)
				
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
				exitSurf = DISPLAYFONT.render('Exit', True, TEXTCOLOR, RED) 
				exitRect = exitSurf.get_rect()
				exitRect.center = (int(boardsize / 2), (boardsize/10)*8.5)
				disp.blit(exitSurf,exitRect)
				#pygame.time.Clock().tick(20)
				pygame.display.update()
				for event in pygame.event.get():
					if(event.type == QUIT):
							sys.exit()
					if event.type == MOUSEBUTTONDOWN:
						mousex, mousey = event.pos
						#Exit screen
						if exitRect.collidepoint((mousex, mousey)):
							return False
						if buyPropRect.collidepoint((mousex, mousey)): #Buy button is pressed
							if (money >= self.price): #Check for sufficient funds
								self.owner = str("Player " + str(player.name +1)) #Update ownership
								player.money = money - self.price #update remaining funds
								disp.fill(BLACK) 
								return False
							else: #Case for not enough money
								while True:
									disp.fill(BLACK) 
									fontsize = int(boardsize*.06)
									STARTFONT = pygame.font.Font('freesansbold.ttf', fontsize)  

									insufGame = STARTFONT.render('Insufficient Funds',True,RED,BGCOLOR)
									insufGameRect = insufGame.get_rect()
									insufGameRect.center = (int(boardsize / 2), (0+(insufGameRect.height)))
									disp.blit(insufGame,insufGameRect)
									pygame.display.update() #updates the screen
									time.sleep(1.5)
									return False
						
		#If property is owned, pay rent
		else:
			while True:
				fontsize = int(boardsize*.05)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)  
				name = DISPLAYFONT.render(str("You Landed On: " + self.name), True, TEXTCOLOR, BGCOLOR) 
				nameRect = name.get_rect() 
				nameRect.center = (int(boardsize / 2), int(2 * boardsize / 10)) 
				disp.blit(name,nameRect)
				fontsize = int(boardsize*.03)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
				
				owner = DISPLAYFONT.render(str("Owner: " + self.owner), True, TEXTCOLOR, BGCOLOR)
				ownerRect = owner.get_rect()
				ownerRect.center=(int(boardsize / 2), int(4 * boardsize / 10))
				disp.blit(owner,ownerRect)
				rent = DISPLAYFONT.render(str("Rent Due: $" + str(self.rent)), True, TEXTCOLOR, BGCOLOR)
				rentRect = rent.get_rect()
				rentRect.center = (int(boardsize / 2), int(5 * boardsize / 10))
				disp.blit(rent,rentRect)
				moneyAv = DISPLAYFONT.render(str("Available Money: $" + str(money)), True, GREEN, BGCOLOR)
				moneyRect = moneyAv.get_rect()
				moneyRect.center = (int(boardsize / 2), int(6 * boardsize /10))
				disp.blit(moneyAv, moneyRect)		
								
				#Button to pay owner of property
				fontsize = int(boardsize*.05)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
				buyPropSurf = DISPLAYFONT.render('Pay', True, TEXTCOLOR, RED) 
				buyPropRect = buyPropSurf.get_rect()
				buyPropRect.center = (int(boardsize / 2), (boardsize/10)*7.5)
				disp.blit(buyPropSurf,buyPropRect)
				
				#pygame.time.Clock().tick(20)
				pygame.display.update()
				for event in pygame.event.get():
					if(event.type == QUIT):
							sys.exit()
					if event.type == MOUSEBUTTONDOWN: 
						mousex, mousey = event.pos
						#Exit screen
						if buyPropRect.collidepoint((mousex, mousey)): #Buy button is pressed
							if (money >= self.rent): #Check for sufficient funds
								player.money = money - self.rent #update remaining funds
								disp.fill(BLACK) 
								return False
							else: #Case for not enough money
								while True:
									disp.fill(BLACK) 
									fontsize = int(boardsize*.06)
									STARTFONT = pygame.font.Font('freesansbold.ttf', fontsize)  

									insufGame = STARTFONT.render('Insufficient Funds',True,RED,BGCOLOR)
									insufGameRect = insufGame.get_rect()
									insufGameRect.center = (int(boardsize / 2), (0+(insufGameRect.height)))
									disp.blit(insufGame,insufGameRect)
									pygame.display.update() #updates the screen
									time.sleep(1.5)
									return False	
		
	def display(self,boardsize,disp):
		BLACK = (  0,   0,   0)
		WHITE = (255, 255, 255)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 1.5*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,boardsize-(2*cornersize),boardsize-(2*cornersize))
		pygame.draw.rect(disp,BLACK,rect)
		if(self.owner == None):
			self.owner = "None"
		while True:
			fontsize = int(boardsize*.06)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR)
			nameRect = name.get_rect()
			nameRect.center = (int(boardsize / 2), int(2 * boardsize / 10))
			disp.blit(name,nameRect)
			fontsize = int(boardsize*.03)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			owner = DISPLAYFONT.render(str("Owner: " + self.owner), True, TEXTCOLOR, BGCOLOR)
			ownerRect = owner.get_rect()
			ownerRect.center = (int(boardsize / 2), int(3 * boardsize / 10))
			disp.blit(owner,ownerRect)
			price = DISPLAYFONT.render(str("Price: $" + str(self.price)), True, TEXTCOLOR, BGCOLOR)
			priceRect = price.get_rect()
			priceRect.center = (int(boardsize / 2), int(4 * boardsize / 10))
			disp.blit(price, priceRect)
			rent = DISPLAYFONT.render(str("Rent: $" + str(self.rent)), True, TEXTCOLOR, BGCOLOR)
			rentRect = rent.get_rect()
			rentRect.center = (int(boardsize / 2), int(5 * boardsize / 10))
			disp.blit(rent,rentRect) 
			mortgage = DISPLAYFONT.render(str("Mortgage: $" + str(self.mortgage)), True, TEXTCOLOR, BGCOLOR)
			mortgageRect = mortgage.get_rect()
			mortgageRect.center = (int(boardsize / 2), int(6 * boardsize/ 10))
			disp.blit(mortgage,mortgageRect)
			fontsize = int(boardsize*.02)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
			returntext = DISPLAYFONT.render("Click anywhere to return.", True, TEXTCOLOR, BGCOLOR)
			returntextRect = returntext.get_rect()
			returntextRect.center = (int(boardsize /2), int(7 * boardsize / 10))
			disp.blit(returntext,returntextRect)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONDOWN:
					disp.fill(BLACK)
					return False
				if(event.type == QUIT):
					sys.exit()

class UtilitiesSpace(Space):
	def __init__(self,name,picture,spaceType,price):
		Space.__init__(self)
		self.name = name
		self.picture = picture
		self.type = spaceType
		self.price = price
		self.rent = '4x dice roll'
		self.mortgage = int(self.price/2)
		self.bothowned = False
		self.owner = None

	#Visit function, essentially display but in response to landing on a space	
	def visit(self, boardsize, disp, player, money):

		BLACK = (  0,   0,   0) 
		WHITE = (255, 255, 255)
		GREEN = (  0, 155,   0)
		RED = (255, 0, 0)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 3.4*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,(boardsize-(2*cornersize)),(boardsize-(2*cornersize))/1.5)
		pygame.draw.rect(disp,BLACK,rect)
		if(self.owner == None):
			
			while True:
				fontsize = int(boardsize*.06)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
				name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR)
				nameRect = name.get_rect()
				nameRect.center = (int(boardsize / 2), int(boardsize / 5))
				disp.blit(name,nameRect)
				fontsize = int(boardsize*.03)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
				#Display user's available money
				moneyAv = DISPLAYFONT.render(str("Available Money: $" + str(money)), True, GREEN, BGCOLOR)
				moneyRect = moneyAv.get_rect()
				moneyRect.center = (int(boardsize / 2), int(3 * boardsize /10))
				disp.blit(moneyAv, moneyRect)
				owner = DISPLAYFONT.render('Owner: None', True, TEXTCOLOR, BGCOLOR)
				ownerRect = owner.get_rect()
				ownerRect.center = (int(boardsize / 2), int(2 * boardsize / 5))
				disp.blit(owner,ownerRect)
				cost = DISPLAYFONT.render('Price: $' + str(self.price), True, RED, BGCOLOR)
				costRect = cost.get_rect()
				costRect.center = (int(boardsize / 2), int(5 * boardsize / 10))
				disp.blit(cost,costRect)
				rent = DISPLAYFONT.render('Rent: ' + self.rent, True, TEXTCOLOR, BGCOLOR)
				rentRect = rent.get_rect()
				rentRect.center = (int(boardsize / 2), int(3 * boardsize / 5))
				disp.blit(rent,rentRect)
				mortgage = DISPLAYFONT.render('Mortgage: $' + str(self.mortgage), True, TEXTCOLOR, BGCOLOR)
				mortgageRect = mortgage.get_rect()
				mortgageRect.center = (int(boardsize / 2), int(7 * boardsize / 10))
				disp.blit(mortgage,mortgageRect)
				
				#Buttons to buy or exit
				fontsize = int(boardsize*.04)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
				buyPropSurf = DISPLAYFONT.render('Buy Utility?', True, TEXTCOLOR, GREEN) 
				buyPropRect = buyPropSurf.get_rect()
				buyPropRect.center = (int(boardsize / 2), (boardsize/10)*7.8)
				disp.blit(buyPropSurf,buyPropRect)
				
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
				exitSurf = DISPLAYFONT.render('Exit', True, TEXTCOLOR, RED) 
				exitRect = exitSurf.get_rect()
				exitRect.center = (int(boardsize / 2), (boardsize/10)*8.5)
				disp.blit(exitSurf,exitRect)
				#pygame.time.Clock().tick(20)
				pygame.display.update()
				for event in pygame.event.get():
					if(event.type == QUIT):
							sys.exit()
					if event.type == MOUSEBUTTONDOWN: 
						mousex, mousey = event.pos
						#Exit screen
						if exitRect.collidepoint((mousex, mousey)):
							return False
						if buyPropRect.collidepoint((mousex, mousey)): #Buy button is pressed
							if (money >= self.price): #Check for sufficient funds
								self.owner = str("Player " + str(player.name + 1)) #Update ownership
								player.money = money - self.price #update remaining funds
								disp.fill(BLACK) 
								return False
							else: #Case for not enough money
								while True:
									disp.fill(BLACK) 
									fontsize = int(boardsize*.06)
									STARTFONT = pygame.font.Font('freesansbold.ttf', fontsize)  

									insufGame = STARTFONT.render('Insufficient Funds',True,RED,BGCOLOR)
									insufGameRect = insufGame.get_rect()
									insufGameRect.center = (int(boardsize / 2), (0+(insufGameRect.height)))
									disp.blit(insufGame,insufGameRect)
									pygame.display.update() #updates the screen
									time.sleep(1.5)
									return False
		#If property is owned, pay rent
		else:
			while True:
				fontsize = int(boardsize*.05)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)  
				name = DISPLAYFONT.render(str("You Landed On: " + self.name), True, TEXTCOLOR, BGCOLOR) 
				nameRect = name.get_rect() 
				nameRect.center = (int(boardsize / 2), int(2 * boardsize / 10)) 
				disp.blit(name,nameRect)
				fontsize = int(boardsize*.03)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
				
				owner = DISPLAYFONT.render(str("Owner: " + self.owner), True, TEXTCOLOR, BGCOLOR)
				ownerRect = owner.get_rect()
				ownerRect.center=(int(boardsize / 2), int(4 * boardsize / 10))
				disp.blit(owner,ownerRect)
				rent = DISPLAYFONT.render(str("Rent Due: $" + str(self.rent)), True, TEXTCOLOR, BGCOLOR)
				rentRect = rent.get_rect()
				rentRect.center = (int(boardsize / 2), int(5 * boardsize / 10))
				disp.blit(rent,rentRect)
				moneyAv = DISPLAYFONT.render(str("Available Money: $" + str(money)), True, GREEN, BGCOLOR)
				moneyRect = moneyAv.get_rect()
				moneyRect.center = (int(boardsize / 2), int(6 * boardsize /10))
				disp.blit(moneyAv, moneyRect)		
								
				#Button to pay owner of property
				fontsize = int(boardsize*.05)
				DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
				buyPropSurf = DISPLAYFONT.render('Pay', True, TEXTCOLOR, RED) 
				buyPropRect = buyPropSurf.get_rect()
				buyPropRect.center = (int(boardsize / 2), (boardsize/10)*7.5)
				disp.blit(buyPropSurf,buyPropRect)
				
				#pygame.time.Clock().tick(20)
				pygame.display.update()
				for event in pygame.event.get():
					if(event.type == QUIT):
							sys.exit()
					if event.type == MOUSEBUTTONDOWN: 
						mousex, mousey = event.pos
						#Exit screen
						if buyPropRect.collidepoint((mousex, mousey)): #Buy button is pressed
							if (money >= self.rent): #Check for sufficient funds
								player.money = money - self.rent #update remaining funds
								disp.fill(BLACK) 
								return False
							else: #Case for not enough money
								while True:
									disp.fill(BLACK) 
									fontsize = int(boardsize*.06)
									STARTFONT = pygame.font.Font('freesansbold.ttf', fontsize)  

									insufGame = STARTFONT.render('Insufficient Funds',True,RED,BGCOLOR)
									insufGameRect = insufGame.get_rect()
									insufGameRect.center = (int(boardsize / 2), (0+(insufGameRect.height)))
									disp.blit(insufGame,insufGameRect)
									pygame.display.update() #updates the screen
									time.sleep(1.5)
									return False	
						
	def display(self,boardsize,disp):
		BLACK = (  0,   0,   0)
		WHITE = (255, 255, 255)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 1.5*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,boardsize-(2*cornersize),boardsize-(2*cornersize))
		pygame.draw.rect(disp,BLACK,rect)
		if(self.bothowned == True):
			self.rent = '10x dice roll'
		if(self.owner == None):
			self.owner = 'None'
		while True:
			fontsize = int(boardsize*.06)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR)
			nameRect = name.get_rect()
			nameRect.center = (int(boardsize / 2), int(boardsize / 5))
			disp.blit(name,nameRect)
			fontsize = int(boardsize*.03)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			group = DISPLAYFONT.render('Group: Utilities', True, TEXTCOLOR, BGCOLOR)
			groupRect = group.get_rect()
			groupRect.center = (int(boardsize / 2), int(3 * boardsize / 10))
			disp.blit(group,groupRect)
			owner = DISPLAYFONT.render('Owner: ' + self.owner, True, TEXTCOLOR, BGCOLOR)
			ownerRect = owner.get_rect()
			ownerRect.center = (int(boardsize / 2), int(2 * boardsize / 5))
			disp.blit(owner,ownerRect)
			cost = DISPLAYFONT.render('Price: $' + str(self.price), True, TEXTCOLOR,BGCOLOR)
			costRect = cost.get_rect()
			costRect.center = (int(boardsize / 2), int(5 * boardsize / 10))
			disp.blit(cost,costRect)
			rent = DISPLAYFONT.render('Rent: ' + self.rent, True, TEXTCOLOR, BGCOLOR)
			rentRect = rent.get_rect()
			rentRect.center = (int(boardsize / 2), int(3 * boardsize / 5))
			disp.blit(rent,rentRect)
			mortgage = DISPLAYFONT.render('Mortgage: $' + str(self.mortgage), True, TEXTCOLOR, BGCOLOR)
			mortgageRect = mortgage.get_rect()
			mortgageRect.center = (int(boardsize / 2), int(7 * boardsize / 10))
			disp.blit(mortgage,mortgageRect)
			fontsize = int(boardsize*.02)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
			returntext = DISPLAYFONT.render("Click anywhere to return.", True, TEXTCOLOR, BGCOLOR)
			returntextRect = returntext.get_rect()
			returntextRect.center = (int(boardsize / 2), int(4 * boardsize / 5))
			disp.blit(returntext,returntextRect)


			pygame.display.update()
			for event in pygame.event.get():
					if event.type == MOUSEBUTTONDOWN:
							disp.fill(BLACK)
							return False
					if(event.type == QUIT):
							sys.exit()

class TaxSpace(Space):
	def __init__(self,name,picture,spaceType):
			Space.__init__(self)
			self.name = name
			self.picture = picture
			self.type = spaceType
			
		
	#Visit function, essentially display but in response to landing on a space	
	def visit(self, boardsize, disp, player, money):

		BLACK = (  0,   0,   0) 
		WHITE = (255, 255, 255)
		GREEN = (  0, 155,   0)
		RED = (255, 0 , 0)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 3.4*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,(boardsize-(2*cornersize)),(boardsize-(2*cornersize))/1.5)
		pygame.draw.rect(disp,BLACK,rect)
		
		while True:
			fontsize = int(boardsize*.06)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR)
			nameRect = name.get_rect()
			nameRect.center = (int(boardsize / 2), int(boardsize / 4))
			disp.blit(name,nameRect)
			fontsize = int(boardsize*.03)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			taxtext=DISPLAYFONT.render("Pay $200 or 10% of assets to bank", True, RED, BGCOLOR)
			taxtextRect = taxtext.get_rect()
			taxtextRect.center = (int(boardsize / 2), int(boardsize /2))
			disp.blit(taxtext,taxtextRect)
			#Display user's available money
			moneyAv = DISPLAYFONT.render(str("Available Money: $" + str(money)), True, GREEN, BGCOLOR)
			moneyRect = moneyAv.get_rect()
			moneyRect.center = (int(3 * boardsize / 4), int(6 * boardsize /10))
			
			#Option to pay $200
			fontsize = int(boardsize*.03)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
			buyPropSurf = DISPLAYFONT.render('Pay $200', True, TEXTCOLOR, RED) 
			buyPropRect = buyPropSurf.get_rect()
			buyPropRect.center = (int(boardsize / 2), (boardsize/10)*8)
			disp.blit(buyPropSurf,buyPropRect)
			
			#option to pay %10 holdings
			fontsize = int(boardsize*.03)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
			perSurf = DISPLAYFONT.render('Pay %10 Total Holdings', True, TEXTCOLOR, RED) 
			perRect = perSurf.get_rect()
			perRect.center = (int(boardsize / 2), (boardsize/10)*7)
			disp.blit(perSurf,perRect)
			
			#pygame.time.Clock().tick(20)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONDOWN: 
					mousex, mousey = event.pos
					if perRect.collidepoint((mousex, mousey)): #%10 button
						player.money = (money - (money * .1))
						disp.fill(BLACK) 
						return False
					if buyPropRect.collidepoint((mousex, mousey)): #$200 button
						player.money = money - 200
						disp.fill(BLACK) 
						return False
				if(event.type == QUIT):
					sys.exit()
	
	def display(self,boardsize,disp):
		BLACK = (  0,   0,   0)
		WHITE = (255, 255, 255)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 1.5*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,boardsize-(2*cornersize),boardsize-(2*cornersize))
		pygame.draw.rect(disp,BLACK,rect)
		while True:
			fontsize = int(boardsize*.06)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR)
			nameRect = name.get_rect()
			nameRect.center = (int(boardsize / 2), int(boardsize / 4))
			disp.blit(name,nameRect)
			fontsize = int(boardsize*.03)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			taxtext=DISPLAYFONT.render("Pay $200 or 10% of assets to bank", True, (255,0,0), BGCOLOR)
			taxtextRect = taxtext.get_rect()
			taxtextRect.center = (int(boardsize / 2), int(boardsize /2))
			disp.blit(taxtext,taxtextRect)
			fontsize = int(boardsize*.02)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
			returntext = DISPLAYFONT.render("Click anywhere to return.", True, TEXTCOLOR, BGCOLOR)
			returntextRect = returntext.get_rect()
			returntextRect.center = (int(boardsize / 2), int(3 * boardsize / 4))
			disp.blit(returntext,returntextRect)


			pygame.display.update()
			for event in pygame.event.get():
					if event.type == MOUSEBUTTONDOWN:
							disp.fill(BLACK)
							return False
					if(event.type == QUIT):
							sys.exit()




class CommunityChestSpace(Space):
	def __init__(self,name,picture,spaceType):
                Space.__init__(self)
		self.name = name
		self.picture = picture
		self.type = spaceType
		
	
	#Visit function, essentially display but in response to landing on a space
	def visit(self, boardsize, disp, player, money):
		BLACK = (  0,   0,   0) 
		WHITE = (255, 255, 255)
		GREEN = (  0, 155,   0)
		RED = (255, 0 , 0)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 3.4*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,(boardsize-(2*cornersize)),(boardsize-(2*cornersize))/1.5)
		pygame.draw.rect(disp,BLACK,rect)
		while True:
			fontsize = int(boardsize*.06)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR)
			nameRect = name.get_rect()
			nameRect.center = (int(boardsize / 2), int(boardsize / 3))
			disp.blit(name,nameRect)
			
			fontsize = int(boardsize*.04)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
			buyPropSurf = DISPLAYFONT.render('OK', True, TEXTCOLOR, GREEN) 
			buyPropRect = buyPropSurf.get_rect()
			buyPropRect.center = (int(boardsize / 2), (boardsize/10)*8)
			disp.blit(buyPropSurf,buyPropRect)
			#pygame.time.Clock().tick(20)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONDOWN: 
					mousex, mousey = event.pos
					if buyPropRect.collidepoint((mousex, mousey)):
						disp.fill(BLACK) 
						 
						return False
				if(event.type == QUIT):
					sys.exit()


	def display(self,boardsize,disp):
		BLACK = (  0,   0,   0)
		WHITE = (255, 255, 255)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 1.5*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,boardsize-(2*cornersize),boardsize-(2*cornersize))
		pygame.draw.rect(disp,BLACK,rect)
		while True:
			fontsize = int(boardsize*.06)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR)
			nameRect = name.get_rect()
			nameRect.center = (int(boardsize / 2), int(boardsize / 3))
			disp.blit(name,nameRect)
			fontsize = int(boardsize*.03)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			fontsize = int(boardsize*.02)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
			returntext = DISPLAYFONT.render("Click anywhere to return.", True, TEXTCOLOR, BGCOLOR)
			returntextRect = returntext.get_rect()
			returntextRect.center = (int(boardsize / 2), int(2 * boardsize / 3))
			disp.blit(returntext,returntextRect)

			pygame.display.update()
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONDOWN:
					disp.fill(BLACK)
					return False
				if(event.type == QUIT):
					sys.exit()

class ChanceSpace(Space):
	def __init__(self,name,picture,spaceType):
                Space.__init__(self)
		self.name = name
		self.picture = picture
		self.type = spaceType
		
		
	#Visit function, essentially display but in response to landing on a space	
	def visit(self, boardsize, disp, player, money):
		BLACK = (  0,   0,   0) 
		WHITE = (255, 255, 255)
		GREEN = (  0, 155,   0)
		RED = (255, 0 , 0)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 3.4*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,(boardsize-(2*cornersize)),(boardsize-(2*cornersize))/1.5)
		pygame.draw.rect(disp,BLACK,rect)
	
		while True:
			fontsize = int(boardsize*.06)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR)
			nameRect = name.get_rect()
			nameRect.center = (int(boardsize / 2), int(boardsize / 3))
			disp.blit(name,nameRect)

			fontsize = int(boardsize*.04)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
			buyPropSurf = DISPLAYFONT.render('OK', True, TEXTCOLOR, GREEN) 
			buyPropRect = buyPropSurf.get_rect()
			buyPropRect.center = (int(boardsize / 2), (boardsize/10)*8)
			disp.blit(buyPropSurf,buyPropRect)
			#pygame.time.Clock().tick(20)
			
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONDOWN: 
					mousex, mousey = event.pos
					if buyPropRect.collidepoint((mousex, mousey)): 
						disp.fill(BLACK) 
						
						return False
				if(event.type == QUIT):
					sys.exit()

	def display(self,boardsize,disp):
		BLACK = (  0,   0,   0)
		WHITE = (255, 255, 255)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 1.5*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,boardsize-(2*cornersize),boardsize-(2*cornersize))
		pygame.draw.rect(disp,BLACK,rect)
		while True:
			fontsize = int(boardsize*.06)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR)
			nameRect = name.get_rect()
			nameRect.center = (int(boardsize / 2), int(boardsize / 3))
			disp.blit(name,nameRect)
			fontsize = int(boardsize*.03)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			fontsize = int(boardsize*.02)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
			returntext = DISPLAYFONT.render("Click anywhere to return.", True, TEXTCOLOR, BGCOLOR)
			returntextRect = returntext.get_rect()
			returntextRect.center = (int(boardsize / 2), int(2 * boardsize / 3))
			disp.blit(returntext,returntextRect)


			pygame.display.update()
			for event in pygame.event.get():
					if event.type == MOUSEBUTTONDOWN:
							disp.fill(BLACK)
							return False
					if(event.type == QUIT):
							sys.exit()

class FreeParkingSpace(Space):
	def __init__(self,name,picture,spaceType):
			Space.__init__(self)
			self.name = name
			self.picture = picture
			self.type = spaceType
			

	#Visit function, essentially display but in response to landing on a space
	def visit(self, boardsize, disp, player, money):
		BLACK = (  0,   0,   0) 
		WHITE = (255, 255, 255)
		GREEN = (  0, 155,   0)
		RED = (255, 0 , 0)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 3.4*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,(boardsize-(2*cornersize)),(boardsize-(2*cornersize))/1.5)
		pygame.draw.rect(disp,BLACK,rect)
		while True:
			fontsize = int(boardsize*.06)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR)
			nameRect = name.get_rect()
			nameRect.center = (int(boardsize / 2), int(boardsize / 4))
			disp.blit(name,nameRect)
			fontsize = int(boardsize*.03)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			nothing = DISPLAYFONT.render("Nothing interesting happens", True, TEXTCOLOR, BGCOLOR)
			nothingRect = nothing.get_rect()
			nothingRect.center = (int(boardsize / 2), int(boardsize / 2))
			disp.blit(nothing,nothingRect)
			
			fontsize = int(boardsize*.04)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
			buyPropSurf = DISPLAYFONT.render('OK', True, TEXTCOLOR, GREEN) 
			buyPropRect = buyPropSurf.get_rect()
			buyPropRect.center = (int(boardsize / 2), (boardsize/10)*8)
			disp.blit(buyPropSurf,buyPropRect)
			#pygame.time.Clock().tick(20)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONDOWN: 
					mousex, mousey = event.pos
					if buyPropRect.collidepoint((mousex, mousey)): 
						disp.fill(BLACK) 
						
						return False
				if(event.type == QUIT):
					sys.exit()


	def display(self,boardsize,disp):
		BLACK = (  0,   0,   0)
		WHITE = (255, 255, 255)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 1.5*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,boardsize-(2*cornersize),boardsize-(2*cornersize))
		pygame.draw.rect(disp,BLACK,rect)
		while True:
			fontsize = int(boardsize*.06)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR)
			nameRect = name.get_rect()
			nameRect.center = (int(boardsize / 2), int(boardsize / 4))
			disp.blit(name,nameRect)
			fontsize = int(boardsize*.03)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			nothing = DISPLAYFONT.render("Nothing interesting happens", True, TEXTCOLOR, BGCOLOR)
			nothingRect = nothing.get_rect()
			nothingRect.center = (int(boardsize / 2), int(boardsize / 2))
			disp.blit(nothing,nothingRect)
			fontsize = int(boardsize*.02)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
			returntext = DISPLAYFONT.render("Click anywhere to return.", True, TEXTCOLOR, BGCOLOR)
			returntextRect = returntext.get_rect()
			returntextRect.center = (int(boardsize / 2), int(3 * boardsize / 4))
			disp.blit(returntext,returntextRect)

			pygame.display.update()
			for event in pygame.event.get():
					if event.type == MOUSEBUTTONDOWN:
							disp.fill(BLACK)
							return False
					if(event.type == QUIT):
							sys.exit()



class JailSpace(Space):  #Still need to figure out what's going on with Jail Space/Just Visiting
	def __init__(self,name,picture,spaceType):
			Space.__init__(self)
			self.name = name
			self.picture = picture
			self.type = spaceType
			self.injail = None #['Ted','Nathan','Joel','John','Chase'] 
			
	
	#Visit function, essentially display but in response to landing on a space
	def visit(self, boardsize, disp, player, money):
		BLACK = (  0,   0,   0) 
		WHITE = (255, 255, 255)
		GREEN = (  0, 155,   0)
		RED = (255, 0 , 0)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 3.4*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,(boardsize-(2*cornersize)),(boardsize-(2*cornersize))/1.5)
		pygame.draw.rect(disp,BLACK,rect)
		while True:
			fontsize = int(boardsize*.06)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR)
			nameRect = name.get_rect()
			nameRect.center = (int(boardsize / 2), int(boardsize / 4))
			disp.blit(name,nameRect)
			fontsize = int(boardsize*.03)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			nothing = DISPLAYFONT.render("Just Visiting", True, TEXTCOLOR, BGCOLOR)
			nothingRect = nothing.get_rect()
			nothingRect.center = (int(boardsize / 2), int(boardsize / 2))
			disp.blit(nothing,nothingRect)
			
			fontsize = int(boardsize*.04)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
			buyPropSurf = DISPLAYFONT.render('OK', True, TEXTCOLOR, GREEN) 
			buyPropRect = buyPropSurf.get_rect()
			buyPropRect.center = (int(boardsize / 2), (boardsize/10)*8)
			disp.blit(buyPropSurf,buyPropRect)
			#pygame.time.Clock().tick(20)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONDOWN: 
					mousex, mousey = event.pos
					if buyPropRect.collidepoint((mousex, mousey)): 
						disp.fill(BLACK) 
						return False
				if(event.type == QUIT):
					sys.exit()
						
						
	def display(self,boardsize,disp):
		BLACK = (  0,   0,   0)
		WHITE = (255, 255, 255)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		cornersize = 1.5*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,boardsize-(2*cornersize),boardsize-(2*cornersize))
		pygame.draw.rect(disp,BLACK,rect)
		if(self.injail == None):
			listinjail = 'None'
		else:
			listinjail = ''
			for i in self.injail:
				listinjail += i
				listinjail += ' '	
				while True:
					fontsize = int(boardsize*.06)
					DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
					name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR)
					nameRect = name.get_rect()
					nameRect.center = (int(boardsize / 2), int(boardsize / 4))
					disp.blit(name,nameRect)
					fontsize = int(boardsize*.03)
					DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
					injail = DISPLAYFONT.render("In Jail: " + listinjail, True, TEXTCOLOR, BGCOLOR)
					injailRect = injail.get_rect()
					injailRect.center = (int(boardsize /2), int(2 * boardsize / 4))
					disp.blit(injail,injailRect)
					fontsize = int(boardsize*.02)
					DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
					returntext = DISPLAYFONT.render("Click anywhere to return.", True, TEXTCOLOR, BGCOLOR)
					returntextRect = returntext.get_rect()
					returntextRect.center = (int(boardsize / 2), int(3 * boardsize / 4))
					disp.blit(returntext,returntextRect)


					pygame.display.update()
					for event in pygame.event.get():
							if event.type == MOUSEBUTTONDOWN:
									disp.fill(BLACK)
									return False
							if(event.type == QUIT):
									sys.exit()


class GoToJailSpace(Space):
        def __init__(self,name,picture,spaceType):
                Space.__init__(self)
                self.name = name
                self.picture = picture
                self.type = spaceType

        def display(self,boardsize,disp):
                BLACK = (  0,   0,   0)
                WHITE = (255, 255, 255)
                TEXTCOLOR = WHITE
                BGCOLOR = BLACK
		cornersize = 1.5*(boardsize/12.0)
		rect = pygame.Rect(cornersize,cornersize,boardsize-(2*cornersize),boardsize-(2*cornersize))
		pygame.draw.rect(disp,BLACK,rect)
                while True:
                        fontsize = int(boardsize*.06)
                        DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
                        name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR)
                        nameRect = name.get_rect()
                        nameRect.center = (int(boardsize / 2), int(boardsize / 4))
                        disp.blit(name,nameRect)
                        fontsize = int(boardsize*.03)
                        DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)
			toJail = DISPLAYFONT.render('Land here, go to jail', True, (255,0,0), BGCOLOR)
			toJailRect = toJail.get_rect()
			toJailRect.center = (int(boardsize / 2), int(boardsize / 2))
			disp.blit(toJail,toJailRect)
                        fontsize = int(boardsize*.02)
                        DISPLAYFONT = pygame.font.Font('freesansbold.ttf',fontsize)
                        returntext = DISPLAYFONT.render("Click anywhere to return.", True, TEXTCOLOR, BGCOLOR)
                        returntextRect = returntext.get_rect()
                        returntextRect.center = (int(boardsize / 2), int(3 * boardsize / 4))
                        disp.blit(returntext,returntextRect)


                        pygame.display.update()
                        for event in pygame.event.get():
                                if event.type == MOUSEBUTTONDOWN:
                                        disp.fill(BLACK)
                                        return False
                                if(event.type == QUIT):
                                        sys.exit()


                        pygame.display.update()
                        for event in pygame.event.get():
                                if event.type == MOUSEBUTTONDOWN:
                                        disp.fill(BLACK)
                                        return False
                                if(event.type == QUIT):
                                        sys.exit()

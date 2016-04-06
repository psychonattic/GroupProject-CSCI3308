from abc import ABCMeta
import random, sys, pygame, time, copy
from pygame.locals import *
class Space:

	 __metaclass__ = ABCMeta

	 def display(self):
	 	return

class GoSpace(Space):

	def __init__(self,name,picture,spaceType): 
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

	def __init__(self,name,picture,spaceType,color,houses,hotels,price,rent,mortgage,housecost,owner): 
		self.name = name
		self.picture = picture
		self.type = spaceType
		self.color = color
		self.houses = houses
		self.hotels = hotels
		self.price = price
		self.rent = rent
		self.mortgage = mortgage
		self.housecost = housecost
		self.owner = owner

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
	def __init__(self,name,picture,spaceType,owner,price,rent,mortgage):
		self.name = name
		self.picture = picture
		self.type = spaceType
		self.owner = owner
		self.price = price
		self.rent = rent
		self.mortgage = mortgage

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

class CommunityChestSpace(Space):
	def __init__(self,name,picture,spaceType):
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

class JailSpace(Space):  #Still need to figure out what's going on with Jail Space/Just Visiting

        def __init__(self,name,picture,spaceType):
                self.name = name
                self.picture = picture
                self.type = spaceType
		self.injail = None #['Ted','Nathan','Joel','John','Chase'] 

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


class UtilitiesSpace(Space):

        def __init__(self,name,picture,spaceType,cost,mortgage,owner):
                self.name = name
                self.picture = picture
                self.type = spaceType
		self.cost = cost
		self.rent = '4x dice roll'
		self.mortgage = mortgage
		self.bothowned = False
		self.owner = owner

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
			cost = DISPLAYFONT.render('Cost: $' + str(self.cost), True, TEXTCOLOR,BGCOLOR)
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

class GoToJailSpace(Space):

        def __init__(self,name,picture,spaceType):
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

class FreeParkingSpace(Space):

        def __init__(self,name,picture,spaceType):
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








				
		





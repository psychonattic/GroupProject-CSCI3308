from abc import ABCMeta
import random, sys, pygame, time, copy
from pygame.locals import *
class Space:

	 __metaclass__ = ABCMeta

	 def display(self):
	 	return

class GoSpace(Space):

	def __init__(self,name,picture,spaceType): #should be form (self, string, int, int, int, int)
		self.name = name
		self.picture = picture
		self.type = spaceType

	def display(self,boardsize,disp):
		# print self.name
		# print self.picture
		# print self.type
		global BLACK, WHITE, GREEN, RED, TEXTCOLOR, BGCOLOR
		BLACK = (  0,   0,   0) 
		WHITE = (255, 255, 255)
		GREEN = (  0, 155,   0)
		RED = (255,0,0)
		TEXTCOLOR = WHITE
		BGCOLOR = BLACK
		while True:
			fontsize = int(boardsize*.04)
			DISPLAYFONT = pygame.font.Font('freesansbold.ttf', fontsize)  #font for start screen
			name = DISPLAYFONT.render(self.name, True, TEXTCOLOR, BGCOLOR) #renders start button
			nameRect = name.get_rect() #gets the rect value of start button
			nameRect.center = (int(boardsize / 2), int(boardsize / 3)) #places start button on botton of the screen
			disp.blit(name,nameRect)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONDOWN:  #checks for mouse click
					disp.fill(BLACK) 
					return False
				if(event.type == QUIT):
					sys.exit()
				
		





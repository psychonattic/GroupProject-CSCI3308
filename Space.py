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

	def display(self):
		print self.name
		print self.picture
		print self.type
		






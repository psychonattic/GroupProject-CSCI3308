import sys, pygame
import time
import random
from pygame.locals import *
from gameboard import *
class Dice:
    
    def __init__(self, boardsize):
        pygame.init()
        self.boardsize = boardsize
        
        self.DISPLAY = pygame.display.set_mode((boardsize, boardsize))
        self.fpsClock = pygame.time.Clock()
        self.cornersize = 2*(boardsize/13) #height and width of corner board pieces
        self.edgewidth = (boardsize/13) #width of non-corner board pieces
        self.edgeheight = 2*(boardsize/13) #height of non-corner board pieces

    global BLACK, WHITE, BRIGHT_WHITE, GREEN, TEXTCOLOR, BGCOLOR, dice1, dice2, dice3, dice4, dice5, dice6    
    BLACK      = (  0,   0,   0) 
    WHITE      = (200, 200, 200)
    BRIGHT_WHITE = (255, 255, 255)
    GREEN      = (  0, 155,   0)
    TEXTCOLOR = WHITE
    BGCOLOR = BLACK
    
    
    dice1 = pygame.image.load('images/dice/1.png')
    dice2 = pygame.image.load('images/dice/2.png')
    dice3 = pygame.image.load('images/dice/3.png')
    dice4 = pygame.image.load('images/dice/4.png')
    dice5 = pygame.image.load('images/dice/5.png')
    dice6 = pygame.image.load('images/dice/6.png')
    
    #player1 = Player(0,0,0)
    #print player1.money
    
    
    
    def text_objects(text, font, color):
        textSurface = font.render(text, True, color) #Create surface
        return textSurface, textSurface.get_rect()
        
    
    def rng(self):
        die1 = random.randrange(1, 7) #rng for dice
        die2 = random.randrange(1, 7)
        return (die1, die2)
    

    
    def dice_roll(self, d1):
        #match generated number with image
        while True:
            if d1 == 1:
                return (dice1)
            elif d1 == 2:
                return (dice2)
            elif d1 == 3:
                return (dice3)
            elif d1 == 4:
                return (dice4)
            elif d1 == 5:
                return (dice5)
            elif d1 == 6:
                return (dice6)
        
    def dice_roll2(self, d2):
        #generate 2nd die
        while True:
            if d2 == 1:
                return (dice1)
            elif d2 == 2:
                return (dice2)
            elif d2 == 3:
                return (dice3)
            elif d2 == 4:
                return (dice4)
            elif d2 == 5:
                return (dice5)
            elif d2 == 6:
                return (dice6)
            
            


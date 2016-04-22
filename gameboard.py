import random, sys, pygame, time, copy
from pygame.locals import *
from Space import *
from dice import *
from player import *

class GameBoard:

    def __init__(self, boardsize,Framepersecond, spaces, players):
        pygame.init()
        self.d1 = 0 #initialize dice values
        self.d2 = 0
        self.boardsize = boardsize
        self.Framepersecond = Framepersecond
        self.spaces = spaces
        self.players = players
        self.DISPLAY = pygame.display.set_mode((boardsize, boardsize),RESIZABLE)
        self.GAMEFONT = pygame.font.Font('freesansbold.ttf', 20)
        self.fpsClock = pygame.time.Clock()
        self.cornersize = 1.5*(boardsize/12.0) #height and width of corner board pieces
        self.edgewidth = 1.0*(boardsize/12.0) #width of non-corner board pieces
        self.edgeheight = 1.5*(boardsize/12.0) #height of non-corner board pieces
        self.endturn = False
        self.turn = 0

        

    global BLACK, WHITE, GREEN, RED, TEXTCOLOR, BGCOLOR
    BLACK = (  0,   0,   0) 
    WHITE = (255, 255, 255)
    GREEN = (  0, 155,   0)
    RED = (255,0,0)
    TEXTCOLOR = WHITE
    BGCOLOR = BLACK


    def run(self): #main game loop - currently just has a quit button
        #self.DISPLAY = pygame.display.set_mode((self.boardsize, self.boardsize),RESIZABLE)
        self.DISPLAY.fill(BLACK)
        dice = Dice(self.boardsize)
        pygame.display.set_caption('Mod-opoly')
        beginSurf = self.GAMEFONT.render('Options', True, TEXTCOLOR, BGCOLOR) #renderes options button
        optionRect = beginSurf.get_rect() #gets rect value of options button
        optionRect.bottomright = (self.boardsize-self.cornersize, self.boardsize-self.cornersize) #puts options button in corner
        
        rollSurf = pygame.font.Font(None, 40).render('Roll', True, BLACK, GREEN) #renders roll button
        rollRect = rollSurf.get_rect() #rect for option button
        rollRect.center = (int(self.boardsize / 2), 150) #centers roll button

        endTurnSurf = pygame.font.Font(None, 40).render('End Turn', True, BLACK, GREEN) #renders roll button
        endTurnRect = endTurnSurf.get_rect()
        endTurnRect.center = (int(self.boardsize / 2), (self.boardsize/6)*2)
        
        self.drawBoard(self.d1, self.d2) #send dice values to drawBoard
        if(not self.endturn):
            self.DISPLAY.blit(rollSurf, rollRect) #displays roll button
        self.DISPLAY.blit(beginSurf,optionRect) #displays options button
        if(self.endturn):
            self.DISPLAY.blit(endTurnSurf,endTurnRect)
        pygame.display.update() #updates the screen
        self.fpsClock.tick(self.Framepersecond)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN: #checks for mouse click
                mousex, mousey = event.pos #saves x,y values of mouse click
                if optionRect.collidepoint((mousex, mousey)): #checks if mouse click is in options button
                    self.optionScreen() #quits the run loop
                if rollRect.collidepoint((mousex, mousey)) and not self.endturn:
                    self.d1, self.d2 = dice.rng() #if roll is clicked, set values of d1, d2 to range(1-6)
                    self.players[self.turn].pos += self.d1 + self.d2
                    self.players[self.turn].pos %= 40
                    self.endturn = True
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

    #def playerTurn(playerIndex,)

    def diceDisplay(self, d1, d2):
        dice = Dice(self.boardsize)

        die1 = dice.dice_roll(d1) #gets image for d1
        die2 = dice.dice_roll2(d2) #gets image for d2
        self.DISPLAY.blit(die1, (125, 375)) #displays d1
        self.DISPLAY.blit(die2, (375, 375)) #displays d2
        
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

    def drawPlayers(self):
        """
        #Replace first 3 lines with this to test icon centering
        for i in range(0, 40):
            piecePos = i
            piece = pygame.image.load(self.pieces[i]).convert()
        """
        for i in range(len(self.players)):
            piecePos = self.players[i].pos #should be something like: piecePos = self.player[i].pos
            piece = pygame.image.load(self.players[i].icon).convert()
            piece = pygame.transform.scale(piece,(50,50))
            spaceSize1 = abs(self.spaces[piecePos].edge3-self.spaces[piecePos].edge1)
            spaceSize2 = abs(self.spaces[piecePos].edge4-self.spaces[piecePos].edge2)
            centerSpace1 = abs(self.spaces[piecePos].edge1-(spaceSize1/2.0))
            centerSpace2 = abs(self.spaces[piecePos].edge2-(spaceSize2/2.0))
            (tokenWidth, tokenHeight) = piece.get_size()
            self.DISPLAY.blit(piece, (centerSpace1-tokenWidth/2.0, centerSpace2-tokenHeight/2.0))


    def drawBoard(self, d1, d2): #DRAWS THE BOARD EVERY TURN	
        ximage = int(self.edgewidth)
        yimage = int(self.edgeheight)
        endpoint = long(self.boardsize-self.cornersize)
        blitdest = [(endpoint,endpoint),(0,endpoint),(0,0),(endpoint,0)] #Array for blit destinations
        
        if d1 != 0 and d2 != 0: #if button has been pressed dice appear
            self.diceDisplay(d1, d2)
        
        #Displays each corner piece
        for i in range(0,4):
            self.spaces[i*10].edge1 = blitdest[i][0]+self.cornersize
            self.spaces[i*10].edge2 = blitdest[i][1]+self.cornersize
            self.spaces[i*10].edge3 = blitdest[i][0]
            self.spaces[i*10].edge4 = blitdest[i][1]
            corner = pygame.image.load(self.spaces[i*10].picture).convert() #Convert image to new pixel format
            corner = pygame.transform.scale(corner,(yimage,yimage)) #Scale image
            self.DISPLAY.blit(corner,blitdest[i]) #Display corner piece at blit destination
            pygame.draw.rect(self.DISPLAY,BLACK,(blitdest[i][0],blitdest[i][1],self.cornersize,self.cornersize),2)
        
        #Displays each non-corner piece
        spacepos = long(endpoint-self.edgewidth) #start to the left of "Go" for bottom row
        for i in range(1,10)+range(11,20)+range(21,30)+range(31,40): #Skip corners
            if i == 11:
                #Start above Jail for left column
                spacepos = long(endpoint-self.edgewidth)
            elif i == 21 or i == 31:
                #Start at the top corners for the other two sides
                spacepos = long(self.cornersize)

            image = pygame.image.load(self.spaces[i].picture).convert()
            
            if i > 0 and i < 10:
                self.spaces[i].edge1 = spacepos+self.edgewidth
                self.spaces[i].edge2 = self.boardsize
                self.spaces[i].edge3 = spacepos
                self.spaces[i].edge4 = self.boardsize-self.edgeheight
                image = pygame.transform.scale(image, (ximage, yimage)) #Scale by x, y for rows
                self.DISPLAY.blit(image,(spacepos,endpoint))
                pygame.draw.rect(self.DISPLAY,BLACK,(spacepos,endpoint,self.edgewidth,self.edgeheight),2)
                spacepos -= self.edgewidth #Go from right to left by subtracting
            elif i > 10 and i < 20:
                self.spaces[i].edge1 = 0
                self.spaces[i].edge2 = spacepos+self.edgewidth
                self.spaces[i].edge3 = self.edgeheight
                self.spaces[i].edge4 = spacepos
                image = pygame.transform.scale(image, (yimage, ximage)) #Scale by y, x for cols
                self.DISPLAY.blit(image,(0,spacepos))
                pygame.draw.rect(self.DISPLAY,BLACK,(0,spacepos,self.edgeheight,self.edgewidth),2)
                spacepos -= self.edgewidth #Go from bottom to top
            elif i > 20 and i < 30:
                self.spaces[i].edge1 = spacepos+self.edgewidth
                self.spaces[i].edge2 = 0
                self.spaces[i].edge3 = spacepos
                self.spaces[i].edge4 = self.edgeheight
                image = pygame.transform.scale(image, (ximage, yimage))
                self.DISPLAY.blit(image, (spacepos,0))
                pygame.draw.rect(self.DISPLAY,BLACK,(spacepos,0,self.edgewidth,self.edgeheight),2)
                spacepos += self.edgewidth #Go from left to right
            elif i > 30 and i <40:
                self.spaces[i].edge1 = self.boardsize
                self.spaces[i].edge2 = spacepos+self.edgewidth
                self.spaces[i].edge3 = self.boardsize-self.edgeheight
                self.spaces[i].edge4 = spacepos
                image = pygame.transform.scale(image, (yimage, ximage))
                self.DISPLAY.blit(image,(endpoint,spacepos))
                pygame.draw.rect(self.DISPLAY,BLACK,(endpoint,spacepos,self.edgeheight,self.edgewidth),2)
                spacepos += self.edgewidth #Go from top to bottom
                
        self.drawPlayers()
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


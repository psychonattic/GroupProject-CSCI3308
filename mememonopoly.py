import random, sys, pygame, time, copy
from pygame.locals import *
from player import Player
from gameboard import *


global spaces 
spaces = []
space0 = GoSpace("go","./images/corner_bottom_right","gospace")
space1 = GoSpace("Mediteranean Avenue","./images/bottom9","gospace")
space2 = GoSpace("Community Chest","./images/bottom8","gospace")
space3 = GoSpace("Baltic Avenue","./images/bottom7","gospace")
space4 = GoSpace("Income Tax","./images/bottom6","gospace")
space5 = GoSpace("Reading Railroad","./images/bottom5","gospace")
space6 = GoSpace("Oriental Avenue","./images/bottom4","gospace")
space7 = GoSpace("Change","./images/bottom3","gospace")
space8 = GoSpace("Vermont Avenue","./images/bottom3","gospace")
space9 = GoSpace("Conneticut Avenue","./images/bottom2","gospace")
space10 = GoSpace("Just Visiting","./images/corner_bottom_left","gospace")
space11 = GoSpace("St. Charles Place","./images/left9","gospace")
space12 = GoSpace("Electric Company",".images/left8","gospace")
space13 = GoSpace("Sates Avenue","./images/left7","gospace")
space14 = GoSpace("Virginia Avenue","./images/left6","gospace")
space15 = GoSpace("Pennsylvania Railroad","./images/left5","gospace")
space16 = GoSpace("St. James Place","./images/left4","gospace")
space17 = GoSpace("Community Chest","./images/left3","gospace")
space18 = GoSpace("Tennessee Avenue","./images/left2","gospace")
space19 = GoSpace("New York Avenue","./images/left1","gospace")
space20 = GoSpace("Free Parking","./images/corner_top_left","gospace")
space21 = GoSpace("Kentucky Avenue","./images/top1","gospace")
space22 = GoSpace("Chance","./images/top2","gospace")
space23 = GoSpace("Indiana Avenue","./images/top3","gospace")
space24 = GoSpace("Illinois Avenue","./images/top4","gospace")
space25 = GoSpace("B. B. O. Railroad","./images/top5","gospace")
space26 = GoSpace("Atlantic Avenue","./images/top6","gospace")
space27 = GoSpace("Venice Avenue","./images/top7","gospace")
space28 = GoSpace("Water Works","./images/top8","gospace")
space29 = GoSpace("Marvin Gardens","./images/top9","gospace")
space30 = GoSpace("GO TO JAIL","./images/corner_top_right","gospace")
space31 = GoSpace("Pacific Avenue","./images/right1","gospace")
space32 = GoSpace("North Carolina Avenue","./images/right2","gospace")
space33 = GoSpace("Community Chest","./images/right3","gospace")
space34 = GoSpace("Pennsylvania Avenue","./images/right4","gospace")
space35 = GoSpace("Short Line","./images/right5","gospace")
space36 = GoSpace("Chance","./images/right6","gospace")
space37 = GoSpace("Dark Place","./images/right7","gospace")
space38 = GoSpace("Luxury Tax","./images/right8","gospace")
space39 = GoSpace("Boardwalk","./images/right9","gospace")
space40 = GoSpace("Jail","./images/jail","gospace")
spaces.append(space0)
spaces.append(space1)
spaces.append(space2)
spaces.append(space3)
spaces.append(space4)
spaces.append(space5)
spaces.append(space6)
spaces.append(space7)
spaces.append(space8)
spaces.append(space9)
spaces.append(space10)
spaces.append(space11)
spaces.append(space12)
spaces.append(space13)
spaces.append(space14)
spaces.append(space15)
spaces.append(space16)
spaces.append(space17)
spaces.append(space18)
spaces.append(space19)
spaces.append(space20)
spaces.append(space21)
spaces.append(space22)
spaces.append(space23)
spaces.append(space24)
spaces.append(space25)
spaces.append(space26)
spaces.append(space27)
spaces.append(space28)
spaces.append(space29)
spaces.append(space30)
spaces.append(space31)
spaces.append(space32)
spaces.append(space33)
spaces.append(space34)
spaces.append(space35)
spaces.append(space36)
spaces.append(space37)
spaces.append(space38)
spaces.append(space39)
spaces.append(space40)



def main():
	board = GameBoard(600,20,spaces) #boardsize, fps 
	board.startScreen()
	while True:
		if board.run() == False:
			break
		board.fpsClock.tick(board.Framepersecond) #limits how fast the screen can updat by framepersecond

		

main()

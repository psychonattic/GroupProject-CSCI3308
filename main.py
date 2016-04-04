import random, sys, pygame, time, copy
from pygame.locals import *
from player import Player
from gameboard import *

default_names = ["Go","Mediterranean Ave.","Community Chest","Baltic Ave.","Income Tax","Reading Railroad",
"Oriental Ave.","Chance","Vermont Ave.","Connecticut Ave.","Just Visiting/Jail","St. Charles Place",
"Electric Company","States Ave.","Virginia Ave.","Pennsylvania Railroad","St. James Place","Community Chest",
"Tennessee Ave.","New York Ave.","Free Parking","Kentucky Ave.","Chance","Indiana Ave.","Illinois Ave.",
"B. & O. Railroad","Atlantic Ave.","Ventnor Ave.","Water Works","Marvin Gardens","Go to Jail","Pacific Ave.",
"North Carolina Ave.","Community Chest","Pennsylvania Ave.","Short Line Railroad","Chance","Park Place",
"Luxury Tax","Boardwalk","Jail"]
default_spaces = []

for i in range(0, 40):
    default_spaces.append(GoSpace(default_names[i], "./images/themes/default/space"+str(i)+".jpg", "gospace"))
def main(boardsize, fps, boardspaces):
    pygame.init()
    done = False
    clock = pygame.time.Clock()

    board = GameBoard(boardsize, fps, boardspaces)
    board.startScreen()

    while board.run() != False:
        clock.tick(fps)

main(600, 20, default_spaces)

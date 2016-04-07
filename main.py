import random, sys, pygame, time, copy
from pygame.locals import *
from player import Player
from gameboard import *
from sys import argv
import itertools
import os
import csv

def loadSpacesError():
    default_path = "./images/themes/default/"
    if os.path.exists(default_path+"titles.csv"):
        with open(default_path+"titles.csv", 'rb') as defaultfile:
            colreader = csv.reader(defaultfile, delimiter=',')
            colnum = len(colreader.next())
            defaultfile.close()
            if colnum < 40:
                print "Default theme does not contain titles for all 40 spaces. Please reinstall game files."
                exit(0)
            else:
                for i in range(0, 40):
                    if os.path.exists(default_path+"space"+str(i)+".jpg") == False:
                        print "Default theme does not contain image files for all 40 spaces. Please reinstall game files."
                        exit(0)
                print "Reverting to default theme."
                return loadSpaces("default")
    else:
        print "Default theme does not exist. Please reinstall game files." 
        exit(0)

def loadSpaces(theme_name):
    space_titles = []
    try:
        with open("./images/themes/"+theme_name+"/titles.csv", 'rb') as titlesfile:
            reader1, reader2 = itertools.tee(csv.reader(titlesfile, delimiter=','))
            title_count = len(reader1.next())
            del reader1
            if title_count < 40:
                print theme_name+"/titles.csv does not contain titles for all 40 spaces."
                titlesfile.close()
                if theme_name != "default":
                    return loadSpacesError()
                else:
                    print "Error loading default theme. Please reinstall game files."
                    exit(0)
            for title in reader2.next():
                space_titles.append(str(title)) 
            titlesfile.close()
    except:
        print "Theme \'%s\' does not exist." % theme_name
        if theme_name != "default":
            return loadSpacesError()
        else:
            print "Error loading default theme. Please reinstall game files."
            exit(0)

    spaces = []
    for i in range(0, 40):
        image_path = "./images/themes/"+theme_name+"/space"+str(i)+".jpg" 
        if os.path.exists(image_path):
            spaces.append(GoSpace(space_titles[i], image_path, "gospace"))
        else:
            print "Theme \'%s\' does not contain image files for all 40 spaces." % theme_name
            if theme_name != "default":
                return loadSpacesError()
            else:
                print "Error loading default theme. Please reinstall game files."
                exit(0)

    return spaces

def main(boardsize, fps, boardspaces):
    pygame.init()
    done = False
    clock = pygame.time.Clock()

    board = GameBoard(boardsize, fps, boardspaces)
    board.startScreen()

    while board.run() != False:
        clock.tick(fps)

if __name__ == '__main__': #Turns out it's impossible to do unit tests without this
    if len(argv) == 2:
        main(600, 20, loadSpaces(argv[1]))
    else:
        main(600, 20, loadSpaces("default"))


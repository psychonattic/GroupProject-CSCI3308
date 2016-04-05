import random, sys, pygame, time, copy
from pygame.locals import *
from player import Player
from gameboard import *
from start import *
from sys import argv
import itertools
import os
import csv

def loadSpacesError():
    default_path = "./images/themes/" + theme_name + "/"
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

    # spaces = []
    # for i in range(0, 40):
    #     image_path = "./images/themes/" + theme_name + "_name+"/space"+str(i)+".jpg" 
    #     if os.path.exists(image_path):
    #         spaces.append(GoSpace(space_titles[i], image_path, "gospace"))
    #     else:
    #         print "Theme \'%s\' does not contain image files for all 40 spaces." % theme_name
    #         if theme_name != "default":
    #             return loadSpacesError()
    #         else:
    #             print "Error loading default theme. Please reinstall game files."
    #             exit(0)

    return createBoardSpaces(theme_name)



def main(boardsize, fps, boardspaces):
    pygame.init()
    done = False
    clock = pygame.time.Clock()

    start = Start(boardsize)
    (pieces, numplayers) = start.startnew()

    board = GameBoard(boardsize, fps, boardspaces)
    board.run()

    while board.run() != False:
        clock.tick(fps)



def createBoardSpaces(theme_name):
    spaces = []
    space0 = GoSpace("GO","./images/themes/" + theme_name + "/space0.jpg","gospace")
    space1 = PropertySpace("Mediteranean Avenue","./images/themes/default/space1.jpg","propertyspace","Brown",None,None,60,2,30,50,"John")
    space2 = CommunityChestSpace("Community Chest","./images/themes/" + theme_name + "/space2.jpg","communitychestspace")
    space3 = PropertySpace("Baltic Avenue","./images/themes/" + theme_name + "/space3.jpg","propertyspace","Brown",None,None,60,4,30,50,"Mandy")
    space4 = TaxSpace("Income Tax","./images/themes/" + theme_name + "/space4.jpg","taxspace")
    space5 = RailRoadSpace("Reading Railroad","./images/themes/" + theme_name + "/space5.jpg","railroadspace",None,200,25,100)
    space6 = PropertySpace("Oriental Avenue","./images/themes/" + theme_name + "/space6.jpg","propertyspace","Light Blue",None,None,100,6,50,50,None)
    space7 = ChanceSpace("Chance","./images/themes/" + theme_name + "/space7.jpg","chancespace")
    space8 = PropertySpace("Vermont Avenue","./images/themes/" + theme_name + "/space8.jpg","propertyspace","Light Blue",None,None,100,6,50,50,None)
    space9 = PropertySpace("Connecticut Avenue","./images/themes/" + theme_name + "/space9.jpg","propertyspace","Light Blue",None,None,120,8,60,50,None)
    space10 = JailSpace("Just Visiting / In Jail","./images/themes/" + theme_name + "/space10.jpg","jailspace")
    space11 = PropertySpace("St. Charles Place","./images/themes/" + theme_name + "/space11.jpg","propertyspace","Pink",None,None,140,10,70,100,None)
    space12 = UtilitiesSpace("Electric Company","./images/themes/" + theme_name + "/space12.jpg","utilitiesspace",150,75,None)
    space13 = PropertySpace("States Avenue","./images/themes/" + theme_name + "/space13.jpg","propertyspace","Pink",None,None,140,10,70,100,None)
    space14 = PropertySpace("Virginia Avenue","./images/themes/" + theme_name + "/space14.jpg","propertyspace","Pink",None,None,160,12,80,100,None)
    space15 = RailRoadSpace("Pennsylvania Railroad","./images/themes/" + theme_name + "/space15.jpg","railroadspace",'Ted',200,25,100)
    space16 = PropertySpace("St. James Place","./images/themes/" + theme_name + "/space16.jpg","propertyspace","Orange",None,None,180,14,90,100,None)
    space17 = CommunityChestSpace("Community Chest","./images/themes/" + theme_name + "/space17.jpg","communitychestspace")
    space18 = PropertySpace("Tennessee Avenue","./images/themes/" + theme_name + "/space18.jpg","propertyspace","Orange",None,None,180,14,90,100,None)
    space19 = PropertySpace("New York Avenue","./images/themes/" + theme_name + "/space19.jpg","propertyspace","Orange",None,None,200,16,100,100,None)
    space20 = FreeParkingSpace("Free Parking","./images/themes/" + theme_name + "/space20.jpg","freeparkingspace")
    space21 = PropertySpace("Kentucky Avenue","./images/themes/" + theme_name + "/space21.jpg","propertyspace","Red",None,None,220,18,110,150,None)
    space22 = ChanceSpace("Chance","./images/themes/" + theme_name + "/space22.jpg","chancespace")
    space23 = PropertySpace("Indiana Avenue","./images/themes/" + theme_name + "/space23.jpg","propertyspace","Red",None,None,220,18,110,150,None)
    space24 = PropertySpace("Illinois Avenue","./images/themes/" + theme_name + "/space24.jpg","propertyspace","Red",None,None,240,20,120,150,None)
    space25 = RailRoadSpace("B. & O. Railroad","./images/themes/" + theme_name + "/space25.jpg","railroadspace",None,200,25,100)
    space26 = PropertySpace("Atlantic Avenue","./images/themes/" + theme_name + "/space26.jpg","propertyspace","Yellow",None,None,260,22,130,150,None)
    space27 = PropertySpace("Ventnor Avenue","./images/themes/" + theme_name + "/space27.jpg","propertyspace","Yellow",None,None,260,22,130,150,None)
    space28 = UtilitiesSpace("Water Works","./images/themes/" + theme_name + "/space28.jpg","utilitiesspace",150,75,None)
    space29 = PropertySpace("Marvin Gardens","./images/themes/" + theme_name + "/space29.jpg","propertyspace","Yellow",None,None,280,24,140,150,None)
    space30 = GoToJailSpace("GO TO JAIL","./images/themes/" + theme_name + "/space30.jpg","gotojailspace")
    space31 = PropertySpace("Pacific Avenue","./images/themes/" + theme_name + "/space31.jpg","propertyspace","Green",None,None,300,26,150,200,None)
    space32 = PropertySpace("North Carolina Avenue","./images/themes/" + theme_name + "/space32.jpg","propertyspace","Green",None,None,300,26,150,200,None)
    space33 = CommunityChestSpace("Community Chest","./images/themes/" + theme_name + "/space33.jpg","communitychestspace")
    space34 = PropertySpace("Pennsylvania Avenue","./images/themes/" + theme_name + "/space34.jpg","propertyspace","Green",None,None,320,28,160,200,None)
    space35 = RailRoadSpace("Short Line","./images/themes/" + theme_name + "/space35.jpg","railroadspace",None,200,25,100)
    space36 = ChanceSpace("Chance","./images/themes/" + theme_name + "/space36.jpg","chancespace")
    space37 = PropertySpace("Dark Place","./images/themes/" + theme_name + "/space37.jpg","Propertyspace","Dark Blue",None,None,350,35,175,200,None)
    space38 = TaxSpace("Luxury Tax","./images/themes/" + theme_name + "/space38.jpg","taxspace")
    space39 = PropertySpace("Boardwalk","./images/themes/" + theme_name + "/space39.jpg","Propertyspace","Dark Blue",None,None,400,50,200,200,None)
    #space40 = GoSpace("Jail","./images/themes/" + theme_name + "/space40.jpg","gospace")
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
#spaces.append(space40)
    return spaces


if len(argv) == 2:
    main(600, 20, loadSpaces(argv[1]))
else:
    main(600, 20, loadSpaces("default"))

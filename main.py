import random, sys, pygame, time, copy
from pygame.locals import *
from player import Player
from gameboard import *
from start import *
from sys import argv
import itertools
import os
import csv

#Whenever an error arises, this function is called
def loadSpacesError(isDefault):
    if not isDefault:
        #Tries to load the default theme if an error arises in another theme
        print "Attempting to load default theme"
        return loadSpaces("default")
    else:
        #If there's an issue with loading the default theme, exit the program
        print "Error loading default theme. Please reinstall game files."
        exit(0)

def loadSpaces(theme_name):
    #Lists for each of the six columns in spaces.csv
    space_titles = []
    space_types = []
    space_prices = []
    property_rent = []
    house_prices = []
    property_colors = []
    csv_path = "./images/themes/"+theme_name+"/spaces.csv"
    if os.path.exists(csv_path):
        with open(csv_path, 'rb') as titlesfile:
            #itertools.tee sets up a second reader: One gets the # of cols for each row
            #The other goes through each row and appends spaces to their appropriate lists
            reader1, reader2 = itertools.tee(csv.reader(titlesfile, delimiter=','))
            row_counts = [] #Where the # of cols for each row goes
            purchasable_count = 0 # of purchasable space
            utility_count = 0 # of utility spaces
            property_count = 0 # of property spaces
            for i in range(0,6): #First reader - gets # cols in each row
                row_counts.append(len(reader1.next()))
            del reader1

            #Ensures first two rows have 40 cols - necessary in any monopoly game
            if row_counts[0] < 40 or row_counts[1] < 40:
                print theme_name+"/spaces.csv does not contain titles and/or types for all 40 spaces."
                titlesfile.close()
                return loadSpacesError(theme_name == "default")

            #Begin appending titles and types to their respective lists
            for title in reader2.next():
                space_titles.append(str(title)) 
            for stype in reader2.next():
                space_types.append(str(stype))
                #Get # of purchasables, properties, utilities
                if stype in ["property", "railroad", "utility"]:
                    purchasable_count += 1
                    if stype == "property":
                        property_count += 1
                    elif stype == "utility":
                        utility_count += 1

            #Since utilities don't take a rent parameter, they must be subtracted from # of purchasables
            if row_counts[2] == purchasable_count and row_counts[3] == purchasable_count-utility_count:
                for price in reader2.next():
                    space_prices.append(int(price))
                for rent in reader2.next():
                    property_rent.append(int(rent))
            else:
                print "Number of given prices and/or rent does not match number of purchasable spaces."
                titlesfile.close()
                return loadSpacesError(theme_name == "default")

            #Last two rows apply to properties only
            if  row_counts[4] == property_count and row_counts[5] == property_count:
                for house_price in reader2.next():
                    house_prices.append(int(house_price))
                for color in reader2.next():
                    property_colors.append(str(color))
            else:
                print "Number of house costs and/or colors does not match number of property spaces."
                titlesfile.close()
                return loadSpacesError(theme_name == "default")
            
            titlesfile.close() #Always remember to close out of the file!

    else:
        print "Path to theme \'%s\' does not exist or %s/spaces.csv does not exist." % (theme_name, theme_name)
        return loadSpacesError(theme_name == "default")

    spaces = []
    for i in range(0, 40):
        image_path = "./images/themes/"+theme_name+"/space"+str(i)+".jpg" 
        #Ensure the image path exists for all 40 images
        if os.path.exists(image_path):
            #Then append the appropriate space class with the information grabbed from spaces.csv
            if space_types[i] == "property":
                spaces.append(PropertySpace(space_titles[i], image_path, space_types[i], property_colors.pop(0), space_prices.pop(0), property_rent.pop(0), house_prices.pop(0)))
            elif space_types[i] == "railroad":
                spaces.append(RailRoadSpace(space_titles[i], image_path, space_types[i], space_prices.pop(0), property_rent.pop(0)))
            elif space_types[i] == "utility":
                spaces.append(UtilitiesSpace(space_titles[i], image_path, space_types[i], space_prices.pop(0)))
            elif space_types[i] == "tax":
                spaces.append(TaxSpace(space_titles[i], image_path, space_types[i]))
            elif space_types[i] == "chest":
                spaces.append(CommunityChestSpace(space_titles[i], image_path, space_types[i]))
            elif space_types[i] == "chance":
                spaces.append(ChanceSpace(space_titles[i], image_path, space_types[i]))
            elif space_types[i] == "go":
                spaces.append(GoSpace(space_titles[i], image_path, space_types[i]))
            elif space_types[i] == "jail":
                spaces.append(JailSpace(space_titles[i], image_path, space_types[i]))
            elif space_types[i] == "parking":
                spaces.append(FreeParkingSpace("Free Parking", image_path, space_types[i]))
            elif space_types[i] == "gotojail":
                spaces.append(GoToJailSpace(space_titles[i], image_path, space_types[i]))
        else:
            #Some image space0.png-space39.png does not exist
            print "Theme \'%s\' does not contain image files for all 40 spaces." % theme_name
            return loadSpacesError(theme_name == "default")

    return spaces

def main(boardsize, fps, boardspaces):
    pygame.init()
    done = False
    clock = pygame.time.Clock()

    start = Start(boardsize)
    (pieces, numplayers) = start.startnew()

    board = GameBoard(boardsize, fps, boardspaces, pieces)
    board.run()

    while board.run() != False:
        clock.tick(fps)

if __name__ == '__main__': #Turns out it's impossible to do unit tests without this
    if len(argv) == 2:
        main(600, 20, loadSpaces(argv[1]))
    else:
        main(600, 20, loadSpaces("default"))


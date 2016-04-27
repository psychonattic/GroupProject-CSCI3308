# GroupProject-CSCI3308

## Who:
 * John Gallagher: John-Gallagher
 * Ted Freeman: TheoFr
 * Chase Heck: whattheheck11
 * Joel Barkley: Psychonattic
 * Nathan Carmine: ncarmine

## Mod Monopoly (Mod-opoly)

## Description:
An open source, customizable Monopoly clone written in pygame

## Vision Statement:
To create an open source Monopoly game using pygame, with the ability to customize the board to the user's liking.

## Motivation: 
To make players smile while combining our love of modularity and board game.

## Risks: 
 * Limited experience with pygames framework
 * Cross-platform difficulties (Windows, Mac OS, Linux, etc.)
 * Schedule conflicts among group members
 * No prior experience working with the group members
 * Legal/copyright questions

## Mitigation strategy for dealing with the risk:
 * We will each research Pygames to familiarize ourselves with it
 * We can perform development on the school computers, giving us equal development environments
 * We will only use open-source graphics or create our own to take away legal risk
 * We will meet regularly at predefined times to discuss the project, using online tools to schedule

## User Requirements
  * As a user I want an Intuitive UI so that I can easily use the program.
    * ID Number: 1
    * Story Points: 40
  * As a user I want to see the current status of the board so I can make gameplay decisions.
    * ID Number: 2
    * Story Points: 35
  * As a user I want to know where my game piece is to make buying and selling decisions in-game.
    * ID Number: 3
    * Story Points: 20
  * As a user I want to know where other players' game pieces are in order to make gameplay decisions.
    * ID Number: 4
    * Story Points: 25
  * As a user I want the game to save the game progress so that I can play in discrete sessions.
    * ID Number: 5
    * Story Points: 10

## Functional Requirements
  * As a user I want a single player mode so that I can play if I don’t have another person to play with. (AI)
    * ID Number: 6
    * Story Points: 45
  * As a user I need to be able to buy properties and gain money from chance and community chest properties so that I get more enjoyment from the game.
    * ID Number: 7
    * Story Points: 32
  * As a user I want to be able to role dice to progress along the board.
    * ID Number: 8
    * Story Points: 5
  * As a user I want to be able to win the game by bankrupting the other players. 
    * ID Number: 9
    * Story Points: 7
  * As a user I want to be able to play against at least one other human player.
    * ID Number: 10
    * Story Points: 42

## Non-Functional Requirements
  * As a user I want to see my high scores or the number of wins so I can see how well I have done in the past.
    * ID Number: 11
    * Story Points: 14
  *  As a user I want to see aesthetically pleasing graphics when I play the game so that I play it more.
    * ID Number: 12
    * Story Points: 27
  * As a user I want to be able to choose different game pieces so that I can customize the experience.
    * ID Number: 13
    * Story Points: 13
  * As a user I want to be able to change the difficulty of the AI in order to tailor the game to my skill level.
    * ID Number: 14
    * Story Points: 50
  * As a user I want to be able to play agianst up to 3 other players.
    * ID Number: 15
    * Story Points: 39

## Methodology: 
Agile Process

## Project Tracking software:
[Trello Link Here](https://trello.com/b/IyxuIwpX/meme-monopoly)

## Project plan: 
![alt text](https://cloud.githubusercontent.com/assets/14183096/13134718/e07562dc-d5c6-11e5-95ed-69e5f7f78775.png "Trello Board Screenshot")

##RUN:
* Download the git project and extract it.
* In the terminal, navigate to the directory GroupProject-CSCI3308-master
* Run the command: python main.py
* To run a custom theme, add the theme name after main.py.  For example run: python main.py high-res for a high res version of the board.

##THEMES:
To create a new theme:
 - Create a new directory under `./images/themes` with the name of your theme. Eg: `./images/themes/MyTheme`
 - Each theme directory should contain the following:
 	- 40 images titled `space0.jpg` to `space39.jpg`. Each image corresponds to the 40 spaces on the board, starting at "Go" (space0) and going clockwise around the board, ending at "Boardwalk" (space39).
 	- A `spaces.csv` file with six rows
 - Each row in `spaces.csv` should be as follows:
	 1. The title of each of the 40 spaces, starting at Go, going clockwise. (40 cols)
	 2. The type of each space. There are different 10 spaces: (40 cols)
	 	- "property" - A purchasable property that can have houses on it
	 	- "railroad" - A purchasable railroad space, traditionally four on a board, in the middle of each row
	 	- "utility" - A purchasable utility space, traditionally two on a board.
	 	- "tax" - Income/Luxury Tax space. Non-purchasable. Traditionally two on a board
	 	- "chest" - Community Chest space. Non-purchasable. Draw a Community Chest card.
	 	- "chance" - Chance space. Non-purchasable. Draw a Chance card.
	 	- "go" - The initial space you start at. bottom-right corner
	 	- "jail" - In Jail/Just Visiting space. bottom-left corner of the board.
	 	- "parking" - The Free Parking space. top-left corner.
	 	- "gotojail" - Player goes to jail when on this space. top-right corner.
	 3. The price for each of the purchasable spaces. This includes properties, railroads, and utilities. (# of cols = # of properties + railroads + utilities on the board)
	 4. The rent for each of the purchasable spaces, not inluding utilities. (# of cols = # of properties + railroads)
	 5. The cost for each house. This is not the rent cost with houses, this is the price required to get one additional house. (# of cols = # of properties)
	 6. The color of each property. (# of cols = # of properties)

To run the program with your selected theme:  
`python main.py MyTheme`

If your theme does not work, the game will automatically revert to the default theme. If you remove, add, or modify anything in the `./images/themes/default/` directory, you may have to reinstall the game files.

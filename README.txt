Description: The goal of the game is to navigate the maze with the arrow keys and reach the objectives spread throughout while avoiding the guard that will try to 
find the player based on the objectives detonation being heard or the player being seen.


Requirements:
	Python 3.7
	Pygame
	Windows System


How to run:
1. On a windows system if Python3.7 is not already installed visit https://www.python.org/ to download and install Python3.7

2. Depending on the system you may need to set up an Environment Path Variable, this is checked by typing "python" into the terminal, if it is already set up it
will state the python version and enter the python terminal, if the version is not 3.7 then there is already a path to an installed python which will need to be
changed. This is done by right clicking on "This Computer" in the windows explorer and selecting "Properties" then "Advanced." Select the "Environment
Variables" option and look for the "Path" variable, selected it and press "Edit", we don't need to overwrite it since we can append to it. Add a semi-colon at
the end and then add one path to the Python3.7 directory and another to the Scripts folder, the scripts will be needed for pip3. An example would be these two paths
"C:\Users\<user>\AppData\Local\Programs\Python\Python37-32" and "C:\Users\<user>\AppData\Local\Programs\Python\Python37-32\Scripts"

3. With the Environment Path Variables set up, next is to install Pygame if it is not already installed, this is done by typing the command "pip3 install pygame" into
the terminal

4. Everything is installed and the game can be ran with the terminal command "python game.py" while its in the directory of the game


File functional descriptions:
game.py-
	This is the main driver file for the game. This is where all the entities (Player, Guard, Bombs, Level) are created and contains the method for updating the display
GameLoop.py-
	This file contains the checks for events, meaning keyboard input and flips bools so the game can act on the inputs
photo_rect.py-
	This is the wrapper for the images, it just contains the directory to the image, loads the image, and scales it to the appropriate size, this is used on every sprite
	in the game
Level.py-
	This file contains the class for how the maze is stored in the game, this includes reading from the file and initializing the data and drawing in the walls of the maze
Player.py-
	This file contains the class for the player, it manages the movement based on the bools that were flipped by key events detected in GameLoop.py and the animations
	related to the movement of the player
bomb.py-
	This file contains the class for the objective the player needs to reach, it checks whether or not he player steps into the bomb's location to start detonation,
	handles the animations related to the explosion, and alerts the guard so it can path to the bomb
enemy.py-
	This file contains the class for the guard, the guard uses the AI algorithm we decided upon, A Star, to generate the path to follow its patrol, the maze is recreated
	inside the guard as a set of coordinates that contain "obstacles" for use with the AI algorithm, but the main purpose of this file is to use the AI algorithm to create
	a path and then follow the path. It also contains a method called "sight()" which is used to see if the guard can "see" the player, and if it does it calls the AI to
	generate a path to the player's position
a_star.py
	This file contains the A Star algorithm to generate a path from the starting x and y position to the goal x and y position based on the obstacle x and y positions. 
	It uses the euclidean distance from the current state to the goal state as the heurisitc, and uses helper methods such as "vert_valid" and "get_index"
	to help create and identify if certain steps are possible
Maze.txt-
	This file is the text file containing the details of the maze that is used
Graphic Folder-
	This folder contains all the images used for the game, separated into subfolders based on the specific entity they are for

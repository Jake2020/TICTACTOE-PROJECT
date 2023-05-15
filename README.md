# JAKE'S TICTACTOE PROJECT - CS50p FINAL PROJECT

## Project Requirements:
- Your project must be implemented in Python.
- Your project must have a main function and three or more additional functions. At least three of those additional functions must be accompanied by tests that can be executed with pytest.
- Your main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of your project.
- Your 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main (i.e., not nested under any classes or functions).
- Your test functions must be in a file called test_project.py, which should also be in the “root” of your project. Be sure they have the same name as your custom functions, prepended with test_ (test_custom_function, for example, where custom_function is a function you’ve implemented in project.py).
- You are welcome to implement additional classes and functions as you see fit beyond the minimum requirement.
- Implementing your project should entail more time and effort than is required by each of the course’s problem sets.
- Any pip-installable libraries that your project requires must be listed, one per line, in a file called requirements.txt in the root of your project.

## My Project:

#### Video Demo: https://youtu.be/2bt9lmyxZUY

#### DESCRIPTION: My project is a Python application that allows 2 players to play TicTacToe vs each other in the termal window. This is achieved by having each player type the position on the board they want to move to expressed as a coordinate e.g. 0-0 would be top-left and 2-2 would be bottom left. At the beggining of the game and after each move, the terminal prints out the current board state so the players can visually see the game state. If any moves are invalid, e.g. out of range or negitive inputs, the players are re-prompted with an error message until they input a valid move. After each move the program check to see if the game has ended and print out who was the winner, otherwise the game continues.

###### ######################################################################
## Quick Start Guide:

###### Launching App:
In "CS50p_project" folder execute "python project.py".

Follow instructions in the terminal to play the game.

###### ######################################################################

## Reflections:

Two things that I would do to improve the project are:

1 - Find a way of displaying the board with horizontal seperator lines. Each way I tried this made the board look wrong so I stuck with just vertical seperators which looks tidy but not exactly how you may imagine a TicTacToe board.

2 - Change what is asked for as input from the user. Currently I ask the user for a position from 0 - 2 but normal users would likely expect top right to be 1-1 not 0-0. I could update the project in future to be more user friendly.

Other than these 2 things I am happy with the project.

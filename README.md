# JAKE'S TICTACTOE PROJECT - CS50p FINAL PROJECT

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
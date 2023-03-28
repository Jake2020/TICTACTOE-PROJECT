# Play a game of TicTacToe in the terminal

def main():

    # Initilize board
    board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
    ]

    # Print out starting (empty) board
    print()
    print_board(board)
    print()

    # Assign players their symbol
    player1 = 'X'
    player2 = 'O'

    # Tell the players
    print(f"Player 1 will be {player1}'s")
    print(f"Player 2 will be {player2}'s")
    print()

    # Start the game
    play(board, player1, player2)


def print_board(board):
    # Print out the current board formatted for visibility
    for row in board:
        print('| {} | {} | {} |'.format(row[0], row[1], row[2]))


def get_move(player):
    # Get players move

    # Prompt player for an input
    print(f"Player {player}'s turn")
    print()
    while True:
        # Keep prompting until valid move provided
        try:
            move = input("Enter row and column numbers (0-2) separated by a space e.g. '0 1': ")
            row, col = [int(x) for x in move.split()]
            if row < 0 or row > 2 or col < 0 or col > 2:
                raise ValueError
            break
        except (ValueError, IndexError):
            print()
            print("Invalid input. Try again.")
            print()
    return row, col


def play(board, player1, player2):
    # Run the game

    # Initilize game
    current_player = player1
    winner = None

    # While no winner and board isn't filled
    while not winner and any('-' in row for row in board):

        # Prompt player for an input
        row, col = get_move(current_player)

        # Reprompt if position taken
        if board[row][col] != '-':
            print()
            print("That spot is already taken. Try again.")
            print()
            continue

        # Fill chosen location with current player's symbol
        board[row][col] = current_player
        print_board(board)
        print()

        # Check whether that move results in a win
        if check_win(board, current_player):
            winner = current_player
            print(f"Congratulations! {winner} wins!")
            print()

        # Move to next player and continue
        else:
            current_player = player2 if current_player == player1 else player1

    # If no one wins - Draw
    if not winner:
        print("It's a draw!")
        print()


def check_win(board, player):
    # Check win conditions

    # check rows
    for row in board:
        if all(spot == player for spot in row):
            return True

    # check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # check Top-Left to Bottom-Right diagonal
    if all(board[i][i] == player for i in range(3)):
        return True

    # check Top-Right to Bottom-Left diagonal
    if all(board[i][2-i] == player for i in range(3)):
        return True

    # Return false if no winner
    return False


if __name__ == "__main__":
    main()
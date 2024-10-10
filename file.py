# Tic-Tac-Toe Game in Python

# Function to print the board
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check for a win
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]  # diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (tie)
def check_tie(board):
    return all(space != ' ' for space in board)

# Main game function
def tic_tac_toe():
    board = [' '] * 9  # Empty 3x3 board
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}, choose a position (1-9): ")

        try:
            move = int(input()) - 1
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        if move < 0 or move > 8 or board[move] != ' ':
            print("Invalid move! Try again.")
            continue

        # Make the move
        board[move] = current_player

        # Check if current player won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()
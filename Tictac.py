# Function to print the current state of the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

# Function to check if the board is full (no more moves)
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to handle player moves
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Please choose a number between 1 and 9.")
                continue
            
            # Convert move to row and column
            row, col = divmod(move - 1, 3)
            
            # Check if the cell is empty
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Cell is already occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Main function to run the game
def tic_tac_toe():
    # Initialize an empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Display welcome message
    print("Welcome to Tic-Tac-Toe!")
    
    # Alternate between player X and player O
    current_player = "X"
    
    while True:
        print_board(board)
        player_move(board, current_player)
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    tic_tac_toe()

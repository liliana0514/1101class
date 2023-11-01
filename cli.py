from logi import check_winner_board

def get_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def print_board(board):
  for row in board:
    print(row)

def get_player_input(current_player):
    """
    input:
        row,col
    return:
        row : int --> the index of row
        col : int --> the index of colum
    """
    
    prompt = f"player{current_player}>"
    player_input = input(prompt) #this is a str
    print(player_input)
    # how to make the str into two int
    # "1,1".split(',') --> ["1","1"]
    row_col_list = player_input.split(',') #["1","1"]
    #[1,1]
    row, col = [int(x) for x in row_col_list]
    return row,col

def switch_player(current_player):
    if current_player == "X":
       return "O"
    return "X"

if __name__ == '__main__':
    current_player = "X"
    # get an empty board
    board = get_empty_board()
    # print the board
    winner = None

    while winner is None:
        print_board(board)
        # ask user input
        
        try:
            row,col = get_player_input(current_player)
        except ValueError:
           print("Invalid input, try again")
           continue

        
        # Mark the board
        board[row][col]=current_player

        # check for winner
        winner = check_winner_board(board)

        # current_player = "X" if current_player == "O" else "O"
        current_player = switch_player(current_player)
    
    print_board(board)
    print(f"Winner is {switch_player(current_player)}")

  # check for winner
  # check if game is draw
  # print the winner

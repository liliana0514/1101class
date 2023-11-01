def get_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def print_board(board):
  for row in board:
    print(row)

def get_player_input():
    """
    return:
        row : int --> the index of row
        col : int --> the index of colum
    """
    player_input = input(f">")
    print(player_input)

if __name__ == '__main__':
  # get an empty board
  board=get_empty_board()
  #print the board
  print_board(board)
  # ask user input
  row,col = get_player_input()
  # check for winner
  # check if game is draw
  # print the winner

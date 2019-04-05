import numpy as np

def create_board():
    board = np.zeros((6, 7))
    return board

def make_selection(player):
    selection = input(f"Player {player} make selection (0 - 6): ")
    try:
        if 0 <= int(selection) <= 6:
            selection = int(selection)
            return selection
        else:
            raise Exception
    except:
        print("Invalid selection. Try again.")
        return None

def drop_piece(col, is_player_one, board):
    try:
        drop_piece_helper(col, is_player_one, board)
        return True
    except:
        print("No more room in that column. Try again.")
        return False

def drop_piece_helper(col, is_player_one, board):
    for i in range(len(board)):
        if board[-1-i][col] == 0:
            board[-1-i][col] = 1 if is_player_one else 2
            return
    raise Exception

board = create_board()
game_over = False
is_player_one = True

while not game_over:
    if is_player_one:
        selection = make_selection(1)
        if selection is None:
            continue
        d = drop_piece(selection, is_player_one, board)
        if not d:
            continue
    else:
        selection = make_selection(2)
        if selection is None:
            continue
        d = drop_piece(selection, is_player_one, board)
        if not d:
            continue
    print(board)
    is_player_one = not is_player_one

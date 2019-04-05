import numpy as np

def create_board():
    board = np.zeros((6, 7))
    return board

def make_selection(player):
    selection = input(f"Player {player} make selection (0 - 6): ")
    try:
        if 0 <= int(selection) <= 6:
            selection = int(selection)
        else:
            raise Exception
    except:
        print("Invalid selection. Try again.")
        return None
    return selection

board = create_board
game_over = False
is_player_one = True

while not game_over:
    if is_player_one:
        selection = make_selection(1)
        if selection is None:
            continue
    else:
        selection = make_selection(2)
        if selection is None:
            continue
    is_player_one = not is_player_one



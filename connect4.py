import numpy as np


def build_all_vals(board):
    all_vals = []
    for row in board:
        for val in row:
            all_vals.append(val)
    return all_vals


def check_diagonals(board):
    all_vals = build_all_vals(board)
    # Upward >> /
    for i in range(21, 39):
        if all_vals[i] > 0:
            if all_vals[i] == all_vals[i-6] == all_vals[i-12] == all_vals[i-18]:
                return True
    # Downward >> \
    for i in range(24, 42):
        if all_vals[i] > 0:
            if all_vals[i] == all_vals[i-8] == all_vals[i-16] == all_vals[i-24]:
                return True
    return False


def check_horizontal(board):
    for row in board:
        for i in range(len(row) - 4):
            if row[i] > 0:
                if row[i] == row[i+1] == row[i+2] == row[i+3]:
                    return True
    return False


def check_vertical(board):
    all_vals = build_all_vals(board)
    for i in range(21, 42):
        if all_vals[i] > 0:
            if all_vals[i] == all_vals[i-7] == all_vals[i-14] == all_vals[i-21]:
                return True
    return False


def create_board():
    board = np.zeros((6, 7))
    return board


def drop_piece(col, player, board):
    for i in range(len(board)):
        if board[-1-i][col] == 0:
            board[-1-i][col] = player
            return True
    print("No more room in that column. Try again.")
    return False


def is_winning_move(board):
    return check_horizontal(board) \
        or check_vertical(board) \
        or check_diagonals(board)


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


def main():
    board = create_board()
    game_over = False
    is_player_one = True

    while not game_over:
        print("-|0||1||2||3||4||5||6|-")
        print(board)
        player = 1 if is_player_one else 2
        selection = make_selection(player)
        if selection is None:
            continue
        d = drop_piece(selection, player, board)
        if not d:
            continue
        if is_winning_move(board):
            print("-|0||1||2||3||4||5||6|-")
            print(board)
            print("-----------")
            print(f"PLAYER {player} IS THE WINNER!")
            game_over = True
        is_player_one = not is_player_one


if __name__ == "__main__":
    main()

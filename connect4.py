import numpy as np


HUMAN, AI = 1, 2
ROWS, COLS = 6, 7


def main():
    board = create_board()
    game_over = False
    is_player_one = True
    while not game_over:
        print_board(board)
        player = HUMAN if is_player_one else AI
        selection = make_selection(player)
        if selection is None:
            continue
        d = drop_piece(selection, player, board)
        if not d:
            continue
        if is_winning_move(board):
            print_board(board)
            print(f"-----------\nPLAYER {player} IS THE WINNER!")
            game_over = True
        if is_full_board():
            print("No more moves. Draw.")
            game_over = True
        is_player_one = not is_player_one


def build_all_vals(board):
    all_vals = []
    for row in board:
        for val in row:
            all_vals.append(val)
    return all_vals


def check_diagonals(board):
    all_vals = build_all_vals(board)
    # Upward >> /
    for i in range(COLS * 3, ROWS * COLS - 3):
        if all_vals[i] > 0 and i >= 0:
            if all_vals[i] == all_vals[i-COLS+1] == all_vals[i-COLS*2+2] \
                == all_vals[i-COLS*3+3]:
                return True
    # Downward >> \
    for i in range(COLS * 3 + 3, ROWS * COLS):
        if all_vals[i-COLS*3-3] > 0 and i-COLS*3-3 >= 0:
            if all_vals[i] == all_vals[i-COLS-1] == all_vals[i-COLS*2-2] \
                == all_vals[i-COLS*3-3]:
                return True
    return False


def check_horizontal(board):
    for row in board:
        for i in range(COLS - 3):
            if row[i] > 0:
                if row[i] == row[i+1] == row[i+2] == row[i+3]:
                    return True
    return False


def check_vertical(board):
    all_vals = build_all_vals(board)
    for i in range(COLS * 3, COLS * ROWS):
        if all_vals[i] > 0:
            if all_vals[i] == all_vals[i-COLS] \
                == all_vals[i-COLS*2] == all_vals[i-COLS*3]:
                return True
    return False


def create_board():
    board = np.zeros((ROWS, COLS))
    return board


def drop_piece(col, player, board):
    for i in range(len(board)):
        if board[-1-i][col] == 0:
            board[-1-i][col] = player
            return True
    print("No more room in that column. Try again.")
    return False


def is_full_board(board):
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == 0:
                return False
    return True


def is_winning_move(board):
    return check_horizontal(board) \
        or check_vertical(board) \
        or check_diagonals(board)


def make_selection(player):
    selection = input(f"Player {player} make selection (0 - 6): ")
    try:
        if 0 <= int(selection) <= COLS - 1:
            selection = int(selection)
            return selection
        else:
            raise Exception
    except:
        print("Invalid selection. Try again.")
        return None


def print_board(board):
    print("-|0||1||2||3||4||5||6|-")
    print(board)




if __name__ == "__main__":
    main()

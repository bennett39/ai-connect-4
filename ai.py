import numpy as np
import random
import time

import connect4 as c4


CENTER_WEIGHT = 4
DOUBLE_WEIGHT = 2
TRIPLE_WEIGHT = 5
QUADRUPLE_WEIGHT = 10000
OPP_DOUBLE_WEIGHT = -2
OPP_TRIPLE_WEIGHT = -100


def main():
    human, ai = 1, 2
    board = c4.create_board()
    game_over = False
    is_human = True
    while not game_over:
        c4.print_board(board)
        player = human if is_human else ai
        if is_human:
            print("Your turn")
            selection = c4.make_selection(human)
            if selection is None:
                continue
        else:
            print("AI turn")
            time.sleep(1)
            selection = ai_select_column(board)
        d = c4.drop_piece(selection, player, board)
        if not d:
            continue
        if c4.is_winning_move(board):
            c4.print_board(board)
            print(f"-----------\nPLAYER {player} IS THE WINNER!")
            game_over = True
        is_human = not is_human


def ai_select_column(board):
    weights = weigh_columns(board)
    return weights.index(max(weights))


def check_diagonals(board, row, col):
    return 0


def check_horizontals(board, row, col):
    lo = 0 if col < 3 else col - 3
    hi = 4 if col > 3 else col + 1
    score = CENTER_WEIGHT if col == 3 else 0
    for i in range(lo, hi):
        score += score_window(board[row][i:i+4])
    return score


def check_verticals(board, row, col):
    return 0


def score_window(window):
    window_score = 0
    if 1 not in window:
        pieces_in_window = np.count_nonzero(window == 2)
        window_score += weigh_pieces(pieces_in_window)
    else:
        # TODO - Add defensive incentives
        pass
    return window_score


def weigh_pieces(num_pieces):
    if num_pieces == 0:
        return 0
    if num_pieces == 1:
        return DOUBLE_WEIGHT
    if num_pieces == 2:
        return TRIPLE_WEIGHT
    if num_pieces == 3:
        return QUADRUPLE_WEIGHT



def weigh_columns(board):
    weights = []
    for col in range(7):
        row = 5
        while row >= 0 and board[row][col] != 0:
            row -= 1
        weights.append(weigh_position(board, row, col))
    return weights


def weigh_position(board, row, col):
    return check_horizontals(board, row, col) \
            + check_verticals(board, row, col) \
            + check_diagonals(board, row, col)




if __name__ == "__main__":
    main()

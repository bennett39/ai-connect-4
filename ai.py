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
    board = c4.create_board()
    game_over = False
    is_human = True
    while not game_over:
        c4.print_board(board)
        player = c4.HUMAN if is_human else c4.AI
        if is_human:
            print("Your turn")
            selection = c4.make_selection(c4.HUMAN)
            if selection is None:
                continue
        else:
            print("AI turn")
            time.sleep(1)
            selection = select_column(board)
        d = c4.drop_piece(selection, player, board)
        if not d:
            continue
        if c4.is_winning_move(board):
            c4.print_board(board)
            print(f"-----------\nPLAYER {player} IS THE WINNER!")
            game_over = True
        is_human = not is_human


def score_diagonals(board, row, col):
    score = 0
    for i in range(4):
        start_row, start_col = row + i - 3, col + i - 3
        if 0 <= start_row <= c4.ROWS - 4 and 0 <= start_col <= c4.COLS - 4:
            window = np.array([
                board[start_row][start_col],
                board[start_row + 1][start_col + 1],
                board[start_row + 2][start_col + 2],
                board[start_row + 3][start_col + 3]
            ])
            score += score_window(window)
        start_row = row - i + 3
        if c4.ROWS - 3 <= start_row <= c4.ROWS - 1 and 0 <= start_col <= c4.COLS- 4:
            window = np.array([
                board[start_row][start_col],
                board[start_row - 1][start_col + 1],
                board[start_row - 2][start_col + 2],
                board[start_row - 3][start_col + 3]
            ])
            score += score_window(window)
    return score


def score_horizontals(board, row, col):
    score = 0
    for i in range(c4.COLS - 3):
        if col - 3 <= i:
            score += score_window(board[row][i:i+4])
    return score


def score_verticals(board, row, col):
    score = 0
    for i in range(c4.ROWS - 3):
        if row - 3 <= i:
            window = np.array(
                [board[i][col], board[i+1][col],
                board[i+2][col], board[i+3][col]]
            )
            score += score_window(window)
    return score


def score_window(window):
    window_score = 0
    if c4.HUMAN not in window:
        pieces_in_window = np.count_nonzero(window == c4.AI)
        window_score += weigh_pieces(pieces_in_window)
    else:
        # TODO - Add defensive incentives
        pass
    return window_score


def select_column(board):
    weights = weigh_columns(board)
    return weights.index(max(weights))


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
    for col in range(c4.COLS):
        if board[0][col] == 0: # Col is not full
            row = c4.ROWS - 1
            while row >= 0 and board[row][col] != 0:
                row -= 1
            weights.append(weigh_position(board, row, col))
        else:
            weights.append(0)
    return weights


def weigh_position(board, row, col):
    if row < 0 or row >= c4.ROWS or col < 0 or col >= c4.COLS:
        return 0
    return score_horizontals(board, row, col) \
            + score_verticals(board, row, col) \
            + score_diagonals(board, row, col) \
            + (CENTER_WEIGHT if col == 3 else 0)


if __name__ == "__main__":
    main()

import pytest
import connect4 as c4
import ai


def test_select_column():
    player = c4.AI
    board = c4.create_board()
    assert ai.select_column(board, player) == 3


def test_score_diagonals():
    player = c4.AI
    test_board = c4.create_board()
    assert ai.score_diagonals(test_board, 3, 3, player) == 0
    test_board[5][1] = c4.AI
    assert ai.score_diagonals(test_board, 3, 3, player) == ai.DOUBLE_WEIGHT
    test_board[4][2] = c4.HUMAN
    assert ai.score_diagonals(test_board, 3, 3, player) == ai.DOUBLE_WEIGHT - 1


def test_score_horizontals():
    player = c4.AI
    test_board = c4.create_board()
    assert ai.score_horizontals(test_board, 5, 3, player) == 0
    test_board[5][6] = c4.AI
    assert ai.score_horizontals(test_board, 5, 3, player) == ai.DOUBLE_WEIGHT
    test_board[5][5] = c4.AI
    assert ai.score_horizontals(test_board, 5, 3, player) == \
            ai.DOUBLE_WEIGHT + ai.TRIPLE_WEIGHT
    test_board[5][4] = c4.AI
    assert ai.score_horizontals(test_board, 5, 3, player) > ai.QUADRUPLE_WEIGHT
    test_board[5][4] = c4.HUMAN
    assert ai.score_horizontals(test_board, 5, 3, player) == ai.DOUBLE_WEIGHT - 1


def test_score_verticals():
    player = c4.AI
    test_board = c4.create_board()
    assert ai.score_verticals(test_board, 3, 3, player) == 0
    test_board[5][3] = c4.AI
    assert ai.score_verticals(test_board, 3, 3, player) == ai.DOUBLE_WEIGHT
    test_board[4][3] = c4.AI
    assert ai.score_verticals(test_board, 3, 3, player) == \
            ai.TRIPLE_WEIGHT + ai.DOUBLE_WEIGHT
    test_board[2][3] = c4.AI
    assert ai.score_verticals(test_board, 3, 3, player) > ai.QUADRUPLE_WEIGHT
    test_board[4][3] = c4.HUMAN
    test_board[1][3] = c4.HUMAN
    assert ai.score_verticals(test_board, 3, 3, player) == 0


def test_weigh_columns():
    player = c4.AI
    test_board = c4.create_board()
    assert ai.weigh_columns(test_board, player)[2] == 0
    assert ai.weigh_columns(test_board, player)[3] == 4
    for i in range(c4.ROWS):
        test_board[i][3] = 99
    assert ai.weigh_columns(test_board, player)[3] == 0
    test_board = c4.create_board()
    test_board[5][2] = c4.AI
    test_board[5][3] = c4.AI
    test_board[5][4] = c4.HUMAN
    assert ai.weigh_columns(test_board, player)[1] == ai.TRIPLE_WEIGHT

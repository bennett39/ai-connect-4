import pytest
import connect4 as c4
import ai


def test_select_column():
    board = c4.create_board()
    assert ai.select_column(board) == 3


def test_score_diagonals():
    test_board = c4.create_board()
    assert ai.score_diagonals(test_board, 5, 3) == 0
    c4.drop_piece(4, c4.HUMAN, test_board)
    c4.drop_piece(3, c4.AI, test_board)
    assert ai.score_diagonals(test_board, 4, 4) == 2
    c4.drop_piece(5, c4.AI, test_board)
    assert ai.score_diagonals(test_board, 4, 4) == 4
    c4.drop_piece(3, c4.HUMAN, test_board)
    assert ai.score_diagonals(test_board, 3, 3) == 2
    c4.drop_piece(6, c4.AI, test_board)
    assert ai.score_diagonals(test_board, 4, 5) == 2
    c4.drop_piece(6, c4.AI, test_board)
    assert ai.score_diagonals(test_board, 3, 6) == 0
    c4.drop_piece(1, c4.AI, test_board)
    assert ai.score_diagonals(test_board, 4, 0) == 0


def test_score_horizontals():
    test_board = c4.create_board()
    assert ai.score_horizontals(test_board, 5, 3) == 0
    test_board = c4.create_board()
    c4.drop_piece(3, c4.HUMAN, test_board)
    c4.drop_piece(1, c4.AI, test_board)
    assert ai.score_horizontals(test_board, 5, 2) == 0
    test_board = c4.create_board()
    c4.drop_piece(3, c4.HUMAN, test_board)
    c4.drop_piece(3, c4.AI, test_board)
    c4.drop_piece(2, c4.HUMAN, test_board)
    assert ai.score_horizontals(test_board, 4, 2) == 6


def test_weigh_columns():
    test_board = c4.create_board()
    assert ai.weigh_columns(test_board)[2] == 0
    assert ai.weigh_columns(test_board)[3] == 4

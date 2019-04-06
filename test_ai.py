import pytest
import connect4 as c4
import ai


def test_ai_select_column():
    board = c4.create_board()
    assert 0 <= ai.ai_select_column(board) <= 6


def test_check_horizontals():
    test_board = c4.create_board()
    assert ai.score_horizontals(test_board, 5, 3) == 4
    test_board = c4.create_board()
    c4.drop_piece(3, 1, test_board)
    c4.drop_piece(1, 2, test_board)
    assert ai.score_horizontals(test_board, 5, 2) == 0
    test_board = c4.create_board()
    c4.drop_piece(3, 1, test_board)
    c4.drop_piece(3, 2, test_board)
    c4.drop_piece(2, 1, test_board)
    assert ai.score_horizontals(test_board, 4, 2) == 6

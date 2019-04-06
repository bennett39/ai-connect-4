import numpy as np
import pytest
import connect4 as c4


def test_create_board():
    """ Creates an empty board """
    board = c4.create_board()
    model = np.zeros((6, 7))
    for i in range(len(board)):
        for j in range(len(board[0])):
            assert board[i][j] == model[i][j]


def test_build_all_vals():
    """ Concatenates matrix into single list """
    board = c4.create_board()
    assert c4.build_all_vals(board) == [0 for _ in range(42)]


def test_check_diagonals():
    """ Finds a diagonal win. Returns false if not """
    test_board = c4.create_board()
    assert c4.check_diagonals(test_board) == False
    for i in range(4):
        test_board[i][i] = 1
    assert c4.check_diagonals(test_board) == True
    test_board[1][1] = 2
    assert c4.check_diagonals(test_board) == False


def test_check_horizontal():
    """ Finds a horizontal win. Returns false if not """
    test_board = c4.create_board()
    assert c4.check_horizontal(test_board) == False
    for i in range(4):
        test_board[3][i] = 1
    assert c4.check_horizontal(test_board) == True
    test_board[3][2] = 2
    assert c4.check_horizontal(test_board) == False


def test_check_vertical():
    """ Finds a vertical win. Returns False if not """
    test_board = c4.create_board()
    assert c4.check_vertical(test_board) == False
    for i in range(4):
        test_board[i][5] = 2
    assert c4.check_vertical(test_board) == True
    test_board[2][5] = 1
    assert c4.check_horizontal(test_board) == False


def test_drop_piece():
    """ Adds a new piece to the board & returns True. False if new piece
    can't be added to that column.
    """
    test_board = c4.create_board()
    c4.drop_piece(1, 1, test_board)
    assert test_board[-1][1] == 1
    c4.drop_piece(2, 2, test_board)
    assert test_board[-1][2] == 2
    c4.drop_piece(1, 1, test_board)
    assert test_board[-2][1] == 1
    for i in range(6):
        c4.drop_piece(6, 1, test_board)
    assert c4.drop_piece(6, 2, test_board) == False


def test_is_winning_move():
    """ Checks for a winner. Returns bool """
    test_board = c4.create_board()
    assert c4.is_winning_move(test_board) == False
    for i in range(4):
        test_board[i][i] = 1
    assert c4.is_winning_move(test_board) == True
    for i in range(4):
        test_board[i][6-i] = 2
    assert c4.is_winning_move(test_board) == True
    for i in range(4):
        test_board[1][2+i] = 2
    assert c4.is_winning_move(test_board) == True
    for i in range(4):
        test_board[1+i][4] = 1
    assert c4.is_winning_move(test_board) == True
    for i in range(0, 6, 2):
        test_board[3][i] = 1
        test_board[3][i+1] = 2
        test_board[4][i] = 2
        test_board[4][i+1] = 1
    assert c4.is_winning_move(test_board) == False


def test_make_selection(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "1")
    assert c4.make_selection(1) == 1
    monkeypatch.setattr('builtins.input', lambda x: "5")
    assert c4.make_selection(1) == 5
    monkeypatch.setattr('builtins.input', lambda x: "abc")
    assert c4.make_selection(1) is None
    monkeypatch.setattr('builtins.input', lambda x: "8")
    assert c4.make_selection(1) is None


pytest.main()

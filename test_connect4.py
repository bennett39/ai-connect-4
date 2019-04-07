import numpy as np
import pytest
import connect4 as c4


def test_create_board():
    """ Creates an empty board """
    board = c4.create_board()
    model = np.zeros((c4.ROWS, c4.COLS))
    for i in range(c4.ROWS):
        for j in range(c4.COLS):
            assert board[i][j] == model[i][j]


def test_build_all_vals():
    """ Concatenates matrix into single list """
    board = c4.create_board()
    assert c4.build_all_vals(board) == [0 for _ in range(c4.ROWS * c4.COLS)]


def test_check_diagonals():
    """ Finds a diagonal win. Returns false if not """
    test_board = c4.create_board()
    assert c4.check_diagonals(test_board) == False
    for i in range(4):
        test_board[i][i] = c4.HUMAN
    assert c4.check_diagonals(test_board) == True
    test_board[1][1] = c4.AI
    assert c4.check_diagonals(test_board) == False


def test_check_horizontal():
    """ Finds a horizontal win. Returns false if not """
    test_board = c4.create_board()
    assert c4.check_horizontal(test_board) == False
    for i in range(4):
        test_board[3][i] = c4.HUMAN
    assert c4.check_horizontal(test_board) == True
    test_board[3][2] = c4.AI
    assert c4.check_horizontal(test_board) == False


def test_check_vertical():
    """ Finds a vertical win. Returns False if not """
    test_board = c4.create_board()
    assert c4.check_vertical(test_board) == False
    for i in range(4):
        test_board[i][5] = c4.AI
    assert c4.check_vertical(test_board) == True
    test_board[2][5] = c4.HUMAN
    assert c4.check_horizontal(test_board) == False


def test_drop_piece():
    """ Adds a new piece to the board & returns True. False if new piece
    can't be added to that column.
    """
    test_board = c4.create_board()
    c4.drop_piece(1, c4.HUMAN, test_board)
    assert test_board[-1][1] == c4.HUMAN
    c4.drop_piece(2, c4.AI, test_board)
    assert test_board[-1][2] == c4.AI
    c4.drop_piece(1, c4.HUMAN, test_board)
    assert test_board[-2][1] == c4.HUMAN
    for i in range(6):
        c4.drop_piece(6, c4.HUMAN, test_board)
    assert c4.drop_piece(6, c4.AI, test_board) == False


def test_is_winning_move():
    """ Checks for a winner. Returns bool """
    test_board = c4.create_board()
    assert c4.is_winning_move(test_board) == False
    for i in range(4):
        test_board[i][i] = c4.HUMAN
    assert c4.is_winning_move(test_board) == True
    for i in range(4):
        test_board[i][6-i] = c4.AI
    assert c4.is_winning_move(test_board) == True
    for i in range(4):
        test_board[1][2+i] = c4.AI
    assert c4.is_winning_move(test_board) == True
    for i in range(4):
        test_board[1+i][4] = c4.HUMAN
    assert c4.is_winning_move(test_board) == True
    for i in range(0, 6, 2):
        test_board[3][i] = c4.HUMAN
        test_board[3][i+1] = c4.AI
        test_board[4][i] = c4.AI
        test_board[4][i+1] = c4.HUMAN
    assert c4.is_winning_move(test_board) == False


def test_make_selection(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "1")
    assert c4.make_selection(c4.HUMAN) == 1
    monkeypatch.setattr('builtins.input', lambda x: "5")
    assert c4.make_selection(c4.HUMAN) == 5
    monkeypatch.setattr('builtins.input', lambda x: "abc")
    assert c4.make_selection(c4.HUMAN) is None
    monkeypatch.setattr('builtins.input', lambda x: "8")
    assert c4.make_selection(c4.HUMAN) is None


pytest.main()

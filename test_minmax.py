import pytest

import connect4 as c4
import minmax as mx


def test_build_tree():
    board = c4.create_board()
    tree = mx.build_tree(board, c4.AI)
    tree.root.children[3].val == 4

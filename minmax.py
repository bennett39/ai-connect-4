import copy
import ai


class Node(object):
    def __init__(self, position=-1, val=0):
        self.position = position
        self.val = val
        self.children = []


class Tree(object):
    def __init__(self):
        self.root = Node()


def build_tree(board, player):
    tree = Tree()
    board = copy.deepcopy(board)
    build_tree_helper(board, tree.root, player)
    return tree


def build_tree_helper(board, root, player):
    for i, val in enumerate(ai.weigh_columns(board, player)):
        root.children.append(Node(i, val))
    return

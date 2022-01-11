"""
Implementation of Red Black Tree in python
"""


class Node:  # Node definition
    def __init__(self, value):
        self.red = False
        self.parent = None
        self.val = value
        self.left = None
        self.right = None


class RBTree:  # Tree definition

    def __init__(self):  # Making root for the first time
        self.nil = Node(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, value):  # Insert function
        new_node = Node(value)
        new_node.parent = None
        new_node.right = self.nil
        new_node.left = self.nil
        new_node.red = True

        parent = None
        current_node = self.root
        while current_node != self.nil:
            parent = current_node
            if new_node.val < current_node.val:
                current_node = current_node.left
            elif new_node.val > current_node.val:
                current_node = current_node.right
            else:
                return
        new_node.parent = parent
        if not parent:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def rotate_left(self, x: Node):  # Rotate left
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x.parent.right == x:
            x.parent.right = y
        else:
            x.parent.left = y

        y.left = x
        x.parent = y

    def rotate_right(self, x: Node):  # Rotate right
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.parent = y

    def fix_insert(self, new_node):  # Fix color of violence nodes
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # uncle
                if u.red:

                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # uncle

                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False

    def search(self, value):  # Search for specific value
        curr = self.root
        while curr != self.nil and curr.val != value:
            if value < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def __repr__(self):  # Representation of tree
        lines = []
        print_tree(self.root, lines)
        return '\n'.join(lines)


def print_tree(node, lines, level=0):  # Printing Tree
    if node.val != 0:
        print_tree(node.left, lines, level + 1)
        lines.append('-' * 4 * level + '> ' +
                     str(node.val) + ' ' + ('r' if node.red else 'b'))
        print_tree(node.right, lines, level + 1)

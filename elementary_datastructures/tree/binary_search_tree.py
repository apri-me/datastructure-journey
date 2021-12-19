class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return True
        temp = self.root
        while True:
            if temp.value == value:
                return False
            elif value < temp.value:
                if temp.left is None:
                    temp.left = node
                    return True
                temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    temp.right = node
                    return True
                temp = temp.right

    def __contains__(self, item):
        temp = self.root
        while True:
            if temp is None:
                return False
            if item == temp.value:
                return True
            elif item < temp.value:
                temp = temp.left
            elif item > temp.value:
                temp = temp.right
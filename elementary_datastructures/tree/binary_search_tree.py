class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None


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
                    node.parent = temp
                    return True
                temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    temp.right = node
                    node.parent = temp
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

    # we assume x to be Non-NIL
    @staticmethod
    def min_node_in_subtree(x: Node):
        temp = x
        while temp.left:
            temp = temp.left
        return temp

    # we assume x to be Non-NIL
    @staticmethod
    def max_node_in_subtree(x: Node):
        temp = x
        while temp.right:
            temp = temp.right
        return temp

    # we assume x to be Non-NIL
    def successor(self, x: Node):
        if x.right:
            return self.min_node_in_subtree(x.right)
        while True:
            if x.parent is None:
                return None
            if x.parent.left == x:
                return x.parent
            x = x.parent

    # we assume x to be Non-NIL
    def predecessor(self, x: Node):
        if x.left:
            return self.max_node_in_subtree(x.left).value
        while True:
            if x.parent is None:
                return None
            if x.parent.right == x:
                return x.parent.value
            x = x.parent

    # we assume x to be Non-NIL
    def traverse(self, x: Node):
        if x:
            self.traverse(x.left)
            print(x.value, end=" ")
            self.traverse(x.right)

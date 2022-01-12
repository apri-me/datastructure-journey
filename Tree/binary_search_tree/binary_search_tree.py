class Node:
    def __init__(self, val=None, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return f"[Node: val={self.val}, left={self.left}, right={self.right}]"


def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left

    return current


def delete_node(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete_node(root.left, key)

    elif key > root.val:
        root.right = delete_node(root.right, key)

    else:

        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)

    return root


class BST:
    root: Node

    def __init__(self, val=None) -> None:
        self.root = Node(val)

    def insert(self, key) -> None:
        x = y = self.root
        node = Node(key)
        flag = False
        while x:
            if x.val < key:
                y = x
                x = x.right
                flag = True
            else:
                y = x
                x = x.left
                flag = False
        node.parent = y
        if flag:
            y.right = node
        else:
            y.left = node

    def search(self, key) -> Node:
        x = self.root
        while x:
            if x.val < key:
                x = x.right
            elif x.val > key:
                x = x.left
            else:
                return x
        return None

    def inorder_traverse(self, node=None) -> list:
        if not node:
            node = self.root
        if not node:
            return []
        answer = []
        if node.left:
            answer += self.inorder_traverse(node.left)
        answer += [node.val]
        if node.right:
            answer += self.inorder_traverse(node.right)
        return answer

    def preorder_traverse(self, node=None) -> list:
        if not node:
            node = self.root
        if not node:
            return []
        answer = [node.val]
        if node.left:
            answer += self.preorder_traverse(node.left)
        if node.right:
            answer += self.inorder_traverse(node.right)
        return answer

    def postorder_traverse(self, node=None) -> list:
        if not node:
            node = self.root
        if not node:
            return []
        answer = []
        if node.left:
            answer += self.postorder_traverse(node.left)
        if node.right:
            answer += self.postorder_traverse(node.right)
        answer += [node.val]
        return answer

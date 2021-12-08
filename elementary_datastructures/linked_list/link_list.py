class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        pop = self.tail
        self.tail = temp
        self.tail.next = None
        self.length -= 1
        return pop

    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, value, index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, value, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        node = Node(value)
        temp = self.get(index - 1)
        node.next = temp.next
        temp.next = node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        temp = self.get(index - 1)
        node = temp.next
        temp.next = node.next
        node.next = None
        self.length -= 1
        return node

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

    def __str__(self):
        answer = str()
        temp = self.head
        while temp:
            answer += str(temp.value) + " "
            temp = temp.next
        return answer

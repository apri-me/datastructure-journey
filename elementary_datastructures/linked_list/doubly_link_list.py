class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkList:
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
            node.prev = self.tail
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
            self.head.prev = node
            self.head = node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        self.tail = temp.prev
        temp.prev = None
        if self.length == 1:
            self.head = None
        else:
            self.tail.next = None
        self.length -= 1
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        if self.length == 1:
            self.tail = None
        else:
            self.head.prev = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1 - index):
                temp = temp.prev
        return temp

    def set(self, value, index):
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
        if index == self.length:
            return self.append(value)
        node = Node(value)
        before = self.get(index - 1)
        after = before.next
        node.next = after
        node.prev = before
        before.next = node
        after.prev = node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        temp.prev = None
        temp.next = None
        before.next = after
        after.prev = before
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.tail
        while temp:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.next
        self.head, self.tail = self.tail, self.head
        return True

    def __str__(self):
        answer = str()
        temp = self.head
        while temp:
            answer += str(temp.value) + " "
            temp = temp.next
        return answer

'''
    Implementing Linked List with implementing whole memory and it's function like free and allocation.
'''

class Node: # Implementing of Node class
    def __init__(self, value) -> None: # Constructor
        self.val = value
        self.next = -1
        self.prev = -1
    
    def set_next(self, next_position) -> None: # Set next parameter in Node
        self.next = next_position
        
    def set_previous(self, previous_position) -> None: # Set previous parameter in Node
        self.prev = previous_position
        
    def set_value(self, value) -> None: # Set value parameter in Node
        self.val = value
    
    def __str__(self) -> str: # Getting string format of a node
        answer = ""
        answer += 'Previous: ' + str(self.prev) + ', Value: ' + str(self.val) + ', Next: ' + str(self.next)
        return answer

class Memory: # Implementing memory section.
    def __init__(self, memory_size) -> None: # Constructor function which create a memory with arbitrary size.
        self.memory = [Node(None) for _ in range(memory_size)]
        self.memory_size = memory_size
        for i in range(memory_size-1):
            self.memory[i].next = i+1
        self.free_index = 0
    
    def get_index(self, node) -> int: # Getting index of an arbitrary node in memory. If there is no root, it will return -1.
        for i in range(self.memory_size):
            if self.memory[i] == node:
                return i
        return -1
    
    def get_node(self, index) -> Node: # Getting node of memory[index].
        if index == -1:
            return None
        return self.memory[index]    
        
    def allocate(self) -> Node: # Allocating memory for new node.
        if self.free_index == -1:
            return None
        tmp = self.memory[self.free_index]
        self.free_index = tmp.next
        return tmp
    
    def free(self, node) -> None: # Free an allocated memory.
        target_index = self.get_index(node)
        if self.free_index == -1:
            self.memory[target_index].next = -1
            self.free_index = target_index
        else:
            self.memory[target_index].next = self.free_index
            self.free_index = target_index
    
    def get_data(self) -> list: # Getting a list of all nodes in memory.
        answer = []
        for i in self.memory:
            answer.append(i.__str__())
        answer += [self.free_index]
        return answer

class LinkedList: # Implementing Linked List class.
    def __init__(self, memory) -> None: # Constructor function.
        # Just consider this fact that in this method, both head and tail are integer which refrence to memory index of head and tail node.
        self.head = -1
        self.tail = -1
        self.memory = memory
        
    def append(self, value) -> None: # Appending new node with arbitrary value to Linked List.
        node = self.memory.allocate()
        if not node:
            print("There is now free space!")
            return
        node_index = self.memory.get_index(node)
        node.val = value
        if self.head == -1:
            self.head = node_index
            self.tail = node_index
            node.next = -1
        else:
            tmp = self.tail
            self.memory.memory[tmp].next = node_index
            self.tail = node_index
            node.prev = tmp
            node.next = -1
    
    def prepend(self, value) -> None: # Prepending new node with arbitrary value to Linked List.
        node = self.memory.allocate()
        if not node:
            print("There is no free space!")
            return
        node_index = self.memory.get_index(node)
        node.val = value
        if self.head == -1:
            self.head = node_index
            self.tail = node_index
        else:
            tmp = self.head
            self.memory.memory[tmp].prev = node_index
            self.head = node_index
            node.next = tmp
    
    def delete(self, value) -> None: # Delete a node with arbitrary value and free up the space.
        tmp = self.head
        while tmp != -1:
            n = self.memory.memory[tmp]
            if n.val == value:
                next_index = n.next
                prev_index = n.prev
                if prev_index != -1:
                    self.memory.memory[prev_index].next = next_index
                else:
                    if next_index != -1:
                        self.memory.memory[next_index].prev = -1
                        self.head = next_index
                    else:
                        self.head = -1
                        self.tail = -1
                if next_index != -1:
                    self.memory.memory[next_index].prev = prev_index
                else:
                    if prev_index != -1:
                        self.memory.memory[prev_index].next = -1
                        self.tail = prev_index
                    else:
                        self.head = -1
                        self.tail = -1
                self.memory.free(n)
            tmp = self.memory.memory[tmp].next
    
    def printer(self) -> None: # Print all available nodes' values.
        tmp = self.head
        while tmp != -1:
            print(self.memory.memory[tmp].val)
            tmp = self.memory.memory[tmp].next

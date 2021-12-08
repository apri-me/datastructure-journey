'''
    Implementing Linked list data structure with respect to Sentinel element method.
    In this program Sentinel element will be a node which is called nil.
    For safe programming reasons, nil.val will be None which will return some exceptions if in any part of the program we want to compare it with another node.
'''
class Node: # Node class which contain an arbitrary data type as value and two node which are the next and previous nodes.
    def __init__(self, value) -> None: # Constructor
        self.val = value
        self.next = None
        self.prev = None

class Linked_List: # Implementing Linked List 
    def __init__(self) -> None: # Constructor for Linked_List which will construct nil node.
        self.nil = Node(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil
    
    def get_head(self) -> Node: # get_head() function will return head of the link list.
        return self.nil.next

    def get_tail(self) -> Node: # get_tail() function will return tail of the link list.
        return self.nil.prev
    
    def append(self, key) -> None: # append() function will add new node to link list.
        tmp = Node(key)
        tail = self.get_tail()
        tail.next = tmp
        tmp.prev = tail
        tmp.next = self.nil
        self.nil.prev = tmp
    
    def prepend(self, key) -> None: # prepend() function will add new node to linked list head.
        tmp = Node(key)
        head = self.get_head()
        head.prev = tmp
        tmp.next = head
        self.nil.next = tmp
    
    def printer(self) -> None: # printer() function will print every nodes' value.
        head = self.get_head()
        while head != self.nil:
            print(head.val)
            head = head.next
    
    def get_all_elements(self) -> list: # get_all_elements() function will return a list of nodes' values.
        answer = []
        head = self.get_head()
        while head != self.nil:
            answer.append(head.val)
            head = head.next
        return answer
    
    def search(self, key) -> Node: # search() function will find a specific node with given key. If there is no node with that key, it will return None.
        head = self.get_head()
        while head != self.nil:
            if head.val == key:
                return head
            head = head.next
        return None
    
    
    def delete_node(self, key) -> None: # delete_node() function is using search function to find specific node and delete that node from linked list.
        target = self.search(key)
        if target:
            target.prev.next = target.next
            target.next.prev = target.prev
    
    def __str__(self) -> str: # this function will return all of elements in one string.
        answer = self.get_all_elements()
        string = ""
        for i in answer:
            string += str(i) + ' '
        return string[:len(string) - 1]
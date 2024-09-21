class Node:
    '''
    A node in a doubly linked list
    '''
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None 

class DoublyLinkedList:
    '''
    A doubly linked list
    '''
    def __init__(self):
        self.head = None  # Start of the linked list
        self.tail = None  # End of the linked list

    def append(self, data):
        '''
        Append a new node with data to the end of the list
        '''
        new_node = Node(data)
        
        if self.head is None:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:  # Append to the end of the list
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def print_forward(self):
        '''
        Print the list from the head to the tail
        '''
        current = self.head
        while current:
            print(current.data)
            current = current.next 
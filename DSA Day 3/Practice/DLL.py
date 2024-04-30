# 1. Code to create a insert_at_front function in a doubly linked list

class Node:
    def __init__(self,previous = None , element = None , next = None):
        self.previous = previous
        self.element = element
        self.next = next

class DoublyLinkedList :
    def __init__ (self):
        self.head = None

    def insert_at_fron(self ,element):
        if self.head == None :
            self.head = Node(None,element,None)
            return
        node = Node(None , element , self.head)
        self.head.previous = node
        self.head = node

    def insert_at_last (self , element):
        if self.head == None :
            self.head = Node (None , element , None)
            return
        
        itr = self.head
        while itr.next :
            itr = itr.next
        itr.next = Node(itr , element , None)

    def length(self):
        if self.head == None :
            return 0
        

    def print_forward(self) :
        if self.head == None :
            return f"Linked List is empty"
        itr = self.head
        string = ''
        while itr :
            string += str(itr.element) + '-->'
            itr = itr.next
        return string
    

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_fron(1)
    dll.insert_at_fron(2)
    dll.insert_at_fron(3)
    dll.insert_at_last(4)
    dll.insert_at_last(5)
    print(dll.print_forward()) # 3-->2-->1-->4-->5-->
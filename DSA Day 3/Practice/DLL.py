# 1. Code to create a insert_at_front function in a doubly linked list

class Node:
    def __init__(self,previous = None , element = None , next = None):
        self.previous = previous
        self.element = element
        self.next = next

class DoublyLinkedList :
    def __init__ (self):
        self.head = None

    def insert_at_front(self ,element):
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
        count = 0
        itr = self.head
        while itr :
            count += 1
            itr = itr.next
        return count
    
    def insert_at_index (self , index , element):
        if index < 0 or index > self.length():
            raise Exception('Invalid Index')
        if index == 0 :
            self.insert_at_fron(element)
            return
        count = 0
        itr = self.head
        while itr :
            if count == index -1 :
                node = Node (itr , element , itr.next)
                itr.next = node
                itr.next.previous = node
                break
            count += 1
            itr = itr.next

    def search (self , element):
        if self.head == None :
            raise Exception('Linked List is empty')
        itr = self.head
        count = 0
        while itr :
            if itr.element == element :
                print(count)
                return
            count += 1
            itr = itr.next
        print ("Element not found")

    def delete_first(self):
        if self.head == None :
            raise Exception('Linked List is empty')
        self.head = self.head.next
        self.head.previous = None

    def delete_last(self):
        if self.head == None :
            raise Exception('Linked List is empty')
        
        itr = self.head
        while itr.next :
            itr = itr.next
        itr.previous.next = None

    def delete_by_element(self , element):
        if self.head == None :
            raise Exception('Linked List is empty')
        
        itr = self.head
        while itr :

            if itr.next == None and itr.element == element :
                self.delete_last()
                return
            
            if itr.previous == None and itr.element == element :
                self.delete_first()
                return

            if itr.element == element :
                itr.previous.next = itr.next
                itr.next.previous = itr.previous
                return
            itr = itr.next
        print('Element not found')

    def print_forward(self) :
        if self.head == None :
            return f"Linked List is empty"
        itr = self.head
        string = ''
        while itr :
            string += str(itr.element) + '-->'
            itr = itr.next
        print(string)
    

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_front(5)
    dll.insert_at_front(10)
    dll.insert_at_front(15)
    dll.insert_at_last(20)
    dll.insert_at_last(25)
    dll.insert_at_last(30)
    dll.insert_at_index(3,35)
    dll.search(35) # 3
    dll.delete_first()
    dll.delete_last()
    dll.delete_by_element(10)
    dll.print_forward() # 15-->10-->5-->35-->20-->25-->30-->
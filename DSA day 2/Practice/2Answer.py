'''
2. Implement doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well. That way you can iterate in forward and backward direction.
Your node class will look this this,
```
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
```
Add following new methods,
```
def print_forward(self):
    # This method prints list in forward direction. Use node.next

def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
```
'''

class Node :
    def __init__(self , element , next , prev):
        self.element = element
        self.next = next
        self.prev = prev

class DBLinkedList :

    def __init__ (self):

        self.head = None

    def add_element_at_front(self , element):

        if self.head == None :

            node = Node(element , self.head , None)
            self.head = node
            return
        
        node = Node(element , self.head , None)
        self.head.prev = node
        self.head = node
    
    def print_forward(self):

        if self.head == None :
            print('The Doubly Linked List is empty')
            return
        
        itr = self.head
        dll = ''
        while itr :
            dll += str(itr.element) + '-->'
            itr = itr.next

        print('Forward Printing ......')
        print(dll)

    def print_backward(self):

        if self.head == None :
            print('The DOubly Linked List is empty')
            return
        
        itr = self.head
        while itr:
            if itr.next == None :
                break
            itr = itr.next
        
        dll = ''
        while itr :

            dll += str(itr.element) + '-->'
            itr = itr.prev
        
        print('Backward Printing ......')
        print(dll)

if __name__ == '__main__':
    dll = DBLinkedList()
    dll.add_element_at_front(5)
    dll.add_element_at_front(10)
    dll.add_element_at_front(15)
    dll.add_element_at_front(20)
    dll.add_element_at_front(25)
    dll.add_element_at_front(30)
    dll.print_forward()
    dll.print_backward()
# Using a class we can create the Node of the LinkedList

class Node :
  
  # We will initiate this Node by defining the element and the pointer through __init__ constructor

  def __init__(self , element = None , nxtPointer = None) :
    
    self.element = element
    self.nxtPointer = nxtPointer

class LinkedList:
    def __init__(self):
        self.head = None

    def add_from_front(self, element):
        node = Node(element , self.head)
        self.head = node
    
    def print(self):
        if self.head == None :
            print('The Linked List is empty')
        else :
            itr = self.head
            llist = ''

            while itr :
                llist += str(itr.element) + '-->'
                itr = itr.nxtPointer
            print (llist)

# Example usage
if __name__ == '__main__':
    ll = LinkedList()
    ll.add_from_front(5)
    ll.add_from_front(89)
    ll.add_from_front(11)
    ll.print()